# HANDOFF — Apresentação Negesp · CALASS 2026 (modelo v2 "Observatório")

Documento de transferência. Tudo o que outra pessoa (ou outro login) precisa para **entender, editar, reconstruir e publicar** esta apresentação.

---

## 1. O que é

Apresentação HTML (single-file, offline) da esposa do LG, **Carla Ulhoa André** (Assessora Técnica do Conass), sobre o **Negesp** (Núcleos Estaduais de Gestão Estratégica da Segurança do Paciente), para o **XXXVI Congresso Anual da ALASS — CALASS 2026, em Montreal (Canadá)**, no fim de julho de 2026.

- **21 slides**, 16:9, tema claro (verde/laranja/branco — identidade Conass).
- Roda 100% no navegador, offline depois de aberta. Não depende de PowerPoint.
- Existem **dois modelos**: o **v1** ("clássico" branco, arquivo `index.html` na raiz do repo) e o **v2** ("Observatório", moderno — é o que está em uso). Todo o trabalho recente é no **v2**.

## 2. Links no ar (GitHub Pages)

- **OFICIAL (usar na apresentação):**
  `https://lgcneiva-pessoal.github.io/negesp-calass-2026/v2/index.html`
- v1 (clássico, backup): `https://lgcneiva-pessoal.github.io/negesp-calass-2026/index.html`

Funciona em desktop **e celular** (no celular: deitar o aparelho na horizontal; na vertical aparece o aviso "Gire o celular").

## 3. Repositório (fonte da verdade)

- GitHub: **`lgcneiva-pessoal/negesp-calass-2026`** (público; Pages servindo do branch `main`).
- Estrutura:
  ```
  index.html          → v1 publicado (clássico)
  v2/index.html       → v2 publicado (É O ARQUIVO OFICIAL, o link aponta pra cá)
  source/             → pipeline de build do v2 (tudo para reconstruir)
    build_v2.py       → montador: junta CSS + seções + JS, injeta assets base64, roda o parity checker, grava em ../v2/index.html
    sections_a.py     → templates HTML dos slides s01–s10 + sorg (organograma)
    sections_b.py     → templates HTML dos slides s11–s20
    style.css         → estilos base do v2
    script.js         → engine (navegação, revelações, cenas, órbita, mobile)
    assets/           → imagens base64, logos, QRs, conteudo_v1.json (base do parity)
    build-and-deploy.sh → atalho: build + commit + push
  HANDOFF.md          → este documento
  ```
- **IMPORTANTE:** a cópia local original da fonte fica em `/Users/LG/TEMP/carla-calass-2026/v2-build/` (só acessível ao usuário `LG`). O repo em `source/` é a cópia **portável e auto-contida** — use ela em qualquer login.

## 4. Como reconstruir (portável, sem editar caminhos)

```bash
git clone https://github.com/lgcneiva-pessoal/negesp-calass-2026.git
cd negesp-calass-2026/source
python3 build_v2.py      # grava em ../v2/index.html e roda o parity checker
```
- Precisa de **Python 3** (só usa a stdlib). `build_v2.py` calcula os caminhos relativos ao próprio arquivo (`B = dir do script`, `OUT = ../v2/index.html`), então roda de qualquer lugar.
- O build imprime `✓ PARIDADE TOTAL` quando todo o texto do v1 está presente no v2. Se falhar, ele lista os trechos faltando e sai com erro.

## 5. Como publicar (⚠️ pegadinha da conta GitHub)

O repo é da conta **`lgcneiva-pessoal`**, mas neste Mac o `gh` tem DUAS contas e a **ativa por padrão é `pitidevendas`** (a errada). Um `git push` normal falha/vai pro lugar errado. Use SEMPRE o token da conta certa numa URL explícita:

```bash
cd negesp-calass-2026
TOKEN=$(gh auth token --user lgcneiva-pessoal)
git push "https://x-access-token:${TOKEN}@github.com/lgcneiva-pessoal/negesp-calass-2026.git" main
```

Ou rode o atalho `source/build-and-deploy.sh "mensagem do commit"` (faz build + add + commit + push com o token certo).

**Se for OUTRO usuário do macOS** (não o `LG`): o `gh` guarda os tokens no keychain **por usuário**, então o novo login **não terá** essas contas. Será preciso `gh auth login` como `lgcneiva-pessoal` (a dona do repo) ou usar um Personal Access Token dela. Se for outra sessão do MESMO usuário `LG`, o keychain é compartilhado e já funciona.

