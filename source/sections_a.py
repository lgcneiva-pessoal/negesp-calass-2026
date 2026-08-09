# -*- coding: utf-8 -*-
# Seções s01–s10 · arquitetura 2 — cada slide com geometria própria; textos VERBATIM

S01 = '''
<section class="slide" id="s01" data-title="Capa">
  <div class="cover"></div><div class="scrim"></div>
  <div class="rail rv" style="--d:1900"><span>Montreal · Canadá · <b>2026</b> · CALASS · XXXVI</span></div>
  <div class="wrap">
    <div class="badge rv" style="--d:100">XXXVI Congresso Anual da Associação Latina para a Análise dos Sistemas de Saúde · Montreal · Canadá · 2026</div>
    <h1 data-words>Um modelo <span class="hl">inovador</span> de governança para a <span class="hl">segurança do paciente</span> no Brasil</h1>
    <p class="sub rv" style="--d:1500">Os Núcleos Estaduais de Gestão Estratégica da Segurança do Paciente: <span class="neg">Negesp</span></p>
    <div class="authors rv" style="--d:1750">
      <div><b>Carla Ulhoa André</b><span>Assessora Técnica</span></div>
      <div class="cn"><b>Conass</b><span>Conselho Nacional de Secretários de Saúde · Brasil</span></div>
    </div>
  </div>
  {NOTES}
</section>'''

S02 = '''
<section class="slide" id="s02" data-title="Pergunta de abertura">
  <div class="mark" aria-hidden="true">?</div>
  <div class="wrap">
    <p class="q" data-words>É possível promover qualidade e segurança do paciente quando as decisões não são sustentadas por <span class="hl">evidências?</span><span class="caret" aria-hidden="true"></span></p>
  </div>
  {NOTES}
</section>'''

S03 = '''
<section class="slide" id="s03" data-title="Conass">
  <div class="wrap">
    <div class="midpair">
      <div class="leadbox rv" style="--d:260"><p class="lead">O Conselho Nacional de Secretários de Saúde congrega os secretários de saúde dos estados e do Distrito Federal, uma associação que atua pelos princípios do direito público, com autonomia administrativa, financeira e patrimonial.</p></div>
      <div class="photo rv" style="--d:420"><div class="frame"><img src="data:image/jpeg;base64,%%JATENE%%" alt="Fotografia do doutor Adib Jatene, com seu nome impresso na peça original"></div></div>
    </div>
    <div class="tagbox rv" style="--d:800">“A força dos estados na garantia do <em>direito à saúde</em>.”</div>
    <div class="stats">
      <div class="stat st"><b>1982</b><span>instituído em 3 de fevereiro</span></div>
      <div class="stat st"><b>27</b><span>Representa as Secretarias Estaduais de Saúde</span></div>
      <div class="stat st"><b>2</b><span>leis federais reconhecem o Conselho: Lei 8.142/1990 e Lei 12.466/2011 (artigos 14-A e 14-B)</span></div>
    </div>
  </div>
  {NOTES}
</section>'''

SORG = '''
<section class="slide" id="sorg" data-title="Organograma do Conass">
  <div class="wrap">
    <div class="kick rv" style="--d:60">Como o Conass se organiza</div>
    <h2 class="title rv" style="--d:160">Da Assembleia Geral às <em>câmaras técnicas</em></h2>
    <div class="chart">
      <div class="orow rv" style="--d:280">
        <div class="obox top"><b>Assembleia Geral</b><span>Os 27 secretários de Saúde dos estados e do Distrito Federal</span></div>
        <div class="side R"><i class="tap"></i><div class="chip"><b>Comitê Consultivo</b><span>ex-presidentes</span></div></div>
      </div>
      <i class="vl rv" style="--d:330"></i>
      <div class="orow rv" style="--d:380">
        <div class="obox"><b>Diretoria</b><span>1 presidente e 5 vice-presidentes · 1 por macrorregião</span></div>
        <div class="side R"><i class="tap"></i><div class="chip"><b>Conselho Fiscal</b></div></div>
      </div>
      <i class="vl rv" style="--d:430"></i>
      <div class="obox solo rv" style="--d:470"><b>Presidência</b></div>
      <i class="vl rv" style="--d:510"></i>
      <div class="obox solo sec rv" style="--d:550"><b>Secretaria Executiva</b><span>Secretário Executivo · Equipes Técnica e Administrativa</span></div>
      <i class="vl rv" style="--d:590"></i>
      <div class="branch rv" style="--d:620">
        <div class="bcol L"><div class="obox cam"><b>Câmaras Técnicas</b></div><i class="tap o"></i></div>
        <i class="spine"></i>
        <div class="bcol R"><i class="tap"></i>
          <div class="pan gab">
            <h6>Gabinete</h6>
            <ul>
              <li>Apoio do Gabinete</li>
              <li>Assessoria Jurídica</li>
              <li>Assessoria Parlamentar</li>
              <li>Assessoria de Comunicação</li>
              <li>Assessoria de Informações Estratégicas</li>
            </ul>
          </div>
        </div>
      </div>
      <i class="vl rv" style="--d:660"></i>
      <div class="dist3 rv" style="--d:700"><i class="feed"></i><i class="bar"></i><i class="d a"></i><i class="d b"></i><i class="d c"></i></div>
      <div class="coords rv" style="--d:740">
        <div class="coord dev"><b>Coordenação de Desenvolvimento Institucional</b></div>
        <div class="coord tec"><b>Coordenação Técnica</b></div>
        <div class="coord adm"><b>Coordenação de Administração e de Finanças</b></div>
      </div>
      <div class="subs rv" style="--d:790">
        <div class="subcol"></div>
        <div class="subcol"><i class="drop"></i><div class="chip"><b>Assessorias Técnicas</b></div></div>
        <div class="subcol"><i class="drop"></i><div class="fork"><i class="fb"></i><i class="fd fl"></i><i class="fd fr"></i></div><div class="gerrow"><div class="chip"><b>Gerência Administrativa</b></div><div class="chip"><b>Gerência Financeira</b></div></div></div>
      </div>
    </div>
  </div>
  {NOTES}
</section>'''

