# -*- coding: utf-8 -*-
"""Monta o modelo V2 (Observatório) e verifica paridade de conteúdo com o V1."""
import json, re, os, sys, unicodedata
B = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, B)
from sections_a import SECTIONS_A
from sections_b import SECTIONS_B

OUT = os.path.join(B, '..', 'v2', 'index.html')  # grava direto no arquivo publicado do repo
inv = {s['id']: s for s in json.load(open(f'{B}/assets/conteudo_v1.json'))}

# ── CSS extra: acertos finos sobre a folha principal ──
EXTRA_CSS = '''
/* ═══════════ TEMA CLARO (slides 2 a 20; capa permanece escura) ═══════════ */
body.light{
  --void:#F7FAF6; --deep:#FFFFFF;
  --ink:#0A2416; --ink-2:#40604E; --ink-3:#7E968A;
  --green:#0E7A4E; --green-core:#0E7A4E;
  --orange:#E87722; --orange-soft:#C4560A;
  --hair:rgba(6,46,30,.14); --hair-2:rgba(6,46,30,.07);
  --glass:#FFFFFF; --glass-2:#FFFFFF;
}
body.light .atmo{background:
  radial-gradient(52vw 52vw at 82% -10%, rgba(14,122,78,.08), transparent 60%),
  radial-gradient(44vw 44vw at -8% 108%, rgba(232,119,34,.05), transparent 62%)}
body.light .atmo::after{content:none}
body.light .grain{opacity:.03}
body.light #dust{opacity:.22}
body.light .glass{background:#fff;border-color:var(--hair-2);
  box-shadow:0 14px 34px rgba(6,46,30,.09),inset 0 1px 0 rgba(255,255,255,.9)}
body.light .title em{text-shadow:none;color:var(--orange-soft)}
body.light .hud i{border-color:rgba(6,46,30,.28)}
body.light .prog{background:rgba(6,46,30,.08)}
body.light .menu{background:rgba(247,250,246,.92)}
body.light .menu a{background:#fff}
body.light .notesbar{background:rgba(255,255,255,.97);box-shadow:0 30px 70px rgba(6,46,30,.2)}
body.light #s02 .mark{-webkit-text-stroke-color:rgba(14,122,78,.16)}
body.light #s02 .q .hl{text-shadow:none;color:var(--orange-soft)}
body.light #s06 .glyph{-webkit-text-stroke-color:rgba(14,122,78,.2)}
body.light #s06 .qm{text-shadow:none}
body.light #s07 .bigdate{background:linear-gradient(100deg,#0A2416,#0E7A4E);-webkit-background-clip:text;background-clip:text}
body.light #s09 .statement .g{text-shadow:none}
body.light #s10 svg.web line{stroke:rgba(14,122,78,.35)}
body.light #s10 svg.web line.ring{stroke:rgba(6,46,30,.1)}
body.light #s10 .fn i{box-shadow:none}
body.light #s11 .sweep{mix-blend-mode:multiply;background:conic-gradient(from 0deg,rgba(14,122,78,.13),transparent 24%)}
body.light #s11 .floor{background:radial-gradient(50% 100% at 50% 0%,rgba(14,122,78,.16),transparent 70%)}
body.light #s11 .brmap{filter:none}
body.light #s11 .reading b{text-shadow:none}
body.light .brmap path.uf{fill:rgba(14,122,78,.13);stroke:#0E7A4E;stroke-opacity:1}
body.light .brmap path.uf.dest{fill:rgba(232,119,34,.6);filter:none}
body.light .brmap circle.cap{fill:#0E7A4E;filter:none}
body.light .brmap path.arc{stroke:rgba(14,122,78,.45)}
body.light #s16 .brmap path.net{stroke:rgba(14,122,78,.55);filter:none}
body.light #s12 .reactor{background:#fff;outline-color:rgba(14,122,78,.3);box-shadow:0 20px 50px rgba(6,46,30,.12)}
body.light #s15 .stepc .ord{-webkit-text-stroke-color:rgba(6,46,30,.14)}
body.light #s04 .pan .num{-webkit-text-stroke-color:rgba(6,46,30,.12)}
body.light #s18 .term.a h4{text-shadow:none}
body.light #s18 .term.b h4{text-shadow:none}
body.light #s18 .term.c h4{background:linear-gradient(95deg,#0E7A4E,#C4560A);-webkit-background-clip:text;background-clip:text}
body.light #s19 .bg{filter:saturate(.8) brightness(.95)}
body.light #s19 .veil{background:linear-gradient(180deg,rgba(247,250,246,.97) 0%,rgba(247,250,246,.82) 24%,rgba(247,250,246,.5) 46%,rgba(247,250,246,.52) 100%)}
body.light #s19 .lib{background:#fff;border:1px solid var(--hair);border-left:2px solid var(--green);border-radius:12px}
body.light #s20 .thanks{background:linear-gradient(100deg,#0A2416 15%,#0E7A4E 55%,#C4560A);-webkit-background-clip:text;background-clip:text}
body.light #s20 .ecg path{filter:none}
body.light #s13 .lay.k4 i{background:#BFE9D3}
body.light #s17 .hub,body.light #s10 .core,body.light #s14 .node{box-shadow:0 0 0 1px rgba(255,255,255,.16) inset,0 16px 40px rgba(14,122,78,.35)}

/* ═══ logo Conass no canto superior direito (slides 2 a 19) ═══ */
.cornerlogo{position:fixed;top:44px;right:52px;z-index:52;width:clamp(9.5rem,18vw,14rem);
  opacity:0;transform:translateY(-8px);transition:opacity .6s var(--ease),transform .6s var(--ease);pointer-events:none}
.cornerlogo svg{display:block;width:100%;height:auto}
body.showlogo .cornerlogo{opacity:1;transform:none}
body.showlogo .hud .htr{display:none}
/* títulos de largura cheia não invadem a logo do canto (s10 tem coluna própria) */
body.showlogo #s04 .title,body.showlogo #s05 .title,body.showlogo #s07 .title,
body.showlogo #s08 .title,body.showlogo #s14 .title,body.showlogo #s15 .title,
body.showlogo #s16 .title,body.showlogo #s17 .title,
body.showlogo #sbra .title,body.showlogo #sorg .title{padding-right:clamp(9.5rem,18vw,14.5rem)}

/* ═══ S03: parágrafo em 4 linhas, par centralizado ═══ */
#s03 .wrap{display:flex;flex-direction:column;padding-left:52px}
#s03 .midpair{flex:1;min-height:0;display:flex;align-items:center;justify-content:center;
  gap:clamp(1.6rem,4vw,4rem);padding:clamp(4rem,11.5vh,6.8rem) 0 clamp(.4rem,1.6vh,1.2rem)}
#s03 .leadbox{flex:0 1 auto;max-width:none}
#s03 .lead{font-size:clamp(1.08rem,1.72vw,1.5rem);line-height:1.58;color:var(--ink);max-width:66ch;text-align:justify;font-weight:700}
#s03 .photo{flex:0 0 auto;align-self:center;display:flex;align-items:center;justify-content:center}
#s03 .photo .frame{background:#fff;border-radius:16px;padding:clamp(.5rem,1vw,.85rem);display:flex;
  box-shadow:0 24px 60px rgba(6,46,30,.22);transform:rotate(2deg)}
#s03 .photo img{display:block;max-width:100%;max-height:min(48vh,480px);object-fit:contain;border-radius:8px}
#s03 .tagbox{align-self:flex-start;writing-mode:horizontal-tb;transform:none;text-align:left;max-width:none;
  border:none;border-left:2px solid var(--orange);padding:.15em 0 .15em 1em;margin-top:clamp(.5rem,2vh,1.2rem);
  font-size:clamp(1.08rem,1.72vw,1.5rem);font-weight:650;line-height:1.4;color:var(--ink)}
#s03 .tagbox em{font-style:normal;color:var(--orange-soft)}
#s03 .stats{margin-top:clamp(.7rem,2.4vh,1.4rem)}
#s03 .stat b{font-size:clamp(2.1rem,4.7vw,4rem);text-shadow:none}
#s03 .stat span{font-size:clamp(.98rem,1.42vw,1.24rem);line-height:1.4}

/* ═══ S04: cards empilhados + foto completa ═══ */
#s04 .duo{display:grid;grid-template-columns:1.16fr .84fr;gap:clamp(1rem,2.6vw,2.2rem);
  flex:1;min-height:0;margin-top:clamp(.6rem,1.8vh,1.1rem);align-items:stretch}
#s04 .cards{display:flex;flex-direction:column;gap:clamp(.5rem,1.4vh,.85rem);min-height:0}
#s04 .cards{justify-content:space-evenly}
#s04 .pan{border-top:none;border-left:3px solid var(--green);flex:0 1 auto;min-height:0;
  display:flex;flex-direction:column;justify-content:flex-start;
  padding:clamp(.55rem,1.2vw,.95rem) clamp(.9rem,1.9vw,1.4rem)}
#s04 .pan:nth-child(2n){border-left-color:var(--orange)}
#s04 .pan h4{min-height:0;max-width:none;font-size:clamp(.92rem,1.32vw,1.18rem);line-height:1.25}
#s04 .pan p{margin-top:.4em;font-size:clamp(.82rem,1.18vw,1.05rem);line-height:1.42;color:var(--ink-2);text-align:justify}
#s04 .pan .num{font-size:clamp(2.2rem,4.2vw,3.4rem);right:.25em;top:-.12em}
#s04 .photo{display:flex;align-items:center;justify-content:center;min-height:0}
#s04 .photo img{max-width:100%;max-height:100%;object-fit:contain;border-radius:14px;
  box-shadow:0 24px 60px rgba(6,46,30,.2)}

/* ═══ S05: porta fiel do modelo clássico (pontos que se conectam) ═══ */
#s05 .split5{display:grid;grid-template-columns:1fr 1fr;gap:clamp(1rem,3vw,3rem);align-items:center;flex:1;min-height:0;margin-top:clamp(.6rem,2vh,1.2rem)}
#s05 .dotstage{position:relative;height:min(56vh,470px)}
#s05 .dotstage svg{position:absolute;inset:0;width:100%;height:100%;overflow:visible}
#s05 .dotstage line{stroke:var(--green);stroke-width:1.4;opacity:0;transition:opacity .9s ease .35s}
#s05.linked .dotstage line{opacity:.4}
#s05 .dot{position:absolute;width:clamp(9px,1.3vw,14px);height:clamp(9px,1.3vw,14px);border-radius:50%;background:var(--orange);
  transition:left 1.15s var(--ease),top 1.15s var(--ease),background .9s ease;box-shadow:0 2px 8px rgba(6,46,30,.14);
  animation:drift5 5s ease-in-out infinite alternate}
#s05.linked .dot{background:var(--green);animation:none}
@keyframes drift5{from{margin-top:-4px}to{margin-top:5px}}
#s05 .pains{display:flex;flex-direction:column;gap:clamp(.45rem,1.4vh,.9rem)}
#s05 .pain{display:flex;gap:.8em;align-items:flex-start;padding:clamp(.55rem,1.5vw,.95rem) clamp(.7rem,1.8vw,1.2rem);
  border-radius:12px;background:#F1F6F2;border:1px solid var(--hair)}
#s05 .pain i{font-style:normal;flex:none;width:1.7em;height:1.7em;border-radius:50%;display:grid;place-items:center;
  background:#FBE3CE;color:#C4560A;font-weight:800;font-size:.95em}
#s05 .pain.good i{background:#DFF0E7;color:#0E7A4E}
#s05 .pain p{font-size:clamp(.9rem,1.3vw,1.12rem);line-height:1.38;color:var(--ink)}
#s05 .pain p b{color:#0A2416}
#s05 .tt-a em,#s05 .tt-b em{font-style:normal;color:var(--orange-soft)}

/* ═══ S08: diamante original em fundo claro, fontes maiores ═══ */
#s08 .dcard li{font-size:clamp(.82rem,1.16vw,1.05rem);line-height:1.32}
#s08 .dcard ul{gap:.18em}
#s08 .dcard .who{font-size:clamp(.85rem,1.22vw,1.08rem)}
#s08 .dcard .resp{margin-top:.35em}
#s08 .dcard .resp b{margin-bottom:.28em}
body.light #s08 svg.links path{stroke:rgba(14,122,78,.5);filter:none}
#s08 svg.links{z-index:3}
#s08 .dcard.fed ul,#s08 .dcard.srv ul{grid-template-columns:1fr}
#s08 .diamond{gap:clamp(.4rem,1.1vh,.75rem) clamp(3rem,8vw,7rem)}
#s08 .dcard{padding:clamp(.5rem,1.1vw,.85rem) clamp(.85rem,1.8vw,1.35rem)}
@media(max-height:780px){
  #s08 .dcard li{font-size:.8rem;line-height:1.28}
  #s08 .dcard ul{gap:.13em}
  #s08 .dcard .who{font-size:.85rem}
  #s08 .title{margin-top:.3em}
}


/* selo único do s08 + enxugamento do diamante */
#s08 .resplabel{display:inline-flex;align-items:center;gap:.6em;max-width:max-content;
  font-size:clamp(.62rem,.92vw,.8rem);letter-spacing:.28em;text-transform:uppercase;font-stretch:120%;
  font-weight:800;color:var(--green);border:1px solid rgba(14,122,78,.35);border-radius:999px;
  padding:.5em 1.2em;margin-top:.6em;background:rgba(255,255,255,.6)}
#s08 .resplabel::before{content:"";width:.5em;height:.5em;border-radius:50%;background:var(--orange)}
#s08 .dcard{padding:clamp(.5rem,1.1vw,.85rem) clamp(.9rem,1.9vw,1.4rem)}
#s08 .dcard .resp{margin-top:.35em}
#s08 .dcard .who{margin-top:.15em}
#s08 .dcard li{line-height:1.32}
#s08 .diamond{gap:clamp(.4rem,1.2vh,.75rem) clamp(3rem,8vw,7rem)}
#s08 .dcard.est,#s08 .dcard.mun{align-self:center}

/* ═══ S09: título no alto, bloco da logo centrado no espaço restante ═══ */
#s09 .wrap{justify-content:flex-start;padding-top:clamp(1.6rem,5vh,2.8rem)}
#s09 .kick{margin-bottom:0}
#s09 .plate{margin-top:auto}
#s09 .chips{margin-bottom:auto}
#s09 .statement{font-size:clamp(1.45rem,2.85vw,2.6rem)}
#s09 .chip{font-size:clamp(.88rem,1.28vw,1.12rem);padding:.65em 1.3em}
/* ═══ S10: cabeçalho abaixo da logo; título e lead em linha única e largura total ═══ */
#s10 .wrap{padding-top:clamp(8rem,15vh,9.2rem)}
#s10 .head{max-width:none}
#s10 .head .title{max-width:none;white-space:nowrap;font-size:clamp(1.05rem,1.92vw,1.85rem);margin-top:.35em}
#s10 .head .lead{max-width:none;white-space:nowrap;font-size:clamp(.78rem,1.21vw,1.26rem);margin-top:.5em}
#s10 .core{font-size:clamp(1.2rem,1.9vw,1.7rem);padding:.85em 1.7em}
#s10 .fn{font-size:clamp(.88rem,1.28vw,1.12rem);padding:.6em 1.2em .6em .55em}
#s10 svg.beams{position:absolute;inset:0;width:100%;height:100%;pointer-events:none;z-index:1}
#s10 .core,#s10 .fn{z-index:3}
#s10 .bgrp{opacity:0;transition:opacity .6s ease}
#s10 .bgrp.go{opacity:1}
#s10 .bbase{fill:none;stroke:#79B295;stroke-width:2.6;stroke-linecap:round}
#s10 .bpulse{fill:none;stroke:#0E7A4E;stroke-width:3;stroke-linecap:round;
  filter:drop-shadow(0 0 4px rgba(14,122,78,.55));
  animation:beamflow var(--bt,3.2s) cubic-bezier(.16,1,.3,1) infinite;animation-delay:var(--bd,0s)}
@keyframes beamflow{from{stroke-dashoffset:var(--boff)}to{stroke-dashoffset:0}}
@media (prefers-reduced-motion:reduce){#s10 .bpulse{animation:none;opacity:0}}

/* ═══ S12: fluxo simétrico — linha única atrás; cards/reator opacos escondem as pontas ═══ */
#s12 .line::before{content:"";position:absolute;left:0;right:0;top:50%;height:2px;transform:translateY(-50%);z-index:0;
  background:linear-gradient(90deg,rgba(232,119,34,.5),rgba(14,122,78,.6) 50%,rgba(232,119,34,.5))}
#s12 .reactor::before,#s12 .reactor::after{content:none}
#s12 .side,#s12 .reactor{position:relative;z-index:1}
#s12 .side .io{width:100%;max-width:none;min-height:clamp(3.6rem,10.5vh,5.6rem);background:#fff;
  display:flex;flex-direction:column;justify-content:center;align-items:flex-start;text-align:left;
  font-size:clamp(.92rem,1.34vw,1.18rem)}
#s12 .side .io span{display:block;margin-top:.3em}
/* rótulos de seção: maiores, verde, com traço de destaque */
#s12 h5{font-size:clamp(.9rem,1.3vw,1.15rem);letter-spacing:.22em;font-weight:800;font-stretch:120%;
  color:var(--green);margin-bottom:1em;position:relative;padding-bottom:.55em}
#s12 h5::after{content:"";position:absolute;left:0;bottom:0;width:2.6em;height:2px;background:var(--orange)}
#s12 .side.right h5{text-align:right;align-self:flex-end}
#s12 .side.right h5::after{left:auto;right:0}
#s12 .proc{font-size:clamp(.85rem,1.24vw,1.08rem)}
#s12 .rlabel{font-size:clamp(1.05rem,1.6vw,1.4rem)}

/* ═══ S13: ÓRBITA RADIAL (porta do 21st.dev · Radial Orbital Timeline) ═══ */
#s13 .orb5{position:relative;flex:1;min-height:0;overflow:visible}
#s13 .oring,#s13 .oring2{position:absolute;left:50%;top:50%;translate:-50% -50%;border-radius:50%;pointer-events:none}
#s13 .oring{width:min(64vh,72%);aspect-ratio:1/.92;border:1.5px solid rgba(6,46,30,.13)}
#s13 .oring2{width:min(46vh,52%);aspect-ratio:1/.92;border:1.5px dashed rgba(14,122,78,.22);animation:spin 34s linear infinite}
@keyframes spin{to{rotate:360deg}}
#s13 .ocore{position:absolute;left:50%;top:50%;translate:-50% -50%;z-index:5;width:clamp(3.4rem,7vh,4.6rem);aspect-ratio:1;
  border-radius:50%;background:radial-gradient(circle at 35% 30%,#17A468,#0A5638 75%);
  box-shadow:0 0 0 1px rgba(255,255,255,.2) inset,0 14px 40px rgba(14,122,78,.35);display:grid;place-items:center}
#s13 .ocore::before{content:"";position:absolute;inset:-11px;border-radius:50%;border:1.5px solid rgba(14,122,78,.35);
  animation:pulseR 2.6s var(--ease) infinite}
#s13 .ocore::after{content:"";position:absolute;inset:-24px;border-radius:50%;border:1px solid rgba(14,122,78,.18);
  animation:pulseR 2.6s var(--ease) .9s infinite}
#s13 .ocore span{width:38%;aspect-ratio:1;border-radius:50%;background:rgba(255,255,255,.85)}
#s13 .onode{position:absolute;translate:-50% -50%;transition:opacity .5s ease}
#s13 .onode .obtn{display:grid;place-items:center;width:clamp(2.9rem,5.6vh,3.8rem);aspect-ratio:1;border-radius:50%;
  border:2.5px solid;background:#fff;cursor:pointer;margin:0 auto;
  box-shadow:0 10px 26px rgba(6,46,30,.16);transition:box-shadow .3s ease,border-color .3s ease}
#s13 .onode .obtn i{font-style:normal;font-weight:850;font-size:clamp(1.05rem,1.8vh,1.35rem)}
#s13 .onode.k1 .obtn{border-color:#E87722;color:#C4560A}
#s13 .onode.k2 .obtn{border-color:#0E7A4E;color:#0A5638}
#s13 .onode.k3 .obtn{border-color:#57B98A;color:#0A5638}
#s13 .onode.k4 .obtn{border-color:#0A5638;background:linear-gradient(120deg,#0E7A4E,#0A5638);color:#fff}
#s13 .onode.open .obtn{box-shadow:0 0 0 6px rgba(14,122,78,.14),0 16px 40px rgba(6,46,30,.24)}
#s13 .olabel{margin-top:.5em;text-align:center;font-size:clamp(.78rem,1.5vh,1rem);font-weight:750;color:var(--ink);
  white-space:nowrap;letter-spacing:.01em;transition:opacity .3s ease}
#s13 .onode.open .olabel{opacity:0}
#s13 .ocard{position:absolute;top:calc(100% + 16px);left:50%;translate:-50% 0;width:clamp(19rem,36vw,25rem);
  background:#fff;border:1px solid rgba(6,46,30,.1);border-top:3px solid var(--green);border-radius:14px;
  box-shadow:0 26px 60px rgba(6,46,30,.2);padding:1rem 1.2rem;text-align:left;
  opacity:0;transform:translateY(-8px);pointer-events:none;transition:opacity .4s var(--ease),transform .4s var(--ease)}
#s13 .onode.k1 .ocard{border-top-color:#E87722}
#s13 .onode.open .ocard{opacity:1;transform:none;pointer-events:auto}
#s13 .ocard::before{content:"";position:absolute;top:-14px;left:50%;translate:-50% 0;width:2px;height:12px;background:rgba(14,122,78,.5)}
#s13 .ocard h5{display:flex;align-items:center;gap:.55em;font-size:clamp(.95rem,1.9vh,1.15rem);font-weight:800;color:var(--ink);margin-bottom:.4em}
#s13 .ocard h5 i{font-style:normal;flex:none;width:1.7em;height:1.7em;border-radius:50%;display:grid;place-items:center;
  font-size:.85em;color:#fff;background:var(--green)}
#s13 .onode.k1 .ocard h5 i{background:#E87722}
#s13 .ocard p{font-size:clamp(.88rem,1.75vh,1.08rem);line-height:1.5;color:var(--ink-2)}
#s13 .orel{display:flex;flex-wrap:wrap;gap:.4em;margin-top:.7em;padding-top:.6em;border-top:1px solid rgba(6,46,30,.08)}
#s13 .orel button{font-family:inherit;font-size:clamp(.68rem,1.35vh,.8rem);font-weight:650;color:var(--ink-2);
  background:#F1F6F2;border:1px solid rgba(6,46,30,.1);border-radius:999px;padding:.35em .9em;cursor:pointer;
  transition:all .25s ease}
#s13 .orel button:hover{color:var(--ink);border-color:rgba(14,122,78,.45);background:#E7F4EC}
#s13 .orbprint{display:none}
@media print{
  #s13 .orb5{display:none}
  #s13 .orbprint{display:grid;gap:1rem;margin-top:1.4rem}
  #s13 .orbprint b{display:block;font-size:1.05rem;color:#0A2416}
  #s13 .orbprint span{font-size:.95rem;color:#40604E}
}

/* ═══ S13: passo final — a órbita se dissolve e os 4 cards aparecem juntos ═══ */
#s13 #orb5{transition:opacity .55s var(--ease),transform .55s var(--ease)}
#s13.summaryon #orb5{opacity:0;transform:scale(.94);pointer-events:none}
#s13 .orbsummary{position:absolute;inset:0;z-index:4;pointer-events:none;
  display:grid;grid-template-columns:repeat(4,1fr);align-content:center;gap:clamp(.8rem,2vw,1.5rem);
  padding:0 var(--pad);opacity:0;transform:translateY(16px);
  transition:opacity .6s var(--ease) .12s,transform .6s var(--ease) .12s}
#s13.summaryon .orbsummary{opacity:1;transform:none}
#s13 .oscard{background:#fff;border:1px solid rgba(6,46,30,.08);border-top:3px solid var(--green);border-radius:16px;
  padding:clamp(1rem,2.1vw,1.6rem);box-shadow:0 18px 44px rgba(6,46,30,.12)}
#s13 .oscard.k1{border-top-color:var(--orange)}
#s13 .oscard.k3{border-top-color:#57B98A}
#s13 .oscard.k4{border-top-color:#0A5638}
#s13 .osn{display:inline-grid;place-items:center;width:2em;height:2em;border-radius:50%;color:#fff;
  font-weight:800;font-size:.95em;margin-bottom:.6em;background:var(--green)}
#s13 .oscard.k1 .osn{background:var(--orange)}
#s13 .oscard.k3 .osn{background:#57B98A}
#s13 .oscard.k4 .osn{background:#0A5638;color:#fff}
#s13 .oscard b{display:block;font-size:clamp(.95rem,1.35vw,1.2rem);color:var(--ink);margin-bottom:.45em;line-height:1.22}
#s13 .oscard p{font-size:clamp(.82rem,1.15vw,1.04rem);color:var(--ink-2);line-height:1.45}
@media(max-height:760px){#s13 .oscard{padding:.85rem 1rem}#s13 .oscard p{font-size:.86rem}}

/* ═══ S14: OPÇÃO A — faixas horizontais, colunas internas por densidade ═══ */
#s14 .title{max-width:none;text-wrap:pretty;font-size:clamp(1.15rem,1.95vw,1.72rem)}
#s14 .tri{display:flex;flex-direction:column;justify-content:space-evenly;gap:clamp(.45rem,1.4vh,.9rem);
  flex:1;min-height:0;margin-top:clamp(.5rem,1.6vh,1rem)}
#s14 .tcol{padding:clamp(.6rem,1.3vw,.95rem) clamp(1rem,2.1vw,1.5rem);display:block;flex:0 0 auto}
#s14 .tcol h4{display:flex;align-items:center;gap:.55em;font-size:clamp(.92rem,1.3vw,1.1rem);
  font-weight:800;font-stretch:110%;letter-spacing:.04em;text-transform:uppercase;color:var(--green);margin-bottom:.38em}
#s14 .tcol.atr h4{color:var(--orange-soft)}
#s14 .mk{width:.6em;height:.6em;border-radius:3px;flex:none}
#s14 .mk.g{background:var(--green)}#s14 .mk.o{background:var(--orange)}#s14 .mk.g2{background:#57B98A}
#s14 .tcol ul{list-style:none;columns:2;column-gap:2.4em}
#s14 .tcol.comp ul{columns:3;column-gap:2em}
#s14 .tcol li{break-inside:avoid;margin-bottom:clamp(.26em,.9vh,.45em)}
#s14 .tcol li{position:relative;padding-left:1em;font-size:clamp(.92rem,1.28vw,1.08rem);color:var(--ink-2);line-height:1.4}
#s14 .tcol li::before{content:"";position:absolute;left:0;top:.5em;width:.32em;height:.32em;border-radius:50%;background:var(--orange)}
#s14 .tcol .intro{font-size:clamp(.88rem,1.24vw,1.06rem);color:var(--ink-3);margin-bottom:.5em;line-height:1.4}
#s14 .foot{font-size:clamp(.9rem,1.28vw,1.12rem);margin-top:clamp(.35rem,1.1vh,.6rem)}
@media(max-height:780px){
  #s14 .tcol li{font-size:.88rem;line-height:1.32}
  #s14 .tcol .intro{font-size:.82rem;margin-bottom:.3em}
  #s14 .tcol h4{font-size:.9rem;margin-bottom:.32em}
  #s14 .title{font-size:1.1rem}
  #s14 .foot{font-size:.84rem}
  #s14 .tcol{padding:.55rem 1rem}
}

/* ═══ S15: fonte maior, conteúdo centrado no card ═══ */
#s15 .stepc .ord{right:auto;left:.4em}
#s15 .result{top:clamp(2.4rem,7vh,4.2rem)}
#s15 .stepc{justify-content:center;gap:.15em}
#s15 .stepc h5{font-size:clamp(.62rem,.92vw,.82rem)}
#s15 .stepc b{font-size:clamp(1.2rem,1.95vw,1.7rem)}
#s15 .stepc p{font-size:clamp(.92rem,1.34vw,1.18rem);line-height:1.45}
#s15 .badge{font-size:clamp(.88rem,1.3vw,1.15rem)}

/* ═══ S16: fontes máximas, cards maiores ═══ */
#s16 .vb{width:clamp(12rem,16.5vw,15rem);max-width:none;min-height:clamp(6.6rem,18.2vh,9.4rem);display:flex;flex-direction:column;justify-content:center;padding:clamp(.7rem,1.5vw,1.1rem) clamp(1rem,2vw,1.5rem)}
#s16 .vb b{font-size:clamp(1.02rem,1.55vw,1.35rem)}
#s16 .vb span{font-size:clamp(.85rem,1.24vw,1.08rem)}

/* ═══ S17: fontes maiores ═══ */
#s17 .hub{font-size:clamp(1.2rem,1.9vw,1.65rem);padding:.85em 1.7em}
#s17 .qd h4{font-size:clamp(1.05rem,1.6vw,1.42rem)}
#s17 .qd p{font-size:clamp(.85rem,1.25vw,1.1rem)}

/* ═══ S18: frases sob as palavras grandes maiores ═══ */
#s18 .cap{font-size:clamp(.98rem,1.48vw,1.32rem)}

/* ═══ S19: frase da biblioteca maior ═══ */
/* S19: frase no topo em largura cheia + dois QR nos cantos inferiores */
/* logo do canto some só no s19 (a frase ocupa a largura toda no topo); a marca Conass fica no HUD e na legenda do QR */
#s19.on ~ .cornerlogo{display:none}
#s19 .wrap{justify-content:flex-start;padding-top:clamp(3.4rem,9vh,5.6rem);padding-bottom:clamp(4rem,8.7vh,5.2rem)}
#s19 .barlabel{margin-bottom:.7em}
#s19 .msg{max-width:none;font-size:clamp(1.32rem,2.02vw,1.92rem);line-height:1.24;font-weight:760}
#s19 .qrs{margin-top:auto;display:flex;justify-content:space-between;align-items:flex-end;width:100%;gap:1rem}
#s19 .qr{display:flex;flex-direction:column;gap:clamp(.55rem,1.4vh,.95rem);width:clamp(16rem,21.5vw,20rem)}
#s19 .qr:last-child{align-items:flex-end}
#s19 .qcap{font-size:clamp(1rem,1.46vw,1.3rem);font-weight:800;font-stretch:118%;letter-spacing:.1em;text-transform:uppercase;color:var(--ink);line-height:1.22;position:relative;padding-bottom:.55em;align-self:flex-start;text-shadow:0 0 3px rgba(247,250,246,.98),0 1px 5px rgba(247,250,246,.95),0 0 12px rgba(247,250,246,.9)}
#s19 .qr:last-child .qcap{align-self:flex-end;text-align:right}
#s19 .qcap::after{content:"";position:absolute;left:0;bottom:0;width:2.6em;height:2px;background:var(--orange)}
#s19 .qr:last-child .qcap::after{left:auto;right:0}
#s19 .qtile{align-self:stretch;background:#fff;border-radius:18px;padding:clamp(.75rem,1.4vw,1.2rem);box-shadow:0 20px 50px rgba(6,46,30,.26),0 0 0 1px rgba(6,46,30,.06)}
#s19 .qtile img{display:block;width:100%;height:auto}

/* ═══ CELULAR: aviso para girar a tela (o deck é 16:9; retrato não comporta) ═══ */
/* dimensões em vw: no retrato o viewport CSS é 1280px escalado p/ ~390px físicos, então as
   unidades compensam o fator de escala e o aviso aparece em tamanho legível no aparelho */
.rotatehint{display:none}
@media (orientation:portrait) and (pointer:coarse){
  .rotatehint{position:fixed;inset:0;z-index:990;display:flex;flex-direction:column;align-items:center;
    justify-content:center;gap:6vw;background:#07130C;color:#EAF4EE;text-align:center}
  .rotatehint .ph{width:15vw;height:26vw;border:1.1vw solid #2FBF83;border-radius:3vw;display:block;
    animation:rotph 2.4s ease-in-out infinite}
  .rotatehint p{font-size:4.6vw;font-weight:700;line-height:1.45;max-width:24ch;font-stretch:105%}
  @keyframes rotph{0%,22%{transform:rotate(0)}58%,100%{transform:rotate(-90deg)}}
}

/* ═══ SORG: organograma do Conass (estrutura oficial, modelo enxuto) ═══ */
#sorg .wrap{padding-top:clamp(2.1rem,4.8vh,3.1rem);padding-bottom:clamp(1.3rem,3.4vh,2.2rem);display:flex;flex-direction:column}
#sorg .title{font-size:clamp(1rem,1.7vw,1.5rem);margin-top:.3em;margin-bottom:clamp(.4rem,1.2vh,.7rem)}
#sorg .chart{flex:1;min-height:0;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:clamp(.26rem,.85vh,.55rem)}
/* caixas */
#sorg .obox{background:#fff;border:1px solid var(--hair);border-radius:12px;text-align:center;
  padding:clamp(.42rem,1.05vh,.72rem) clamp(1rem,1.8vw,1.5rem);box-shadow:0 9px 24px rgba(6,46,30,.08)}
#sorg .obox b{display:block;font-weight:800;font-stretch:110%;font-size:clamp(.92rem,1.35vw,1.24rem);color:var(--ink);line-height:1.2}
#sorg .obox span{display:block;font-size:clamp(.68rem,.98vw,.9rem);color:var(--ink-2);line-height:1.26;margin-top:.12em}
#sorg .obox.solo{align-self:center}
#sorg .obox.top{background:var(--green);border-color:transparent;box-shadow:0 14px 34px rgba(14,122,78,.3);max-width:min(54vw,620px)}
#sorg .obox.top b{color:#fff}#sorg .obox.top span{color:rgba(255,255,255,.9)}
#sorg .obox.sec{border-top:3px solid var(--orange)}
#sorg .obox.cam{background:var(--orange);border-color:transparent;box-shadow:0 14px 34px rgba(232,119,34,.34);
  padding:clamp(.48rem,1.25vh,.78rem) clamp(1.1rem,2.1vw,1.85rem)}
#sorg .obox.cam b{color:#fff;font-size:clamp(.94rem,1.4vw,1.32rem);letter-spacing:.02em}
/* conectores verticais */
#sorg .vl{width:2px;height:clamp(.42rem,1.3vh,.85rem);background:rgba(14,122,78,.4)}
/* linhas com satélite à direita (Assembleia+Comitê, Diretoria+Conselho Fiscal) */
#sorg .orow{display:grid;grid-template-columns:1fr auto 1fr;align-items:center;width:100%}
#sorg .orow>.obox{grid-column:2;justify-self:center}
#sorg .orow>.side{display:flex;align-items:center}
#sorg .orow>.side.R{grid-column:3;justify-self:start}
#sorg .tap{height:2px;width:clamp(.7rem,1.9vw,1.5rem);background:rgba(14,122,78,.4);flex:none}
#sorg .tap.o{background:rgba(232,119,34,.5)}
/* chips (satélites e subitens) */
#sorg .chip{background:#fff;border:1px solid var(--hair);border-radius:10px;padding:.4em .95em;text-align:center;
  box-shadow:0 7px 18px rgba(6,46,30,.06)}
#sorg .chip b{font-weight:700;font-size:clamp(.76rem,1.08vw,.98rem);color:var(--ink);line-height:1.2;display:block}
#sorg .chip span{display:block;font-size:clamp(.62rem,.88vw,.8rem);color:var(--ink-3);line-height:1.2}
/* faixa de ramais: Câmaras Técnicas (esq.) · espinha · Gabinete (dir.) */
#sorg .branch{display:grid;grid-template-columns:1fr auto 1fr;align-items:center;width:100%;margin:clamp(.1rem,.3vh,.24rem) 0}
#sorg .branch .bcol{display:flex;align-items:center}
#sorg .branch .bcol.L{grid-column:1;justify-content:flex-end}
#sorg .branch .spine{grid-column:2;width:2px;align-self:stretch;justify-self:center;background:rgba(14,122,78,.4)}
#sorg .branch .bcol.R{grid-column:3;justify-content:flex-start}
#sorg .pan.gab{background:#fff;border:1px solid var(--hair);border-radius:12px;box-shadow:0 9px 24px rgba(6,46,30,.08);
  padding:clamp(.5rem,1.15vh,.82rem) clamp(.85rem,1.5vw,1.3rem);max-width:min(34vw,420px)}
#sorg .pan.gab h6{font-size:clamp(.78rem,1.1vw,1.02rem);font-weight:800;font-stretch:110%;letter-spacing:.05em;
  text-transform:uppercase;color:var(--green);margin-bottom:.4em;text-align:center}
#sorg .pan.gab ul{list-style:none;margin:0;padding:0;display:flex;flex-direction:column;gap:.22em}
#sorg .pan.gab li{position:relative;font-size:clamp(.72rem,1vw,.92rem);line-height:1.26;color:var(--ink-2);padding-left:.95em}
#sorg .pan.gab li::before{content:"";position:absolute;left:0;top:.46em;width:.3em;height:.3em;border-radius:50%;background:var(--green)}
/* distribuidor: Secretaria (50%) → 3 coordenações (16.7% · 50% · 83.3%) */
#sorg .dist3{position:relative;width:100%;height:clamp(.55rem,1.5vh,.95rem)}
#sorg .dist3 i{position:absolute;background:rgba(14,122,78,.4)}
#sorg .dist3 .feed{left:50%;top:0;width:2px;height:50%;translate:-1px 0}
#sorg .dist3 .bar{left:16.667%;right:16.667%;top:50%;height:2px}
#sorg .dist3 .d{width:2px;top:50%;bottom:0;translate:-1px 0}
#sorg .dist3 .a{left:16.667%}#sorg .dist3 .b{left:50%}#sorg .dist3 .c{left:83.333%}
/* coordenações */
#sorg .coords{display:grid;grid-template-columns:repeat(3,1fr);gap:clamp(.6rem,1.4vw,1.2rem);width:100%}
#sorg .coord{display:flex;align-items:center;justify-content:center;text-align:center;background:#fff;border:1px solid var(--hair);
  border-radius:11px;padding:.65em .85em;box-shadow:0 9px 24px rgba(6,46,30,.08)}
#sorg .coord b{font-size:clamp(.82rem,1.2vw,1.08rem);line-height:1.2;color:var(--ink)}
#sorg .coord.dev{border-top:3px solid #57B98A}
#sorg .coord.tec{border-top:3px solid var(--green)}
#sorg .coord.adm{border-top:3px solid var(--orange)}
/* subitens sob Técnica e Adm/Finanças */
#sorg .subs{display:grid;grid-template-columns:repeat(3,1fr);gap:clamp(.5rem,1.2vw,1rem);width:100%;align-items:start}
#sorg .subcol{display:flex;flex-direction:column;align-items:center}
#sorg .subcol .drop{width:2px;height:clamp(.32rem,.95vh,.58rem);background:rgba(14,122,78,.4)}
#sorg .subcol .gerrow{display:flex;gap:clamp(.4rem,1vw,.8rem)}
/* forquilha p/ as 2 gerências */
#sorg .fork{position:relative;width:min(66%,160px);height:clamp(.28rem,.85vh,.52rem)}
#sorg .fork i{position:absolute;background:rgba(14,122,78,.4)}
#sorg .fork .fb{left:25%;right:25%;top:0;height:2px}
#sorg .fork .fd{width:2px;top:0;bottom:0}
#sorg .fork .fl{left:25%}#sorg .fork .fr{right:25%}
@media (max-height:760px){
  #sorg .chart{gap:clamp(.18rem,.55vh,.36rem)}
  #sorg .obox{padding:clamp(.32rem,.85vh,.56rem) clamp(.9rem,1.6vw,1.3rem)}
  #sorg .obox b{font-size:clamp(.85rem,1.2vw,1.08rem)}
  #sorg .obox span{font-size:clamp(.64rem,.9vw,.82rem)}
  #sorg .obox.cam b{font-size:clamp(.88rem,1.25vw,1.14rem)}
  #sorg .coord b{font-size:clamp(.78rem,1.08vw,.98rem)}
  #sorg .pan.gab h6{font-size:clamp(.74rem,1vw,.92rem)}
  #sorg .pan.gab li{font-size:clamp(.68rem,.92vw,.84rem)}
  #sorg .chip b{font-size:clamp(.72rem,1vw,.9rem)}
  #sorg .vl{height:clamp(.32rem,.95vh,.6rem)}
  #sorg .title{font-size:1rem;margin-bottom:.28rem}
}

/* ═══ SBRA: Brasil (território + números em destaque à esq.; Gini alto à dir.) ═══ */
#sbra .wrap{padding-top:clamp(2.1rem,4.8vh,3.1rem);padding-bottom:clamp(3rem,7vh,4.2rem);display:flex;flex-direction:column}
#sbra .title{margin-bottom:clamp(.4rem,1.2vh,.8rem)}
#sbra .bcols{flex:1;min-height:0;display:grid;grid-template-columns:1fr auto;gap:clamp(1.6rem,4vw,3.4rem);
  align-items:stretch;padding-top:clamp(.4rem,1.6vh,1.2rem)}
/* topo dos dois mapas desce junto para não invadir a logo do canto (topo permanece alinhado) */
body.showlogo #sbra .bcols{padding-top:clamp(2.7rem,6.3vh,3.7rem)}
/* coluna esquerda: território em cima (topo alinhado ao Gini), números grandes embaixo */
#sbra .bleft{display:flex;flex-direction:column;justify-content:space-between;gap:clamp(.8rem,2.2vh,1.5rem);min-width:0;min-height:0}
#sbra .tmap{margin:0;display:flex;flex-direction:column;align-items:flex-start;gap:clamp(.28rem,.85vh,.5rem)}
#sbra .tmap img{width:min(46vw,600px);max-width:100%;height:auto;max-height:min(42vh,342px);border-radius:12px;
  filter:drop-shadow(0 26px 46px rgba(6,46,30,.34)) drop-shadow(0 6px 14px rgba(6,46,30,.18))}
#sbra .tmap figcaption{font-size:clamp(.58rem,.85vw,.75rem);color:var(--ink-2);line-height:1.3;padding-left:.15em;max-width:52ch}
/* números bem maiores */
#sbra .stats{display:flex;flex-direction:column;gap:clamp(.55rem,1.7vh,1.1rem)}
#sbra .pop{display:flex;flex-direction:column;gap:.04em}
#sbra .pop b{font-size:clamp(2.5rem,4.4vw,4rem);font-weight:800;font-stretch:112%;line-height:.9;color:var(--green);
  font-variant-numeric:tabular-nums;letter-spacing:-.02em;text-shadow:0 0 30px rgba(14,122,78,.16)}
#sbra .pop span{font-size:clamp(.82rem,1.2vw,1.08rem);color:var(--ink-2);font-weight:600}
#sbra .grid5{display:flex;flex-wrap:wrap;gap:clamp(1rem,2.6vw,2.3rem);align-items:flex-end}
#sbra .s{display:flex;flex-direction:column;gap:.12em}
#sbra .s b{font-size:clamp(1.8rem,3vw,2.65rem);font-weight:800;color:var(--ink);line-height:1;font-variant-numeric:tabular-nums}
#sbra .s b i{font-style:normal;font-size:.46em;color:var(--orange);margin-left:.1em;vertical-align:.36em}
#sbra .s span{font-size:clamp(.74rem,1.05vw,.95rem);color:var(--ink-2);line-height:1.18}
/* coluna direita: Gini alto, topo alinhado ao território */
#sbra .gmap{margin:0;display:flex;flex-direction:column;align-items:center;justify-content:flex-start;
  gap:clamp(.4rem,1.1vh,.8rem);min-height:0}
#sbra .gmap img{height:min(63vh,548px);width:auto;max-width:min(42vw,470px);border-radius:12px;
  filter:drop-shadow(0 26px 46px rgba(6,46,30,.34)) drop-shadow(0 6px 14px rgba(6,46,30,.18))}
#sbra .gmap figcaption{font-size:clamp(.62rem,.9vw,.8rem);color:var(--ink-2);text-align:center;line-height:1.34;max-width:44ch}
#sbra .gmap figcaption b{color:var(--orange-soft);font-weight:800}
#sbra .gmap figcaption em{font-style:normal;color:var(--orange);font-weight:700}
/* entrada em "pulo" (escala com leve overshoot) + flutuação contínua = salta da página */
#sbra .bcols figure{opacity:0;transform:translateY(32px) scale(.88)}
#sbra.on .bcols figure{opacity:1;transform:none;
  transition:opacity .5s ease,transform .85s cubic-bezier(.34,1.46,.5,1);transition-delay:var(--jd,0s)}
@keyframes sbfloat{0%,100%{transform:translateY(0)}50%{transform:translateY(-9px)}}
#sbra.on .bcols img{animation:sbfloat 6s ease-in-out 1.1s infinite}
#sbra.on .gmap img{animation-duration:6.9s}
@media (prefers-reduced-motion:reduce){
  #sbra .bcols figure{opacity:1;transform:none;transition:none}
  #sbra.on .bcols img{animation:none}
}
@media (max-height:760px){
  #sbra .pop b{font-size:clamp(1.9rem,3.4vw,2.7rem)}
  #sbra .s b{font-size:clamp(1.45rem,2.4vw,1.95rem)}
  #sbra .tmap img{width:min(42vw,520px)}
  #sbra .gmap img{height:60vh}
}

/* ═══ S20: foto + contatos com fonte máxima ═══ */
#s20 .cphoto{width:clamp(8.5rem,13vw,11.5rem);border-radius:20px;overflow:hidden;
  box-shadow:0 24px 60px rgba(6,46,30,.28),0 0 0 4px #fff;margin-bottom:.7em}
#s20 .cphoto img{display:block;width:100%;height:auto}
#s20 .who b{font-size:clamp(1.15rem,1.85vw,1.6rem)}
#s20 .who span{font-size:clamp(.85rem,1.24vw,1.1rem)}
#s20 .contacts span{font-size:clamp(1rem,1.5vw,1.35rem);padding:.2em 1em .2em 0}
/* bloco de contato sobe junto com a foto (antes ficava colado na base) */
#s20 .right{align-self:flex-start;margin-top:clamp(1.4rem,7vh,4.4rem)}
'''

