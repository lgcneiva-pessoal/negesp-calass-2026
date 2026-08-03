# -*- coding: utf-8 -*-
# Seções s11–s20 · arquitetura 2 — textos VERBATIM

S11 = '''
<section class="slide" id="s11" data-title="O Negesp em números">
  <div class="wrap" style="padding:0">
    <div class="stage">
      <div class="holo rv" style="--d:300">
        <div class="table">
          <div class="ringsF"></div>
          <div class="sweep"></div>
          <svg class="brmap" id="mapMain" role="img" aria-label="Mapa do Brasil com a situação de implantação por unidade federativa"></svg>
          <div class="floor"></div>
        </div>
      </div>
      <div class="reading rv" style="--d:150">
        <div class="kick">O Negesp em números</div>
        <b id="ufcount" style="margin-top:.2em">26</b>
        <small>unidades federativas no movimento nacional de implantação</small>
      </div>
      <div class="legend">
        <div class="lg rv" style="--d:700"><i class="g"></i>Estados implantados: Negesp oficialmente instituído e em funcionamento</div>
        <div class="lg st" data-st="1"><i class="o"></i>Rio Grande do Sul: em implementação, estado em processo de estruturação</div>
      </div>
    </div>
  </div>
  {NOTES}
</section>'''

S12 = '''
<section class="slide" id="s12" data-title="O motor do Negesp">
  <div class="wrap">
    <div class="kick rv" style="--d:60">Como a estratégia vira ação</div>
    <div class="line">
      <div class="side">
        <h5 class="rv" style="--d:200">Entradas</h5>
        <div class="io glass st">Diretrizes da Política Nacional de Qualidade e Segurança do Paciente</div>
        <div class="io glass st">Evidências científicas</div>
        <div class="io glass st">Dados locais</div>
      </div>
      <div class="reactor rv" style="--d:350">
        <div class="rlabel">
          <svg viewBox="0 0 200 200" aria-hidden="true">
            <circle class="track" cx="100" cy="100" r="86" fill="none" stroke-width="6"/>
            <g id="gearSpin" style="transform-origin:100px 100px">
              <circle class="dash" cx="100" cy="100" r="74" fill="none" stroke-width="7" stroke-dasharray="24 15" stroke-linecap="round"/>
              <circle class="dot" cx="174" cy="100" r="9"/>
            </g>
          </svg>
          <span>O processo<br>Negesp</span>
        </div>
        <div class="proc st">Diagnóstico situacional<small>matriz de forças, fraquezas, oportunidades e ameaças</small></div>
        <div class="proc st">Planejamento de melhoria<small>ciclos planejar · fazer · estudar · agir</small></div>
        <div class="proc st">Articulação intersetorial<small>além dos muros da secretaria</small></div>
      </div>
      <div class="side right">
        <h5 class="rv" style="--d:200">Resultados</h5>
        <div class="io glass st">Tomada de decisão assertiva <span>com o Centro de Inteligência Estratégica</span></div>
        <div class="io glass st">Cultura de melhoria contínua</div>
        <div class="io glass st">Ambiente de cuidado seguro em toda a Rede de Atenção à Saúde</div>
      </div>
    </div>
  </div>
  {NOTES}
</section>'''