**Cache do GitHub Pages / navegador:** depois do push, a propagação leva ~30–90s. Para conferir/forçar a versão nova use `?v=<qualquer-coisa>` na URL, ou `Ctrl+Shift+R`. Nunca divulgue o link com `?v=...` — o oficial é o limpo (item 2).

## 6. Regras globais do projeto (NÃO QUEBRAR)

- **Sem travessão (—) em nenhum texto visível.** `build_v2.py` tem `sem_travessao()` que converte — em vírgula nas notas/títulos. Manter.
- **Parity checker:** o build confere, caractere a caractere, que TODO o texto do v1 (de `assets/conteudo_v1.json`) está presente no v2. `norm()` ignora só a troca de pontuação autorizada (`— – : · ,`). Se você **remover** de propósito algum texto do v1, adicione-o ao set `REMOVIDOS` em `build_v2.py` (já contém "Merci beaucoup." e o antigo card da Biblioteca do s19), senão o build falha.
- **Slides exclusivos do v2** (sem contraparte no v1, ex.: o organograma) ficam no dict `EXTRA_SLIDES` de `build_v2.py`, com `title` (índice) e `notes` (notas da apresentadora). O parity checker os ignora.
- **Fluxo de trabalho com o LG:** editar direto e publicar; **não** ficar avisando sobre atualizar PDF/PPTX até ele dizer que terminou a revisão. Idioma: **pt-BR**.

## 7. Ordem dos slides e o que tem em cada um

Ordem montada em `build_v2.py` (`order`), com o organograma inserido no índice 3:
`s01, s02, s03, sorg, s04, s05, s06, s07, s08, s09, s10, s11, s12, s13, s14, s15, s16, s17, s18, s19, s20`

| Nº | id | Conteúdo |
|----|-----|----------|
| 1 | s01 | Capa (fundo escuro) |
| 2 | s02 | Citação de abertura |
| 3 | s03 | O Conass (frase justificada+negrito, foto Dr. Adib Jatene, stats 1982/27/2) |
| **4** | **sorg** | **Organograma do Conass** (slide NOVO do v2 — ver item 8) |
| 5 | s04 | Câmara Técnica de Qualidade no Cuidado e Segurança do Paciente (3 faixas) |
| 6 | s05 | (substituído pelo do v1) |
| 7–12 | s06–s11 | Conteúdo Negesp; s10 = feixes/beams; s11 = mapa grande |
| 13 | s12 | Entradas → Processo → Resultados |
| 14 | s13 | **Órbita radial** (21st.dev) — passos 1–4 abrem cada nó; passo 5 mostra os 4 cards resumo. **Sempre entra pela órbita** (regra `#s13.on` reseta step 0), mesmo em acesso direto/índice |
| 15 | s14 | Comitê Consultivo (opção "faixas") |
| 16 | s15 | — |
| 17 | s16 | Rede nacional colaborativa (6 cards uniformes ao redor do mapa) |
| 18 | s17 | — |
| 19 | s18 | — |
| **20** | **s19** | **Visão + 2 QR codes** (Biblioteca Digital Conass / Rede Negesp) — ver item 9 |
| 21 | s20 | Encerramento "Obrigada." + contatos da Carla + foto |

Menu/índice (tecla **O**) tem os 21 itens; numeração e HUD já refletem 21 slides. A **logo Conass** aparece no canto de todos, exceto capa (s01) e encerramento (s20); no s19 ela é ocultada de propósito (`#s19.on ~ .cornerlogo{display:none}`) para a frase usar a largura toda.

## 8. Slide 4 — Organograma (dados auditados; NÃO alterar sem conferir)

Unificado das duas telas originais que o LG mandou (uma era continuação da outra; a Secretaria Executiva aparece só uma vez). Hierarquia:
- **Assembleia** (27 secretários de Saúde dos estados e DF)
- **Diretoria** (1 presidente + 5 vice-presidentes, 1 por macrorregião) + satélites: Comissão Fiscal, Representações Oficiais, Comitê Consultivo (ex-presidentes)
- **Secretaria Executiva** (Secretário Executivo · Equipes Técnica e Administrativa) + Assessorias: Jurídica, Comunicação Social, Parlamentar
- **3 Coordenações:** Técnica · Administração e de Finanças · Desenvolvimento Institucional
- **14 Núcleos Técnicos** (o item destacado é "Qualidade e Segurança do Paciente")
- **14 Câmaras Técnicas** (inclui "Laboratório de Saúde Pública"; item destacado "Qualidade no Cuidado e Segurança do Paciente" fica por último de propósito, é a deixa pro slide 5)
- Adm/Finanças → Gerências Administrativa, de Compras e Contratos, Financeira
- Desenvolvimento → Unidade de Gestão de Projetos