SBRA = '''
<section class="slide" id="sbra" data-title="Brasil">
  <div class="wrap">
    <div class="kick rv" style="--d:60">O contexto brasileiro</div>
    <h2 class="title rv" style="--d:160"><em>Brasil</em>: dimensão continental</h2>
    <div class="bcols">
      <div class="bleft">
        <figure class="tmap jump" style="--jd:.14s">
          <img src="data:image/png;base64,%%MAPTERR%%" alt="Mapa do território brasileiro por população, com área de 8.510.418 km² e densidade de 23,86 habitantes por km² (Censo 2022, IBGE)">
          <figcaption>Território, área e densidade · Censo 2022 · 71% dos municípios com menos de 20 mil hab. (IBGE)</figcaption>
        </figure>
        <div class="stats rv" style="--d:560">
          <div class="pop"><b>213.485.153</b><span>habitantes · população residente (IBGE, 2026)</span></div>
          <div class="grid5">
            <div class="s"><b>26<i>+DF</i></b><span>Estados e DF</span></div>
            <div class="s"><b>5.571</b><span>Municípios</span></div>
            <div class="s"><b>5</b><span>Regiões geográficas</span></div>
            <div class="s"><b>117</b><span>Macrorregiões de saúde</span></div>
            <div class="s"><b>453</b><span>Regiões de saúde</span></div>
          </div>
        </div>
      </div>
      <figure class="gmap jump" style="--jd:.3s">
        <img src="data:image/png;base64,%%MAPGINI%%" alt="Mapa do Brasil pelo Índice de Gini por grande região: Sul 0,448, Centro-Oeste 0,486, Sudeste 0,508, Norte 0,517 e Nordeste 0,520; Brasil 0,509. Fonte: IBGE">
        <figcaption>Índice de Gini por grande região (2024) · Brasil <b>0,509</b> · 2º país com maior desigualdade no <em>G20</em></figcaption>
      </figure>
    </div>
  </div>
  {NOTES}
</section>'''

S04 = '''
<section class="slide" id="s04" data-title="Câmara Técnica">
  <div class="wrap">
    <div class="kick rv" style="--d:60">Onde a agenda nacional se encontra</div>
    <h2 class="title rv" style="--d:200">A Câmara Técnica de Qualidade no Cuidado e <em>Segurança do Paciente</em></h2>
    <div class="duo">
      <div class="cards">
        <div class="pan glass st"><span class="num">01</span><h4>Objetivos</h4><p>Assessorar a Secretaria Executiva, a Diretoria e a Assembleia dos Secretários do Conass na formulação de políticas e estratégias voltadas à qualidade e segurança do paciente, promovendo a construção de consensos técnicos.</p></div>
        <div class="pan glass st"><span class="num">02</span><h4>Instituição e composição</h4><p>Constituída em 2017, é composta por representantes das Secretarias de Saúde e do Distrito Federal, oficialmente indicados pelos Secretários de Estado da Saúde, com designação de um representante titular e um suplente.</p></div>
        <div class="pan glass st"><span class="num">03</span><h4>Eixos de atuação</h4><p>Promove a integração e a troca de experiências entre as secretarias, fortalecendo a gestão estadual e qualificando os processos de trabalho.</p></div>
        <div class="pan glass st"><span class="num">04</span><h4>Governança e funcionamento</h4><p>Reuniões ordinárias e extraordinárias, promovendo a construção de consensos técnicos. Sua atuação é fortalecida pela articulação com o Ministério da Saúde, a Agência Nacional de Vigilância Sanitária, o Conselho Nacional de Secretarias Municipais de Saúde e a Organização Pan-Americana da Saúde, contribuindo para o desenvolvimento e a implementação de políticas públicas.</p></div>
      </div>
      <div class="photo rv" style="--d:420"><img src="data:image/jpeg;base64,%%GRUPO%%" alt="Representantes das vinte e sete secretarias estaduais de saúde reunidos na sede do Conselho Nacional de Secretários de Saúde"></div>
    </div>
  </div>
  {NOTES}
</section>'''