S13 = '''
<section class="slide" id="s13" data-title="Camadas de governança">
  <div class="wrap">
    <div class="kick rv" style="--d:60">Da equipe técnica à rede nacional</div>
    <div class="orb5 rv" style="--d:220" id="orb5">
      <div class="oring"></div>
      <div class="oring2"></div>
      <div class="ocore"><span></span></div>
      <div class="onode st k1" data-st="4">
        <button type="button" class="obtn"><i>1</i></button>
        <div class="olabel">Rede nacional e parceiros externos</div>
        <div class="ocard"><h5><i>1</i>Rede nacional e parceiros externos</h5><p>a articulação sistêmica, coordenada pelo Conselho Nacional de Secretários de Saúde.</p>
          <div class="orel"><button type="button" data-goto="1">Negesp estadual</button></div></div>
      </div>
      <div class="onode st k2" data-st="3">
        <button type="button" class="obtn"><i>2</i></button>
        <div class="olabel">Negesp estadual</div>
        <div class="ocard"><h5><i>2</i>Negesp estadual</h5><p>a estrutura consolidada de governança no estado.</p>
          <div class="orel"><button type="button" data-goto="0">Rede nacional e parceiros externos</button><button type="button" data-goto="2">Comitê consultivo</button></div></div>
      </div>
      <div class="onode st k3" data-st="2">
        <button type="button" class="obtn"><i>3</i></button>
        <div class="olabel">Comitê consultivo</div>
        <div class="ocard"><h5><i>3</i>Comitê consultivo</h5><p>a integração com os departamentos da secretaria estadual de saúde.</p>
          <div class="orel"><button type="button" data-goto="1">Negesp estadual</button><button type="button" data-goto="3">Equipe técnica multiprofissional</button></div></div>
      </div>
      <div class="onode st k4" data-st="1">
        <button type="button" class="obtn"><i>4</i></button>
        <div class="olabel">Equipe técnica multiprofissional</div>
        <div class="ocard"><h5><i>4</i>Equipe técnica multiprofissional</h5><p>a base de operação técnica, dentro da secretaria estadual.</p>
          <div class="orel"><button type="button" data-goto="2">Comitê consultivo</button></div></div>
      </div>
    </div>
    <i class="st" data-st="5" aria-hidden="true" style="display:none"></i>
    <div class="orbsummary" aria-hidden="true">
      <div class="oscard k1"><span class="osn">1</span><b>Rede nacional e parceiros externos</b><p>a articulação sistêmica, coordenada pelo Conselho Nacional de Secretários de Saúde.</p></div>
      <div class="oscard k2"><span class="osn">2</span><b>Negesp estadual</b><p>a estrutura consolidada de governança no estado.</p></div>
      <div class="oscard k3"><span class="osn">3</span><b>Comitê consultivo</b><p>a integração com os departamentos da secretaria estadual de saúde.</p></div>
      <div class="oscard k4"><span class="osn">4</span><b>Equipe técnica multiprofissional</b><p>a base de operação técnica, dentro da secretaria estadual.</p></div>
    </div>
    <div class="orbprint"><div><b>1 · Rede nacional e parceiros externos</b><span>a articulação sistêmica, coordenada pelo Conselho Nacional de Secretários de Saúde.</span></div><div><b>2 · Negesp estadual</b><span>a estrutura consolidada de governança no estado.</span></div><div><b>3 · Comitê consultivo</b><span>a integração com os departamentos da secretaria estadual de saúde.</span></div><div><b>4 · Equipe técnica multiprofissional</b><span>a base de operação técnica, dentro da secretaria estadual.</span></div></div>
  </div>
  {NOTES}
</section>'''

S14 = '''
<section class="slide" id="s14" data-title="Comitê consultivo por dentro">
  <div class="wrap">
    <div class="kick rv" style="--d:60">O motor de integração interna</div>
    <h2 class="title rv" style="--d:180">O <em>Comitê Consultivo</em> é uma instância colegiada de caráter técnico-consultivo que apoia o Negesp na governança, no planejamento e na tomada de decisão.</h2>
    <div class="tri">
      <div class="tcol fn glass st"><h4><i class="mk g"></i>Função central</h4><ul>
        <li>Reunir diferentes áreas estratégicas da Secretaria Estadual de Saúde e parceiros relevantes.</li>
        <li>Garantir que as decisões do Negesp sejam integradas, baseadas em evidências e alinhadas às necessidades da Rede de Atenção à Saúde.</li>
      </ul></div>
      <div class="tcol atr glass st"><h4><i class="mk o"></i>Principais atribuições</h4><ul>
        <li>Assessorar tecnicamente o Negesp na definição de prioridades estratégicas.</li>
        <li>Contribuir para a elaboração, implementação e monitoramento do plano operativo estadual.</li>
        <li>Analisar indicadores, eventos adversos e resultados de qualidade e segurança do paciente.</li>
        <li>Propor estratégias de melhoria e apoiar a gestão de riscos.</li>
        <li>Favorecer a integração entre as áreas da secretaria e demais instituições parceiras.</li>
        <li>Apoiar a implementação da Política Nacional de Qualidade e Segurança do Paciente no âmbito estadual.</li>
        <li>Fortalecer a articulação entre estado, municípios, serviços de saúde, instituições de ensino e órgãos de controle, quando pertinente.</li>
      </ul></div>
      <div class="tcol comp glass st"><h4><i class="mk g2"></i>Composição sugerida</h4><p class="intro">Pode reunir representantes de áreas estratégicas da secretaria estadual, como:</p><ul>
        <li>Atenção Primária à Saúde</li>
        <li>Atenção Especializada e Hospitalar</li>
        <li>Vigilância em Saúde</li>
        <li>Regulação</li>
        <li>Planejamento</li>
        <li>Gestão da Qualidade</li>
        <li>Educação Permanente</li>
        <li>Saúde Digital e Informação</li>
        <li>Assistência Farmacêutica</li>
        <li>Auditoria, avaliação e monitoramento</li>
        <li>Ouvidoria</li>
        <li>Escola de Saúde Pública, quando houver</li>
      </ul></div>
    </div>
    <p class="foot rv" style="--d:900">Participação ampliada, com <b>representantes externos convidados</b> conforme a pauta.</p>
  </div>
  {NOTES}
</section>'''