Correções de digitação feitas vs. as telas originais: "(MAC eRegulação)" → "(MAC e Regulação)"; abreviações de "Gestão do Trabalho e da Educação em Saúde" expandidas.

## 9. QR codes (slide 20 / s19)

- **Biblioteca Digital Conass** → `https://www.conass.org.br/biblioteca/`
- **Rede Negesp** → `https://www.conass.org.br/negesp/`
- Gerados com **segno** (`pip install segno`), SVG, cor `#0A2416` sobre branco, correção de erro 'm'. Ficam em `assets/qr_bib.b64` e `assets/qr_neg.b64` (base64 de SVG), injetados via tokens `%%QRBIB%%` / `%%QRNEG%%`.
- Para regenerar (ex.: mudar URL): usar `segno.make(url, error='m').save(buf, kind='svg', dark='#0A2416', light='#ffffff', border=3, scale=10)`, base64, gravar no .b64. **Sempre decodificar de volta pra conferir** (ex.: `cv2.QRCodeDetector`).
- Títulos em **preto** (`--ink`), caixa-alta, com traço laranja embaixo e halo branco no texto (legibilidade sobre a foto). QRs grandes, nos cantos opostos (bem separados p/ escanear de longe).

## 10. Suporte a celular

- `<meta name="viewport" content="width=1280">` → o celular renderiza como um desktop de 1280px e escala pra caber (padrão de players de slides).
- Aviso de girar a tela: `.rotatehint`, só aparece em `@media (orientation:portrait) and (pointer:coarse)`.
- Navegação por toque (arrastar) já existia; tem guarda `portraitLock()` no `script.js` pra não navegar por baixo do aviso. Pinça (zoom) livre.

## 11. Pendências / próximos passos

- **PDF e PPTX de backup: GERADOS** (a pedido do LG, agosto/2026), nas duas línguas, em `~/Downloads`:
  `Negesp-CALASS-2026-PT.pdf` · `Negesp-CALASS-2026-PT.pptx` · `Negesp-CALASS-2026-FR.pdf` · `Negesp-CALASS-2026-FR.pptx`
  Todos com 22 slides, 16:9 (13,333 × 7,5 pol), imagens 2560×1440.
- Nenhuma outra pendência aberta; a apresentação está aprovada pelo LG.

### Como regerar o PDF/PPTX (fiel ao deck aprovado)

Não recriar o design em pptxgenjs (perde fidelidade). O método que funcionou: **renderizar os slides reais** com Playwright e montar os arquivos a partir das imagens. Script em `source/render_deck.py`:

```bash
cd <repo> && python3 -m http.server 8791 &     # servir o repo
python3 source/render_deck.py "http://localhost:8791/v2/index.html"    ~/Downloads/Negesp-CALASS-2026-PT
python3 source/render_deck.py "http://localhost:8791/v2-fr/index.html" ~/Downloads/Negesp-CALASS-2026-FR
```

Requisitos: `playwright` (python) + chromium, `Pillow`, `python-pptx`.
Detalhes que o script já trata (não remover):
- Navega com `window.goTo(i, true)` (revela todos os passos do slide).
- **s13 (órbita)** entra sempre no passo 0; o script força `window.__s13step(5)` para mostrar os 4 cards de resumo.
- **s11 / s16 (mapas)** precisam de ~4s de espera: o traçado e os arcos são animados via JS.
- Slides com conectores SVG (s08, s10, s12, s14, s15, s17) e o `sbra` (mapas com "pulo") precisam de espera extra antes do screenshot.
- Esconde só `.hud .hbl` (dica de teclado, que não faz sentido impressa); mantém logo e numeração.

## 12. Dicas de verificação (workflow que funcionou)

- Servir local pra testar: `cd <repo> && python3 -m http.server 8791`, abrir `http://localhost:8791/v2/index.html`.
- Testar nos dois tamanhos: **1280×720** e **1512×860**.
- Medir overflow/colisão via JS no browser (getBoundingClientRect) em vez de confiar só no olho.
- Preview às vezes retorna viewport `[0,0]` (snapshot estático) ou `transform` de revelação não-assentado — nesses casos a captura de tela (screenshot) é a verdade; refazer a medição após `resize_window` + navegação limpa.
