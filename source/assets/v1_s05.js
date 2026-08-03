(function(){
  const stage = document.querySelector('#s05 .dotstage');
  if(!stage) return;
  let seed = 7;
  const rnd = ()=> (seed = (seed*16807)%2147483647) / 2147483647;
  const N = 24, dots = [], scatter = [], net = [];
  // posições em rede: anel duplo organizado
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
  // linhas da rede (vizinhos no anel)
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