S15 = '''
<section class="slide" id="s15" data-title="A dinâmica na secretaria">
  <div class="wrap">
    <div class="kick rv" style="--d:60">O que muda na prática</div>
    <h2 class="title rv" style="--d:180">Da informação dispersa à <em>ação intersetorial</em></h2>
    <div class="climb">
      <svg class="path" aria-hidden="true"></svg>
      <div class="result rv" style="--d:1300"><span class="badge">Qualidade e segurança do paciente transversais a toda a gestão</span></div>
      <div class="stepc glass st"><span class="ord">01</span><h5>Entrada</h5><b>Compartilhamento</b><p>Informações, indicadores e evidências antes dispersas entre os departamentos passam a circular.</p></div>
      <div class="stepc glass st"><span class="ord">02</span><h5>Processamento</h5><b>Análise</b><p>Riscos prioritários identificados e analisados de forma transversal para a alta gestão estadual.</p></div>
      <div class="stepc glass st"><span class="ord">03</span><h5>Saída</h5><b>Ação intersetorial</b><p>Planos de ação coordenados, com elaboração e monitoramento do plano operativo da Política Nacional.</p></div>
    </div>
  </div>
  {NOTES}
</section>'''

S16 = '''
<section class="slide" id="s16" data-title="A rede nacional colaborativa">
  <div class="wrap">
    <div class="kick rv" style="--d:60">Nenhum estado caminha sozinho</div>
    <h2 class="title rv" style="--d:180">Uma rede nacional <em>colaborativa</em>, coordenada pelo Conselho</h2>
    <div class="stage">
      <div class="netmap rv" style="--d:340"><svg class="brmap" id="mapNet" role="img" aria-label="Mapa do Brasil com conexões entre os estados a partir de Brasília"></svg></div>
      <div class="vb glass st L" style="left:17%;top:22%"><b>Compartilhar</b><span>experiências exitosas entre os estados.</span></div>
      <div class="vb glass st L" style="left:13%;top:50%"><b>Monitorar</b><span>os indicadores dos núcleos estaduais.</span></div>
      <div class="vb glass st L" style="left:17%;top:78%"><b>Produzir</b><span>soluções colaborativas.</span></div>
      <div class="vb glass st R" style="left:83%;top:22%"><b>Desenvolver</b><span>projetos estratégicos integrados.</span></div>
      <div class="vb glass st R" style="left:87%;top:50%"><b>Promover</b><span>aprendizagem mútua.</span></div>
      <div class="vb glass st R" style="left:83%;top:78%"><b>Apoiar</b><span>a implementação contínua da Política Nacional.</span></div>
    </div>
  </div>
  {NOTES}
</section>'''