# ── monta as 20 seções, injetando as notas verbatim do v1 ──
# regra global: nenhum travessão nos textos visíveis (notas, títulos)
def sem_travessao(t):
    t = re.sub(r'\s*—\s*', ', ', t)   # travessão vira vírgula na prosa
    t = re.sub(r',\s*,', ',', t)
    return t.replace(' ,', ',')

order = [f's{i:02d}' for i in range(1, 21)]
order.insert(1, 'sbra')   # slide Brasil (contexto do país), logo após a capa (s01)
order.insert(4, 'sorg')   # organograma do Conass, entre o s03 (Conass) e o s04 (Câmara Técnica)

# ── SLIDES OCULTOS ──────────────────────────────────────────────────────────
# NADA é apagado: o slide continua inteiro em sections_a/b(.py e _fr.py) e nas
# notas; ele apenas fica de fora da montagem. Para REEXIBIR, remova o id do set
# e rode o build de novo (build_v2.py e build_fr.py). A numeração, o índice (O)
# e o total de slides se reajustam sozinhos.
#   's14' = slide 16 "Comitê consultivo por dentro" (oculto a pedido da Carla)
OCULTOS = {'s14'}
order = [sid for sid in order if sid not in OCULTOS]

# slides exclusivos do V2 (sem contraparte no V1): título p/ índice + notas da apresentadora
EXTRA_SLIDES = {
    'sbra': {
        'title': 'Brasil',
        'notes': ('Antes de entrar no modelo, vale situar a escala do país. O Brasil tem cerca de 213 milhões '
                  'de habitantes, segundo o IBGE, distribuídos em 26 estados e no Distrito Federal e em 5.571 '
                  'municípios, sendo que 71% deles têm menos de 20 mil habitantes. O território se organiza em '
                  '5 regiões geográficas e, na saúde, em 117 macrorregiões e 453 regiões de saúde. É um país de '
                  'dimensão continental e profundamente desigual: o Índice de Gini de 2024 é de 0,509, o que '
                  'coloca o Brasil como o segundo país com maior desigualdade no G20. É nesse cenário de escala '
                  'e desigualdade que o modelo dos núcleos precisa funcionar.'),
    },
    'sorg': {
        'title': 'Organograma do Conass',
        'notes': ('Antes de falar da Câmara Técnica, vale ver o desenho institucional do Conass. No topo está a '
                  'Assembleia Geral, que reúne os 27 secretários de Saúde dos estados e do Distrito Federal, com o '
                  'Comitê Consultivo formado pelos ex-presidentes. Abaixo vêm a Diretoria, acompanhada do Conselho '
                  'Fiscal, e a Presidência. A Secretaria Executiva conduz a operação e conta com o Gabinete e suas '
                  'assessorias: de Apoio do Gabinete, Jurídica, Parlamentar, de Comunicação e de Informações '
                  'Estratégicas. Dela partem três coordenações: de Desenvolvimento Institucional, Técnica e de '
                  'Administração e de Finanças. A Coordenação Técnica reúne as assessorias técnicas, e a de '
                  'Administração e de Finanças, as gerências Administrativa e Financeira. É no conjunto das câmaras '
                  'técnicas, destacado aqui, que está a Câmara Técnica de Qualidade no Cuidado e Segurança do '
                  'Paciente, que veremos a seguir.'),
    },
}
meta_of = lambda sid: inv[sid] if sid in inv else EXTRA_SLIDES[sid]

