# -*- coding: utf-8 -*-
"""Monta a versão FRANCÊS (fr-FR internacional) do modelo V2.

Reaproveita CSS/JS/estrutura/ativos do build_v2 SEM duplicar: importa build_v2 (que
reconstrói o PT como efeito colateral, mantendo os dois em sincronia) e troca apenas:
  - as seções (textos em francês: sections_a_fr / sections_b_fr)
  - os textos de interface (HUD, aviso de girar, barra de notas) para francês
  - o idioma (<html lang="fr">) e o <title>
  - o arquivo de saída (../v2-fr/index.html)

NOTAS DA APRESENTADORA: ficam em PORTUGUÊS de propósito (são privadas, só a apresentadora
vê com a tecla N; servem de apoio para a Carla, brasileira). Para gerar em francês, trocar
`pt.meta_of(sid)['notes']` por um dicionário de notas em francês.
"""
import os, re
import build_v2 as pt   # roda o build PT e expõe EXTRA_CSS, order, sem_travessao, meta_of, B
from sections_a_fr import SECTIONS_A_FR
from sections_b_fr import SECTIONS_B_FR

B = pt.B
A = f'{B}/assets'
OUT = os.path.join(B, '..', 'v2-fr', 'index.html')
os.makedirs(os.path.dirname(OUT), exist_ok=True)

SECTIONS_FR = SECTIONS_A_FR | SECTIONS_B_FR

# ── monta as seções (notas em PT, reaproveitadas do v1/EXTRA) ──
sections = []
for sid in pt.order:
    tpl = SECTIONS_FR[sid]
    notes = pt.sem_travessao(pt.meta_of(sid)['notes'])   # PT: apoio à apresentadora
    sections.append(tpl.replace('{NOTES}', f'<aside class="notes">{notes}</aside>'))
BODY_SECTIONS = '\n'.join(sections)

# ── índice (tecla O): título = data-title (francês) de cada seção ──
def data_title(tpl):
    m = re.search(r'data-title="([^"]*)"', tpl)
    return m.group(1) if m else ''
menu_links = '\n'.join(
    f'<a href="#" data-i="{i}"><b>{i+1:02d}</b><span>{data_title(SECTIONS_FR[sid])}</span></a>'
    for i, sid in enumerate(pt.order))

style = open(f'{B}/style.css').read() + pt.EXTRA_CSS
script = open(f'{B}/script.js').read()

html = f'''<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=1280">
<title>Negesp · Gouvernance de la sécurité des patients · CALASS 2026</title>
<style>
{style}
</style>
</head>
<body>
<div class="atmo"></div>
<canvas id="dust"></canvas>
<div class="grain"></div>

{BODY_SECTIONS}

<div class="rotatehint" aria-hidden="true"><i class="ph"></i><p>Tournez votre téléphone pour voir la présentation</p></div>

<div class="hud" aria-hidden="true">
  <i class="tl"></i><i class="tr"></i><i class="bl"></i><i class="br"></i>
  <div class="htl"><b>Conass</b> · Negesp · CALASS 2026</div>
  <div class="htr" id="hudTitle"></div>
  <div class="hbl"><b>&rarr;</b> avancer · <b>N</b> notes · <b>O</b> index · <b>F</b> plein &eacute;cran</div>
  <div class="hbr" id="hudNum"></div>
</div>
<div class="prog"><i id="progBar"></i></div>
<div class="cornerlogo" aria-hidden="true">%%CONASS_SVG%%</div>

<div class="menu" id="menu"><div class="mgrid">
{menu_links}
</div></div>
<div class="notesbar" id="notesBar"><h6>Notes de la pr&eacute;sentatrice</h6><div id="notesTxt"></div></div>

<script>
{script}
</script>
</body>
</html>'''

# ── injeta ativos (os MESMOS do PT) ──
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
    '%%MAPTERRFR%%':  open(f'{A}/mapa_terr_fr.svg.b64').read().strip(),
    '%%MAPGINIFR%%':  open(f'{A}/mapa_gini_fr.svg.b64').read().strip(),
}
for k, v in tok.items():
    html = html.replace(k, v)

open(OUT, 'w').write(html)
rest = re.findall(r'%%[A-Z]+%%', html)
print(f'FR gravado: {os.path.getsize(OUT)//1024} KB | tokens restantes: {rest}')
print('seções:', html.count('<section class="slide"'), '| notas:', html.count('<aside class="notes">'))