S05 = '''
<section class="slide" id="s05" data-title="O problema: fragmentação">
  <div class="wrap">
    <div class="kick rv" style="--d:60">O ponto de partida</div>
    <h2 class="title rv" style="--d:200" data-swap-title><span class="tt-a">Um sistema potente, ações <em>fragmentadas</em></span><span class="tt-b" hidden>O que a evolução <em>exige</em></span></h2>
    <div class="split5">
      <div class="dotstage rv" style="--d:320" aria-hidden="true">
        <svg class="linkslayer"></svg>
      </div>
      <div class="pains">
        <div class="pain st" data-st="1" data-phase="a"><i>!</i><p><b>Fragmentação</b> das ações de segurança do paciente.</p></div>
        <div class="pain st" data-st="2" data-phase="a"><i>!</i><p><b>Baixa integração</b> entre as áreas estratégicas das secretarias estaduais de saúde.</p></div>
        <div class="pain st" data-st="3" data-phase="a"><i>!</i><p><b>Dados brutos</b> que não se transformam em decisões ágeis.</p></div>
        <div class="pain good st" data-st="4" data-phase="b"><i>✓</i><p><b>Informações qualificadas</b> para apoiar a alta gestão.</p></div>
        <div class="pain good st" data-st="5" data-phase="b"><i>✓</i><p><b>Fortalecimento</b> da Política Nacional de Qualidade e Segurança do Paciente.</p></div>
        <div class="pain good st" data-st="6" data-phase="b"><i>✓</i><p><b>Monitoramento de riscos</b> em toda a Rede de Atenção à Saúde.</p></div>
      </div>
    </div>
  </div>
  {NOTES}
</section>'''

S06 = '''
<section class="slide" id="s06" data-title="A definição da política">
  <div class="glyph" aria-hidden="true">“</div>
  <div class="wrap">
    <div class="kick rv" style="--d:60">O alicerce nacional</div>
    <p class="quote rv" style="--d:280">Um conjunto de ações, práticas e processos destinados a <span class="hl">reduzir riscos e danos evitáveis</span>, promovendo cuidado <span class="hl2">seguro, efetivo, oportuno, eficiente, equitativo e centrado na pessoa</span>.”</p>
    <div class="attr rv" style="--d:820">Política Nacional de Qualidade e Segurança do Paciente</div>
  </div>
  {NOTES}
</section>'''

S07 = '''
<section class="slide" id="s07" data-title="O marco legal">
  <div class="wrap">
    <div class="kick rv" style="--d:60">O marco legal da transformação</div>
    <h2 class="title rv" style="--d:200">A segurança do paciente vira <em>política de Estado</em></h2>
    <div class="scene">
      <div class="monument rv" style="--d:380">
        <div class="selo">Publicada</div>
        <div class="dou">Diário Oficial da União</div>
        <div class="bigdate">9 de junho de 2026</div>
        <div class="portn">Portaria número 11.527 · Ministério da Saúde</div>
        <p class="ementa">Institui a Política Nacional de Qualidade e Segurança do Paciente no âmbito do Sistema Único de Saúde.</p>
      </div>
      <div class="metro">
        <div class="stop st"><div class="from">Esforço governamental temporário</div><div class="to">Política de Estado permanente</div></div>
        <div class="stop st"><div class="from">Iniciativas dispersas</div><div class="to">Implementação por eixos territoriais, orientada por resultados</div></div>
        <div class="stop st"><div class="from">Modelos isolados</div><div class="to">Um modelo sistêmico para todos os estabelecimentos do Sistema Único de Saúde</div></div>
      </div>
    </div>
  </div>
  {NOTES}
</section>'''