S17 = '''
<section class="slide" id="s17" data-title="Além dos muros">
  <div class="wrap">
    <div class="kick rv" style="--d:60">A ponte entre a gestão, o conhecimento e a sociedade</div>
    <h2 class="title rv" style="--d:180">A segurança do paciente exige articulação <em>além dos muros</em> da secretaria</h2>
    <div class="fanstage">
      <svg class="rays" aria-hidden="true"></svg>
      <div class="hub rv" style="--d:400" id="fanHub">Negesp</div>
      <div class="qd glass st" style="left:46%;top:11%"><h4>Ciência e <em>inovação</em></h4><p>Universidades, centros de pesquisa e hospitais de ensino.</p></div>
      <div class="qd glass st" style="left:56%;top:37%"><h4>Ética e <em>prática</em></h4><p>Conselhos profissionais, sociedades científicas e escolas de saúde pública.</p></div>
      <div class="qd glass st" style="left:56%;top:63%"><h4>Controle <em>institucional</em></h4><p>Ministério Público e tribunais de contas.</p></div>
      <div class="qd glass st" style="left:46%;top:89%"><h4>Alinhamento <em>global</em></h4><p>Organismos nacionais e internacionais.</p></div>
    </div>
  </div>
  {NOTES}
</section>'''

S18 = '''
<section class="slide" id="s18" data-title="A equação de valor">
  <div class="wrap">
    <div class="kick center rv" style="--d:60">A equação de valor do Negesp</div>
    <div class="eqline">
      <div class="term a st"><h4>Conecta</h4></div>
      <div class="op st">+</div>
      <div class="term b st"><h4>Produz</h4></div>
      <div class="op st">=</div>
      <div class="term c st"><h4>Entrega</h4></div>
    </div>
    <div class="caps">
      <div class="cap a st">Gestão, assistência, vigilância, ensino e controle social.</div>
      <div class="cap b st">Dados, evidências, aprendizagem e melhoria contínua.</div>
      <div class="cap c st">Governança, decisões qualificadas e resultados em saúde.</div>
    </div>
  </div>
  {NOTES}
</section>'''

S19 = '''
<section class="slide" id="s19" data-title="Visão: mensagem final">
  <div class="bg"></div><div class="veil"></div>
  <div class="wrap">
    <div class="barlabel rv" style="--d:80">Visão</div>
    <p class="msg" data-words>A segurança do paciente <span class="o">não é um programa isolado.</span> É a cultura que transforma a <span class="g">Atenção Primária</span>, conecta a <span class="g">Rede de Atenção à Saúde</span> e protege a vida de <span class="o">cada brasileiro.</span></p>
    <div class="qrs">
      <div class="qr rv" style="--d:820"><span class="qcap">Biblioteca Digital Conass</span><div class="qtile"><img src="data:image/svg+xml;base64,%%QRBIB%%" alt="QR code para a Biblioteca Digital do Conass"></div></div>
      <div class="qr rv" style="--d:960"><span class="qcap">Rede Negesp</span><div class="qtile"><img src="data:image/svg+xml;base64,%%QRNEG%%" alt="QR code para a Rede Negesp"></div></div>
    </div>
  </div>
  {NOTES}
</section>'''

S20 = '''
<section class="slide" id="s20" data-title="Encerramento">
  <div class="wrap">
    <div class="left">
      <div class="thanks rv" style="--d:100">Obrigada.</div>
    </div>
    <div class="right rv" style="--d:750">
      <div class="cphoto"><img src="data:image/jpeg;base64,%%CARLA%%" alt="Carla Ulhoa André"></div>
      <div class="cap">Contato</div>
      <div class="who"><b>Carla Ulhoa André</b><span>Assessora Técnica · Conselho Nacional de Secretários de Saúde</span></div>
      <div class="contacts">
        <span>carla.andre@conass.org.br</span>
        <span>linkedin.com/in/carlaulhoa</span>
        <span>@eucarlaulhoa</span>
      </div>
    </div>
  </div>
  <svg class="ecg" viewBox="0 0 1200 100" preserveAspectRatio="none" aria-hidden="true">
    <path d="M0 60 H320 L360 60 375 30 392 82 406 60 H560 L600 60 615 22 634 88 650 60 H840 L880 60 895 34 912 80 926 60 H1200"/>
  </svg>
  <div class="motto"><span>A força dos estados na garantia do direito à saúde</span></div>
  {NOTES}
</section>'''

SECTIONS_B = {'s11':S11,'s12':S12,'s13':S13,'s14':S14,'s15':S15,'s16':S16,'s17':S17,'s18':S18,'s19':S19,'s20':S20}