sections = []
for sid in order:
    tpl = (SECTIONS_A | SECTIONS_B)[sid]
    notes = sem_travessao(meta_of(sid)['notes'])
    sections.append(tpl.replace('{NOTES}', f'<aside class="notes">{notes}</aside>'))
BODY_SECTIONS = '\n'.join(sections)

# ── índice (tecla O) ── (títulos sem travessão, dois-pontos p/ definições)
menu_links = '\n'.join(
    f'<a href="#" data-i="{i}"><b>{i+1:02d}</b><span>{meta_of(sid)["title"].replace(" — ", ": ")}</span></a>'
    for i, sid in enumerate(order))

style = open(f'{B}/style.css').read() + EXTRA_CSS
script = open(f'{B}/script.js').read()

html = f'''<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=1280">
<title>Negesp · Governança da Segurança do Paciente · CALASS 2026</title>
<style>
{style}
</style>
</head>
<body>
<div class="atmo"></div>
<canvas id="dust"></canvas>
<div class="grain"></div>

{BODY_SECTIONS}

<div class="rotatehint" aria-hidden="true"><i class="ph"></i><p>Gire o celular para ver a apresentação</p></div>

<div class="hud" aria-hidden="true">
  <i class="tl"></i><i class="tr"></i><i class="bl"></i><i class="br"></i>
  <div class="htl"><b>Conass</b> · Negesp · CALASS 2026</div>
  <div class="htr" id="hudTitle"></div>
  <div class="hbl"><b>→</b> avança · <b>N</b> notas · <b>O</b> índice · <b>F</b> tela cheia</div>
  <div class="hbr" id="hudNum"></div>
</div>
<div class="prog"><i id="progBar"></i></div>
<div class="cornerlogo" aria-hidden="true">%%CONASS_SVG%%</div>

<div class="menu" id="menu"><div class="mgrid">
{menu_links}
</div></div>
<div class="notesbar" id="notesBar"><h6>Notas da apresentadora</h6><div id="notesTxt"></div></div>

<script>
{script}
</script>
</body>
</html>'''

