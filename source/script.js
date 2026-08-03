/* ═══ NEGESP V2 · motor (arquitetura 2) ═══ */
(function(){
'use strict';
const $=(s,c)=>(c||document).querySelector(s), $$=(s,c)=>[...(c||document).querySelectorAll(s)];
const slides=$$('.slide'); const N=slides.length;
const reduced=matchMedia('(prefers-reduced-motion: reduce)').matches;

/* palavras animadas */
$$('[data-words]').forEach(el=>{
  const parts=[]; let d=0;
  el.childNodes.forEach(node=>{
    if(node.nodeType===3){
      node.textContent.split(/(\s+)/).forEach(tk=>{
        if(!tk)return;
        if(/^\s+$/.test(tk)){parts.push(tk);return;}
        parts.push(`<span class="w" style="--wd:${d+=55}">${tk}</span>`);
      });
    }else if(node.nodeType===1){
      const cl=node.getAttribute('class')||'';
      if(!node.textContent.trim()){parts.push(`<span class="${cl}"></span>`);return;}
      const inner=node.textContent.split(/(\s+)/).map(tk=>{
        if(!tk||/^\s+$/.test(tk))return tk;
        return `<span class="w" style="--wd:${d+=55}">${tk}</span>`;
      }).join('');
      parts.push(`<span class="${cl}">${inner}</span>`);
    }
  });
  el.innerHTML=parts.join('');
});

/* passos */
const stepMax=slides.map(s=>{
  const auto=$$('.st',s).filter(e=>!e.dataset.st);
  auto.forEach((e,i)=>e.dataset.st=i+1);
  return Math.max(0,...$$('.st',s).map(e=>+e.dataset.st));
});
const step=new Array(N).fill(0);
function applySteps(i){
  $$('.st',slides[i]).forEach(e=>e.classList.toggle('go',+e.dataset.st<=step[i]));
  if(slides[i].id==='s05'&&window.__s05link)window.__s05link(step[i]>=4);
  if(slides[i].id==='s13'&&window.__s13step)window.__s13step(step[i]);
  if(slides[i].id==='s10'&&window.__s10sync)window.__s10sync();
}

const hudTitle=$('#hudTitle'),hudNum=$('#hudNum'),progBar=$('#progBar');
const notesBar=$('#notesBar'),notesTxt=$('#notesTxt'),menu=$('#menu');

/* ── desenhadores de conexões (retângulos reais: respeita translate/centralização) ── */
function off(el,root){const a=el.getBoundingClientRect(),b=root.getBoundingClientRect();return[a.left-b.left,a.top-b.top];}
function mid(el,root){const a=el.getBoundingClientRect(),b=root.getBoundingClientRect();return[a.left+a.width/2-b.left,a.top+a.height/2-b.top];}
function half(el){const r=el.getBoundingClientRect();return[r.width/2,r.height/2];}
function prepSvg(svg){const p=svg.parentElement,r=p.getBoundingClientRect();svg.setAttribute('viewBox',`0 0 ${r.width} ${r.height}`);svg.innerHTML='';return p;}
function q(svg,[x1,y1],[x2,y2],lift,cls){
  const mx=(x1+x2)/2,my=(y1+y2)/2-(lift||0);
  const el=document.createElementNS('http://www.w3.org/2000/svg','path');
  el.setAttribute('d',`M${x1} ${y1} Q${mx} ${my} ${x2} ${y2}`);
  if(cls)el.setAttribute('class',cls);
  svg.appendChild(el);
}
function drawS08(){
  const s=$('#s08'),svg=$('svg.links',s);if(!svg)return;const root=prepSvg(svg);
  const g=n=>$(`.dcard.${n}`,s);
  const fed=mid(g('fed'),root),est=mid(g('est'),root),mun=mid(g('mun'),root),srv=mid(g('srv'),root);
  q(svg,fed,est,30);q(svg,fed,mun,30);q(svg,est,srv,-30);q(svg,mun,srv,-30);
}
function drawS10(){
  const s=$('#s10'),svg=$('svg.beams',s);if(!svg)return;const root=prepSvg(svg);
  const NS='http://www.w3.org/2000/svg';
  const [cx,cy]=mid($('.core',s),root);
  /* feixes de CENTRO a CENTRO; núcleo (z2) e cards (z2) ficam por cima e
     escondem as pontas — nunca há folga, seja qual for o tamanho do pino */
  $$('.fn',s).forEach((f,idx)=>{
    const [fx,fy]=mid(f,root);
    const g=document.createElementNS(NS,'g');
    g.setAttribute('class','bgrp');g.dataset.st=f.dataset.st||'';
    const dy=fy-cy, dx=fx-cx;
    const curv=Math.abs(dy)<60?0:(dy<0?-58:58);
    const d=`M ${cx},${cy} Q ${(cx+fx)/2},${(cy+fy)/2+curv} ${fx},${fy}`;
    const base=document.createElementNS(NS,'path');
    base.setAttribute('class','bbase');base.setAttribute('d',d);
    const pulse=document.createElementNS(NS,'path');
    pulse.setAttribute('class','bpulse');pulse.setAttribute('d',d);
    g.appendChild(base);g.appendChild(pulse);svg.appendChild(g);
    const L=pulse.getTotalLength();
    pulse.style.strokeDasharray=`${L*.22} ${L}`;
    pulse.style.setProperty('--boff',String(L*1.22));
    pulse.style.setProperty('--bt',(2.8+idx*.35)+'s');
    pulse.style.setProperty('--bd',(idx*.5)+'s');
  });
  window.__s10sync&&window.__s10sync();
}
window.__s10sync=function(){
  const s=document.getElementById('s10');if(!s)return;
  const fns=[...s.querySelectorAll('.fn')];
  [...s.querySelectorAll('.bgrp')].forEach((g,i)=>{
    g.classList.toggle('go',fns[i]&&fns[i].classList.contains('go'));
  });
}
function drawS14(){
  const s=$('#s14'),svg=$('svg.ties',s);if(!svg)return;const root=prepSvg(svg);
  const node=$('#mindNode',s),nm=mid(node,root);
  [['#blkFn',-1],['#blkComp',-1],['#blkAtr',1]].forEach(([sel,side])=>{
    const b=$(sel,s);if(!b)return;const[bx,by]=off(b,root);
    const br=b.getBoundingClientRect();
    const p=side<0?[bx+br.width,by+br.height/2]:[bx,by+br.height/2];
    q(svg,nm,p,20);
  });
}
function drawS15(){
  const s=$('#s15'),svg=$('svg.path',s);if(!svg)return;const root=prepSvg(svg);
  const steps=$$('.stepc',s).map(el=>{const[x,y]=off(el,root);return[x+el.getBoundingClientRect().width/2,y];});
  for(let i=0;i<steps.length-1;i++)q(svg,steps[i],steps[i+1],36);
  const res=$('.result .badge',s);if(res){const[rx,ry]=off(res,root);const rr=res.getBoundingClientRect();
    q(svg,steps[2],[rx+rr.width/2,ry+rr.height],26);}
}
function drawS17(){
  const s=$('#s17'),svg=$('svg.rays',s);if(!svg)return;const root=prepSvg(svg);
  const hub=mid($('#fanHub',s),root);
  $$('.qd',s).forEach(c=>{const[x,y]=off(c,root);q(svg,hub,[x,y+c.getBoundingClientRect().height/2],26);});
}
const SCENES={s08:drawS08,s10:drawS10,s14:drawS14,s15:drawS15,s17:drawS17};

/* navegação */
let cur=-1;
function goTo(i,full){
  i=Math.max(0,Math.min(N-1,i));
  if(i===cur&&full===undefined)return;
  if(cur>=0)slides[cur].classList.remove('on');
  cur=i;
  const s=slides[cur];
  s.classList.add('on');
  document.body.classList.toggle('light', cur!==0);
  document.body.classList.toggle('showlogo', cur>=1 && cur<N-1); /* logo em todos, exceto capa e encerramento */
  if(full)step[cur]=stepMax[cur];
  if(s.id==='s13')step[cur]=0;            /* s13 sempre entra pela órbita, mesmo em acesso direto/índice */
  applySteps(cur);
  hudTitle.textContent=s.dataset.title||'';
  hudNum.innerHTML='<b>'+String(cur+1).padStart(2,'0')+'</b> · '+String(N).padStart(2,'0');
  progBar.style.width=((cur+1)/N*100)+'%';
  notesTxt.textContent=($('aside.notes',s)||{}).textContent||'';
  history.replaceState(null,'','#'+(cur+1));
  requestAnimationFrame(()=>requestAnimationFrame(()=>{SCENES[s.id]&&SCENES[s.id]();}));
  setTimeout(()=>{if(slides[cur]===s&&SCENES[s.id])SCENES[s.id]();},950);
  if(s.id==='s11')armMap();
  if(s.id==='s16')armNet();
  if(s.id==='s12')armGear();
}
function next(){ if(step[cur]<stepMax[cur]){step[cur]++;applySteps(cur);} else goTo(cur+1); }
function prev(){ if(step[cur]>0){step[cur]--;applySteps(cur);} else goTo(cur-1,true); }
window.goTo=goTo;window.next=next;window.prev=prev;

addEventListener('keydown',e=>{
  if(e.key==='ArrowRight'||e.key===' '||e.key==='PageDown'){e.preventDefault();next();}
  else if(e.key==='ArrowLeft'||e.key==='PageUp'){e.preventDefault();prev();}
  else if(e.key==='Home'){goTo(0);}
  else if(e.key==='End'){goTo(N-1,true);}
  else if(e.key==='f'||e.key==='F'){document.fullscreenElement?document.exitFullscreen():document.documentElement.requestFullscreen();}
  else if(e.key==='n'||e.key==='N'){notesBar.classList.toggle('open');}
  else if(e.key==='o'||e.key==='O'){menu.classList.toggle('open');}
  else if(e.key==='Escape'){menu.classList.remove('open');notesBar.classList.remove('open');}
});
addEventListener('click',e=>{
  if(portraitLock&&portraitLock())return;
  if(e.target.closest('.menu a'))return;
  if(e.target.closest('.menu')){menu.classList.remove('open');return;}
  if(e.clientX>innerWidth*.6)next(); else if(e.clientX<innerWidth*.25)prev();
});
$$('.menu a').forEach(a=>a.addEventListener('click',e=>{
  e.preventDefault();menu.classList.remove('open');goTo(+a.dataset.i,true);
}));

/* scroll: roda do mouse / trackpad — com acumulador e período refratário */
let wAcc=0,wLock=0;
addEventListener('wheel',e=>{
  if(menu.classList.contains('open'))return;
  e.preventDefault();
  const now=performance.now();
  if(now<wLock)return;
  wAcc+=e.deltaY+e.deltaX;
  if(Math.abs(wAcc)>70){
    (wAcc>0?next:prev)();
    wAcc=0;wLock=now+760;
  }
},{passive:false});
/* gesto de arrastar (touch) — inerte enquanto o aviso de girar a tela está visível */
const portraitLock=()=>matchMedia('(orientation:portrait) and (pointer:coarse)').matches;
let tx=0,ty=0;
addEventListener('touchstart',e=>{tx=e.touches[0].clientX;ty=e.touches[0].clientY;},{passive:true});
addEventListener('touchend',e=>{
  if(portraitLock())return;
  if(e.touches.length>0)return; /* pinch em andamento: não navegar */
  const dx=e.changedTouches[0].clientX-tx,dy=e.changedTouches[0].clientY-ty;
  if(Math.max(Math.abs(dx),Math.abs(dy))<42)return;
  (Math.abs(dx)>Math.abs(dy)?(dx<0?next:prev):(dy<0?next:prev))();
},{passive:true});

addEventListener('resize',()=>{const s=slides[cur];s&&SCENES[s.id]&&SCENES[s.id]();});

/* partículas */
const cv=$('#dust'),ctx=cv.getContext('2d');let P=[];
function sizeCv(){cv.width=innerWidth*devicePixelRatio;cv.height=innerHeight*devicePixelRatio;}
sizeCv();addEventListener('resize',sizeCv);
if(!reduced){
  const M=Math.min(90,Math.round(innerWidth/18));
  for(let i=0;i<M;i++)P.push({x:Math.random(),y:Math.random(),r:Math.random()*1.6+.4,
    v:Math.random()*.00022+.00007,s:Math.random()*.0004-.0002,o:Math.random()*.5+.1,
    c:Math.random()<.82?'47,191,131':'255,138,60',ph:Math.random()*6.28});
  (function tick(t){
    ctx.clearRect(0,0,cv.width,cv.height);
    for(const p of P){
      p.y-=p.v;p.x+=Math.sin(t*.0004+p.ph)*p.s;
      if(p.y<-.02){p.y=1.02;p.x=Math.random();}
      const tw=.55+.45*Math.sin(t*.0011+p.ph*3);
      ctx.beginPath();
      ctx.arc(p.x*cv.width,p.y*cv.height,p.r*devicePixelRatio,0,6.283);
      ctx.fillStyle=`rgba(${p.c},${(p.o*tw*.5).toFixed(3)})`;
      ctx.fill();
    }
    requestAnimationFrame(tick);
  })(0);
}

/* mapa */
const MAP=%%MAPDATA%%;
function buildMap(svg){
  svg.setAttribute('viewBox',`0 0 ${MAP.w} ${MAP.h}`);
  let g='<g class="ufs">';
  for(const u of MAP.ufs)g+=`<path class="uf" id="${svg.id}-${u.id}" d="${u.d}"></path>`;
  g+='</g><g class="arcs"></g><g class="caps"></g>';
  svg.innerHTML=g;
}
const mapMain=$('#mapMain');if(mapMain)buildMap(mapMain);
const mapNet=$('#mapNet');if(mapNet)buildMap(mapNet);
const DF=MAP.ufs.find(u=>u.id==='DF');

let mapArmed=false;
function armMap(){
  if(mapArmed||!mapMain)return;mapArmed=true;
  const EASE='cubic-bezier(.32,.72,0,1)';
  $$('path.uf',mapMain).forEach((p,i)=>{
    const L=p.getTotalLength();
    p.style.strokeDasharray=L;
    p.animate([{strokeDashoffset:L},{strokeDashoffset:0}],
      {duration:1100,delay:i*45,easing:EASE,fill:'both'});
    p.animate([{fillOpacity:0},{fillOpacity:1}],
      {duration:900,delay:700+i*45,easing:'ease',fill:'both'});
  });
  const rs=$('#mapMain-RS');if(rs)setTimeout(()=>rs.classList.add('dest'),1400+27*45);
  const arcsG=$('.arcs',mapMain),capsG=$('.caps',mapMain);
  capsG.innerHTML=`<circle class="hub" cx="${DF.cx}" cy="${DF.cy}" r="7"></circle>`;
  MAP.ufs.filter(u=>u.id!=='DF').forEach((u,i)=>{
    const mx=(DF.cx+u.cx)/2,my=(DF.cy+u.cy)/2-Math.hypot(u.cx-DF.cx,u.cy-DF.cy)*.22;
    const el=document.createElementNS('http://www.w3.org/2000/svg','path');
    el.setAttribute('class','arc');el.setAttribute('d',`M${DF.cx} ${DF.cy} Q${mx} ${my} ${u.cx} ${u.cy}`);
    if(u.id==='RS'){el.style.stroke='rgba(232,119,34,.8)';el.style.strokeWidth='1.6';}
    arcsG.appendChild(el);
    const L=el.getTotalLength();
    el.style.strokeDasharray=L;
    el.animate([{strokeDashoffset:L},{strokeDashoffset:0}],
      {duration:900,delay:1200+i*70,easing:EASE,fill:'both'});
    const c=document.createElementNS('http://www.w3.org/2000/svg','circle');
    c.setAttribute('class','cap');c.setAttribute('r',u.id==='RS'?4:2.6);
    c.setAttribute('cx',u.cx);c.setAttribute('cy',u.cy);
    if(u.id==='RS')c.style.fill='#E87722';
    c.animate([{opacity:0},{opacity:1}],{duration:500,delay:1950+i*70,easing:'ease',fill:'both'});
    capsG.appendChild(c);
  });
  const el=$('#ufcount');let v=0;el.textContent='0';
  const iv=setInterval(()=>{v++;el.textContent=v;if(v>=26)clearInterval(iv);},52);
}

let netArmed=false;
function armNet(){
  if(!mapNet||netArmed)return;netArmed=true;
  const arcsG=$('.arcs',mapNet),capsG=$('.caps',mapNet);
  capsG.innerHTML=`<circle class="hub" cx="${DF.cx}" cy="${DF.cy}" r="6"></circle>`;
  const others=MAP.ufs.filter(u=>u.id!=='DF');
  function wave(){
    arcsG.innerHTML='';
    [...others].sort(()=>Math.random()-.5).slice(0,9).forEach((u,i)=>{
      const mx=(DF.cx+u.cx)/2,my=(DF.cy+u.cy)/2-Math.hypot(u.cx-DF.cx,u.cy-DF.cy)*.2;
      const el=document.createElementNS('http://www.w3.org/2000/svg','path');
      el.setAttribute('class','net');
      el.setAttribute('d',`M${DF.cx} ${DF.cy} Q${mx} ${my} ${u.cx} ${u.cy}`);
      arcsG.appendChild(el);
      const L=el.getTotalLength();
      el.style.strokeDasharray=L;
      el.animate([{strokeDashoffset:L},{strokeDashoffset:0}],
        {duration:1000,delay:i*90,easing:'cubic-bezier(.32,.72,0,1)',fill:'both'});
      el.animate([{opacity:1},{opacity:0}],{duration:800,delay:1900+i*40,easing:'ease',fill:'both'});
    });
  }
  wave();
  if(!reduced)setInterval(wave,3200);
}

let gearArmed=false;
function armGear(){
  if(gearArmed)return;gearArmed=true;
  const g=$('#gearSpin');
  if(g&&!reduced)g.animate([{transform:'rotate(0deg)'},{transform:'rotate(360deg)'}],{duration:14000,iterations:Infinity});
}


/* s05: pontos dispersos que se conectam (porta do modelo clássico) */
(function(){
  const stage = document.querySelector('#s05 .dotstage');
  if(!stage) return;
  let seed = 7;
  const rnd = ()=> (seed = (seed*16807)%2147483647) / 2147483647;
  const N = 24, dots = [], scatter = [], net = [];
  for(let i=0;i<N;i++){
    scatter.push([6+rnd()*88, 4+rnd()*88]);
    const ring = i%2, ang = (i/N)*Math.PI*2;
    const r = ring? 26 : 40;
    net.push([50 + Math.cos(ang)*r, 50 + Math.sin(ang)*r*0.92]);
  }
  const svg = stage.querySelector('svg');
  for(let i=0;i<N;i++){
    const d = document.createElement('div');
    d.className='dot';
    d.style.left = scatter[i][0]+'%';
    d.style.top  = scatter[i][1]+'%';
    d.style.animationDelay = (rnd()*2)+'s';
    stage.appendChild(d);
    dots.push(d);
  }
  const lines = [];
  for(let i=0;i<N;i++){
    const j = (i+2)%N;
    const L = document.createElementNS('http://www.w3.org/2000/svg','line');
    svg.appendChild(L); lines.push([L,i,j]);
  }
  window.__s05link = (on)=>{
    dots.forEach((d,i)=>{
      const p = on? net[i] : scatter[i];
      d.style.left = p[0]+'%'; d.style.top = p[1]+'%';
    });
    lines.forEach(([L,i,j])=>{
      const a = on? net[i]:scatter[i], b = on? net[j]:scatter[j];
      L.setAttribute('x1',a[0]+'%');L.setAttribute('y1',a[1]+'%');
      L.setAttribute('x2',b[0]+'%');L.setAttribute('y2',b[1]+'%');
    });
    document.getElementById('s05').classList.toggle('linked', on);
    const ta = document.querySelector('#s05 .tt-a'), tb = document.querySelector('#s05 .tt-b');
    if(ta&&tb){ ta.hidden = on; tb.hidden = !on; }
  };
  window.__s05link(false);
})();


/* s13: órbita radial (porta do 21st.dev · Radial Orbital Timeline) */
(function(){
  const orb=document.getElementById('orb5');
  if(!orb)return;
  const sec=document.getElementById('s13');
  const nodes=[...orb.querySelectorAll('.onode')];
  let ang=90, tAng=90, auto=true;
  function layout(){
    const W=orb.clientWidth,H=orb.clientHeight;
    if(!W||!H)return;
    const R=Math.min(W*.42,H*.33);
    nodes.forEach((n,i)=>{
      const a=((i/nodes.length)*360+ang)%360, rad=a*Math.PI/180;
      const x=W/2+R*Math.cos(rad), y=H/2+R*Math.sin(rad)*0.92;
      const open=n.classList.contains('open');
      const depth=(1-Math.sin(rad))/2;           /* 1 = topo (frente do palco) */
      n.style.left=x+'px'; n.style.top=y+'px';
      n.style.zIndex=open?200:Math.round(50+depth*50);
      const vis=n.classList.contains('go');
      n.style.opacity=vis?(open?1:(0.45+0.55*depth)):0;
      n.style.pointerEvents=vis?'auto':'none';
      n.style.scale=open?'1.12':String(.84+.24*depth);
    });
  }
  (function tick(){
    if(sec.classList.contains('on')){
      if(auto&&!reduced)tAng=(tAng+0.1)%360;
      ang+=(tAng-ang)*0.08;
      layout();
    }
    requestAnimationFrame(tick);
  })();
  function openNode(n){
    nodes.forEach(m=>m.classList.toggle('open',m===n));
    auto=false;
    const i=nodes.indexOf(n);
    tAng=270-(i/nodes.length)*360;               /* leva o nó ao topo */
    ang=tAng-24;                                  /* pequena chegada animada */
  }
  function closeAll(){nodes.forEach(m=>m.classList.remove('open'));auto=true;}
  nodes.forEach(n=>{
    n.querySelector('.obtn').addEventListener('click',e=>{
      e.stopPropagation();
      n.classList.contains('open')?closeAll():openNode(n);
    });
  });
  orb.querySelectorAll('.orel button').forEach(b=>b.addEventListener('click',e=>{
    e.stopPropagation();
    openNode(nodes[+b.dataset.goto]);
  }));
  orb.addEventListener('click',e=>{e.stopPropagation();if(!e.target.closest('.onode'))closeAll();});
  window.__s13step=(st)=>{
    const sec=document.getElementById('s13');
    if(st>=5){ closeAll(); sec.classList.add('summaryon'); return; }
    sec.classList.remove('summaryon');
    if(st<=0){closeAll();return;}
    const n=nodes.find(m=>+m.dataset.st===st);
    if(n)openNode(n);
  };
})();

const h=parseInt(location.hash.slice(1),10);
goTo(isNaN(h)?0:h-1,!isNaN(h));
/* redesenha a cena atual quando a fonte embutida terminar de carregar
   (as larguras dos cards mudam e os conectores precisam nascer nas bordas certas) */
if(document.fonts&&document.fonts.ready)document.fonts.ready.then(()=>{
  const s=slides[cur];if(s&&SCENES[s.id])SCENES[s.id]();
});
})();
