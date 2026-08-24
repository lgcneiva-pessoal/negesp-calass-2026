# -*- coding: utf-8 -*-
"""Renderiza os 22 slides do deck HTML e monta PDF + PPTX fiéis ao que está no ar.

Uso (com o repo servido em http://localhost:8791):
    python3 source/render_deck.py "http://localhost:8791/v2/index.html"    ~/Downloads/Negesp-CALASS-2026-PT
    python3 source/render_deck.py "http://localhost:8791/v2-fr/index.html" ~/Downloads/Negesp-CALASS-2026-FR

Requer: playwright (+chromium), Pillow, python-pptx.
Ver HANDOFF.md secao 11 para os detalhes das esperas por slide.
"""
import sys, os, io, time
from playwright.sync_api import sync_playwright
from PIL import Image
from pptx import Presentation
from pptx.util import Inches

URL      = sys.argv[1]           # ex.: http://localhost:8791/v2/index.html
OUTBASE  = sys.argv[2]           # ex.: /Users/LG/Downloads/Negesp-CALASS-2026-PT
N        = 22
W, H     = 1280, 720             # 16:9
SCALE    = 2                     # 2560x1440
TMP      = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'frames_' + os.path.basename(OUTBASE))
os.makedirs(TMP, exist_ok=True)

# esconde só a dica de teclado (não faz sentido em PDF/PPTX); mantém logo e numeração
HIDE_CSS = ".hud .hbl{display:none!important}"

frames = []
with sync_playwright() as p:
    br = p.chromium.launch(args=['--force-color-profile=srgb','--font-render-hinting=none'])
    pg = br.new_page(viewport={'width': W, 'height': H}, device_scale_factor=SCALE)
    pg.goto(URL, wait_until='networkidle')
    pg.add_style_tag(content=HIDE_CSS)
    pg.wait_for_timeout(1500)                     # fontes embutidas + primeiro layout

    for i in range(N):
        pg.evaluate("i => window.goTo(i, true)", i)
        pg.wait_for_timeout(300)
        sid = pg.evaluate("() => (document.querySelector('.slide.on')||{}).id")

        # slides com cenas que se desenham/animam: dar tempo extra
        if sid in ('s11', 's16'):                 # mapas (traçado + arcos)
            pg.wait_for_timeout(4200)
        elif sid == 's13':                        # órbita: força o resumo dos 4 cards
            pg.evaluate("() => window.__s13step && window.__s13step(5)")
            pg.wait_for_timeout(1400)
        elif sid in ('s08', 's10', 's14', 's15', 's17', 's12'):   # conectores svg
            pg.wait_for_timeout(1800)
        elif sid == 'sbra':                       # mapas com 'pulo' + flutuação
            pg.wait_for_timeout(2200)
        else:
            pg.wait_for_timeout(1200)

        f = os.path.join(TMP, f'slide-{i+1:02d}.png')
        pg.screenshot(path=f)
        frames.append(f)
        print(f'  slide {i+1:02d}/{N} ({sid})', flush=True)
    br.close()

# ── PDF (uma página por slide, 13.333 x 7.5 in) ──
imgs = []
for f in frames:
    im = Image.open(f).convert('RGB')
    if im.size != (W*SCALE, H*SCALE):
        im = im.resize((W*SCALE, H*SCALE), Image.LANCZOS)
    imgs.append(im)
dpi = (W*SCALE)/13.3333
imgs[0].save(OUTBASE + '.pdf', save_all=True, append_images=imgs[1:], resolution=dpi)
print('PDF :', OUTBASE + '.pdf', f'{os.path.getsize(OUTBASE + ".pdf")//1024} KB')

# ── PPTX (16:9, imagem full-bleed por slide) ──
prs = Presentation()
prs.slide_width  = Inches(13.3333)
prs.slide_height = Inches(7.5)
blank = prs.slide_layouts[6]
for im, f in zip(imgs, frames):
    s = prs.slides.add_slide(blank)
    buf = io.BytesIO(); im.save(buf, 'JPEG', quality=93, optimize=True); buf.seek(0)
    s.shapes.add_picture(buf, 0, 0, width=prs.slide_width, height=prs.slide_height)
prs.save(OUTBASE + '.pptx')
print('PPTX:', OUTBASE + '.pptx', f'{os.path.getsize(OUTBASE + ".pptx")//1024} KB')