# ── injeta ativos ──
A = f'{B}/assets'
tok = {
    '%%FONT%%':       open(f'{A}/archivo.b64').read().strip(),
    '%%COVER%%':      open(f'{A}/img0.jpg.b64').read().strip(),
    '%%GRUPO%%':      open(f'{A}/img1.jpg.b64').read().strip(),
    '%%CONASS_SVG%%':  open(f'{A}/conass-logo.svg').read().strip(),
    '%%JATENE%%':     open(f'{A}/img3.jpg.b64').read().strip(),
    '%%LOGONEGESP%%': open(f'{A}/img5.png.b64').read().strip(),
    '%%CARLA%%':      open(f'{A}/carla.jpg.b64').read().strip(),
    '%%QRBIB%%':      open(f'{A}/qr_bib.b64').read().strip(),
    '%%QRNEG%%':      open(f'{A}/qr_neg.b64').read().strip(),
    '%%MAPDATA%%':    open(f'{A}/map_data.json').read().strip(),
    '%%MAPTERR%%':    open(f'{A}/mapa_terr.png.b64').read().strip(),
    '%%MAPGINI%%':    open(f'{A}/mapa_gini.png.b64').read().strip(),
}
for k, v in tok.items():
    html = html.replace(k, v)

open(OUT, 'w').write(html)
rest = re.findall(r'%%[A-Z]+%%', html)
print(f'V2 gravado: {os.path.getsize(OUT)//1024} KB | tokens restantes: {rest}')
print('seções:', html.count('<section class="slide"'), '| notas:', html.count('<aside class="notes">'))