S08 = '''
<section class="slide" id="s08" data-title="Governança em quatro níveis">
  <div class="wrap">
    <div class="kick rv" style="--d:60">Do macro ao micro</div>
    <h2 class="title rv" style="--d:180">Uma política, <em>quatro níveis</em> de responsabilidade</h2>
    <div class="resplabel rv" style="--d:300">Responsabilidade estratégica</div>
    <div class="diamond">
      <svg class="links" aria-hidden="true"></svg>
      <div class="dcard fed glass st" data-link="fed"><div class="lvl">Federal</div><div class="who">Ministério da Saúde</div><div class="resp"><ul><li>Definir a política nacional.</li><li>Estabelecer diretrizes, estratégias e prioridades nacionais.</li><li>Instituir mecanismos de financiamento e adotar estratégias indutoras para o fortalecimento das ações.</li></ul></div></div>
      <div class="dcard est glass st" data-link="est"><div class="lvl">Estadual</div><div class="who">Núcleo Estadual de Gestão Estratégica da Segurança do Paciente</div><div class="resp"><ul><li>Coordenar a implementação da política no território.</li><li>Promover a integração das ações no âmbito das regiões de saúde.</li><li>Apoiar tecnicamente os municípios na implementação das ações.</li><li>Monitorar resultados da Rede de Atenção à Saúde.</li></ul></div></div>
      <div class="dcard mun glass st" data-link="mun"><div class="lvl">Municipal</div><div class="who">Núcleo Municipal de Gestão Estratégica da Segurança do Paciente</div><div class="resp"><ul><li>Coordenar a implementação das ações da política nos serviços de saúde.</li><li>Monitorar e analisar indicadores.</li><li>Apoiar a implementação e o funcionamento dos Núcleos de Segurança do Paciente nos serviços de saúde.</li></ul></div></div>
      <div class="dcard srv glass st" data-link="srv"><div class="lvl">Serviços de saúde</div><div class="who">Hospitais, unidades básicas e demais pontos de atenção à saúde</div><div class="resp"><ul><li>Instituir Núcleo de Segurança do Paciente.</li><li>Implementar práticas assistenciais seguras baseadas em evidências e diretrizes.</li><li>Notificar, analisar e promover aprendizagem organizacional a partir de incidentes e eventos adversos.</li></ul></div></div>
    </div>
  </div>
  {NOTES}
</section>'''

S09 = '''
<section class="slide" id="s09" data-title="O elo crítico">
  <div class="wrap">
    <div class="kick center rv" style="--d:60">O elo que faltava no Sistema Único de Saúde</div>
    <div class="plate rv" style="--d:260">
      <img src="data:image/png;base64,%%LOGONEGESP%%" alt="Logomarca do Negesp: Núcleo Estadual de Gestão Estratégica da Segurança do Paciente · Conass">
    </div>
    <p class="statement rv" style="--d:520">O Núcleo Estadual de Gestão Estratégica da Segurança do Paciente, <span class="g">Negesp</span>, é a estrutura permanente que conecta a <span class="g">evidência científica</span> à <span class="g">prática cotidiana</span>.</p>
    <div class="chips">
      <div class="chip st">Vinculado à alta gestão das secretarias estaduais de saúde</div>
      <div class="chip st">Transversal a toda Rede de Atenção à Saúde</div>
      <div class="chip o st">Foco: subsidiar as tomadas de decisão, reduzir eventos adversos evitáveis e otimizar recursos públicos</div>
    </div>
  </div>
  {NOTES}
</section>'''

S10 = '''
<section class="slide" id="s10" data-title="O que é o Negesp">
  <div class="wrap">
    <div class="head">
      <div class="kick rv" style="--d:60">Anatomia do modelo</div>
      <h2 class="title rv" style="--d:200">Uma estrutura estratégica <em>deliberativa</em>, vinculada à alta gestão da secretaria estadual</h2>
      <p class="lead rv" style="--d:360">Apoia a gestão na formulação, no monitoramento e na avaliação das ações de qualidade do cuidado e segurança do paciente, e cumpre cinco funções.</p>
    </div>
    <div class="stage" id="beamStage">
      <svg class="beams" aria-hidden="true"></svg>
      <div class="core rv" style="--d:500">Negesp</div>
      <div class="fn st" style="left:22%;top:16%"><i>1</i> · Espaço de governança</div>
      <div class="fn st" style="left:78%;top:16%"><i>2</i> · Integração entre áreas</div>
      <div class="fn st" style="left:85%;top:54%"><i>3</i> · Apoio à tomada de decisão</div>
      <div class="fn st" style="left:50%;top:88%"><i>4</i> · Produção de inteligência para a gestão</div>
      <div class="fn st" style="left:15%;top:54%"><i>5</i> · Indução da cultura de segurança</div>
    </div>
  </div>
  {NOTES}
</section>'''

SECTIONS_A = {'s01':S01,'sbra':SBRA,'s02':S02,'s03':S03,'sorg':SORG,'s04':S04,'s05':S05,'s06':S06,'s07':S07,'s08':S08,'s09':S09,'s10':S10}