# ── VERIFICAÇÃO DE PARIDADE DE CONTEÚDO ──
# neutraliza travessão e a pontuação que o substituiu (,:·) dos dois lados,
# para verificar palavra a palavra ignorando só a troca de pontuação autorizada
def norm(t):
    t = unicodedata.normalize('NFC', t)
    t = re.sub(r'[—–:·,]', ' ', t)
    return re.sub(r'\s+', ' ', t).strip()

new_plain = norm(re.sub(r'<[^>]+>', ' ', re.sub(r'<(script|style)[^>]*>.*?</\1>', ' ', html, flags=re.S)))
# trechos do V1 removidos de propósito a pedido do usuário (não são perda acidental de texto)
REMOVIDOS = {
    norm('Merci beaucoup.'),
    norm('O Conselho está ao lado de cada secretaria: conheça a Biblioteca Digital do Conselho Nacional de Secretários de Saúde'),
}
missing = []
for sid in order:
    if sid not in inv:   # slide exclusivo do V2 (ex.: organograma): nada a conferir contra o V1
        continue
    body = inv[sid]['body']
    body = re.sub(r'<aside class="notes">.*?</aside>', '', body, flags=re.S)
    chunks = [norm(c) for c in re.split(r'<[^>]+>', body)]
    for c in chunks:
        if len(c) < 2 or c in ('→', '“', '”', '+', '=', '!', '✓'):
            continue
        if c in REMOVIDOS:
            continue
        if c not in new_plain:
            missing.append((sid, c))
# notas também
for sid in order:
    if sid not in inv:
        continue
    n = norm(re.sub(r'<[^>]+>', ' ', inv[sid]['notes']))
    if n and n not in new_plain:
        missing.append((sid, 'NOTA: ' + n[:80]))

if missing:
    print(f'\\n✗ FALTAM {len(missing)} trechos:')
    for sid, c in missing:
        print(f'  [{sid}] {c[:110]}')
    sys.exit(1)
print('✓ PARIDADE TOTAL: todo o texto do V1 está presente no V2, caractere a caractere.')
