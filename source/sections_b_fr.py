# -*- coding: utf-8 -*-
# Seções s11–s20 · versão FRANCÊS (fr-FR internacional). Estrutura idêntica ao PT; só o texto muda.

S11 = '''
<section class="slide" id="s11" data-title="Le Negesp en chiffres">
  <div class="wrap" style="padding:0">
    <div class="stage">
      <div class="holo rv" style="--d:300">
        <div class="table">
          <div class="ringsF"></div>
          <div class="sweep"></div>
          <svg class="brmap" id="mapMain" role="img" aria-label="Carte du Brésil montrant l'état de déploiement par unité fédérée"></svg>
          <div class="floor"></div>
        </div>
      </div>
      <div class="reading rv" style="--d:150">
        <div class="kick">Le Negesp en chiffres</div>
        <b id="ufcount" style="margin-top:.2em">26</b>
        <small>unités fédérées dans le mouvement national de déploiement</small>
      </div>
      <div class="legend">
        <div class="lg rv" style="--d:700"><i class="g"></i>États déployés : Negesp officiellement institué et opérationnel</div>
        <div class="lg st" data-st="1"><i class="o"></i>Rio Grande do Sul : en cours de déploiement, État en phase de structuration</div>
      </div>
    </div>
  </div>
  {NOTES}
</section>'''

S12 = '''
<section class="slide" id="s12" data-title="Le moteur du Negesp">
  <div class="wrap">
    <div class="kick rv" style="--d:60">Comment la stratégie devient action</div>
    <div class="line">
      <div class="side">
        <h5 class="rv" style="--d:200">Entrées</h5>
        <div class="io glass st">Orientations de la Politique nationale de qualité et de sécurité des patients</div>
        <div class="io glass st">Données probantes scientifiques</div>
        <div class="io glass st">Données locales</div>
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
          <span>Le processus<br>Negesp</span>
        </div>
        <div class="proc st">Diagnostic situationnel<small>matrice des forces, faiblesses, opportunités et menaces</small></div>
        <div class="proc st">Planification de l'amélioration<small>cycles planifier · faire · étudier · agir</small></div>
        <div class="proc st">Concertation intersectorielle<small>au-delà des murs du secrétariat</small></div>
      </div>
      <div class="side right">
        <h5 class="rv" style="--d:200">Résultats</h5>
        <div class="io glass st">Prise de décision assertive <span>avec le Centre d'intelligence stratégique</span></div>
        <div class="io glass st">Culture d'amélioration continue</div>
        <div class="io glass st">Un environnement de soins sûrs dans l'ensemble du réseau de soins de santé</div>
      </div>
    </div>
  </div>
  {NOTES}
</section>'''

S13 = '''
<section class="slide" id="s13" data-title="Les couches de gouvernance">
  <div class="wrap">
    <div class="kick rv" style="--d:60">De l'équipe technique au réseau national</div>
    <div class="orb5 rv" style="--d:220" id="orb5">
      <div class="oring"></div>
      <div class="oring2"></div>
      <div class="ocore"><span></span></div>
      <div class="onode st k1" data-st="4">
        <button type="button" class="obtn"><i>1</i></button>
        <div class="olabel">Réseau national et partenaires externes</div>
        <div class="ocard"><h5><i>1</i>Réseau national et partenaires externes</h5><p>la concertation systémique, coordonnée par le Conseil national des secrétaires à la santé.</p>
          <div class="orel"><button type="button" data-goto="1">Negesp de l'État</button></div></div>
      </div>
      <div class="onode st k2" data-st="3">
        <button type="button" class="obtn"><i>2</i></button>
        <div class="olabel">Negesp de l'État</div>
        <div class="ocard"><h5><i>2</i>Negesp de l'État</h5><p>la structure de gouvernance consolidée dans l'État.</p>
          <div class="orel"><button type="button" data-goto="0">Réseau national et partenaires externes</button><button type="button" data-goto="2">Comité consultatif</button></div></div>
      </div>
      <div class="onode st k3" data-st="2">
        <button type="button" class="obtn"><i>3</i></button>
        <div class="olabel">Comité consultatif</div>
        <div class="ocard"><h5><i>3</i>Comité consultatif</h5><p>l'intégration avec les départements du secrétariat à la santé de l'État.</p>
          <div class="orel"><button type="button" data-goto="1">Negesp de l'État</button><button type="button" data-goto="3">Équipe technique multiprofessionnelle</button></div></div>
      </div>
      <div class="onode st k4" data-st="1">
        <button type="button" class="obtn"><i>4</i></button>
        <div class="olabel">Équipe technique multiprofessionnelle</div>
        <div class="ocard"><h5><i>4</i>Équipe technique multiprofessionnelle</h5><p>la base d'opération technique, au sein du secrétariat de l'État.</p>
          <div class="orel"><button type="button" data-goto="2">Comité consultatif</button></div></div>
      </div>
    </div>
    <i class="st" data-st="5" aria-hidden="true" style="display:none"></i>
    <div class="orbsummary" aria-hidden="true">
      <div class="oscard k1"><span class="osn">1</span><b>Réseau national et partenaires externes</b><p>la concertation systémique, coordonnée par le Conseil national des secrétaires à la santé.</p></div>
      <div class="oscard k2"><span class="osn">2</span><b>Negesp de l'État</b><p>la structure de gouvernance consolidée dans l'État.</p></div>
      <div class="oscard k3"><span class="osn">3</span><b>Comité consultatif</b><p>l'intégration avec les départements du secrétariat à la santé de l'État.</p></div>
      <div class="oscard k4"><span class="osn">4</span><b>Équipe technique multiprofessionnelle</b><p>la base d'opération technique, au sein du secrétariat de l'État.</p></div>
    </div>
    <div class="orbprint"><div><b>1 · Réseau national et partenaires externes</b><span>la concertation systémique, coordonnée par le Conseil national des secrétaires à la santé.</span></div><div><b>2 · Negesp de l'État</b><span>la structure de gouvernance consolidée dans l'État.</span></div><div><b>3 · Comité consultatif</b><span>l'intégration avec les départements du secrétariat à la santé de l'État.</span></div><div><b>4 · Équipe technique multiprofessionnelle</b><span>la base d'opération technique, au sein du secrétariat de l'État.</span></div></div>
  </div>
  {NOTES}
</section>'''

S14 = '''
<section class="slide" id="s14" data-title="Le comité consultatif de l'intérieur">
  <div class="wrap">
    <div class="kick rv" style="--d:60">Le moteur de l'intégration interne</div>
    <h2 class="title rv" style="--d:180">Le <em>Comité consultatif</em> est une instance collégiale à caractère technique et consultatif qui appuie le Negesp dans la gouvernance, la planification et la prise de décision.</h2>
    <div class="tri">
      <div class="tcol fn glass st"><h4><i class="mk g"></i>Fonction centrale</h4><ul>
        <li>Réunir différents domaines stratégiques du secrétariat à la santé de l'État et des partenaires pertinents.</li>
        <li>Garantir que les décisions du Negesp soient intégrées, fondées sur des données probantes et alignées sur les besoins du réseau de soins de santé.</li>
      </ul></div>
      <div class="tcol atr glass st"><h4><i class="mk o"></i>Principales attributions</h4><ul>
        <li>Conseiller techniquement le Negesp dans la définition des priorités stratégiques.</li>
        <li>Contribuer à l'élaboration, à la mise en œuvre et au suivi du plan opérationnel de l'État.</li>
        <li>Analyser les indicateurs, les événements indésirables et les résultats de qualité et de sécurité des patients.</li>
        <li>Proposer des stratégies d'amélioration et appuyer la gestion des risques.</li>
        <li>Favoriser l'intégration entre les domaines du secrétariat et les autres institutions partenaires.</li>
        <li>Appuyer la mise en œuvre de la Politique nationale de qualité et de sécurité des patients à l'échelle de l'État.</li>
        <li>Renforcer la concertation entre l'État, les municipalités, les services de santé, les établissements d'enseignement et les organes de contrôle, le cas échéant.</li>
      </ul></div>
      <div class="tcol comp glass st"><h4><i class="mk g2"></i>Composition suggérée</h4><p class="intro">Elle peut réunir des représentants de domaines stratégiques du secrétariat de l'État, tels que :</p><ul>
        <li>Soins de santé primaires</li>
        <li>Soins spécialisés et hospitaliers</li>
        <li>Surveillance de la santé</li>
        <li>Régulation</li>
        <li>Planification</li>
        <li>Gestion de la qualité</li>
        <li>Formation continue</li>
        <li>Santé numérique et information</li>
        <li>Assistance pharmaceutique</li>
        <li>Audit, évaluation et suivi</li>
        <li>Ombudsman</li>
        <li>École de santé publique, le cas échéant</li>
      </ul></div>
    </div>
    <p class="foot rv" style="--d:900">Participation élargie, avec des <b>représentants externes invités</b> selon l'ordre du jour.</p>
  </div>
  {NOTES}
</section>'''

S15 = '''
<section class="slide" id="s15" data-title="La dynamique au secrétariat">
  <div class="wrap">
    <div class="kick rv" style="--d:60">Ce qui change en pratique</div>
    <h2 class="title rv" style="--d:180">De l'information dispersée à l'<em>action intersectorielle</em></h2>
    <div class="climb">
      <svg class="path" aria-hidden="true"></svg>
      <div class="result rv" style="--d:1300"><span class="badge">Qualité et sécurité des patients transversales à toute la gestion</span></div>
      <div class="stepc glass st"><span class="ord">01</span><h5>Entrée</h5><b>Partage</b><p>Les informations, indicateurs et données probantes autrefois dispersés entre les départements se mettent à circuler.</p></div>
      <div class="stepc glass st"><span class="ord">02</span><h5>Traitement</h5><b>Analyse</b><p>Les risques prioritaires sont identifiés et analysés de façon transversale pour la haute direction de l'État.</p></div>
      <div class="stepc glass st"><span class="ord">03</span><h5>Sortie</h5><b>Action intersectorielle</b><p>Des plans d'action coordonnés, avec l'élaboration et le suivi du plan opérationnel de la Politique nationale.</p></div>
    </div>
  </div>
  {NOTES}
</section>'''

S16 = '''
<section class="slide" id="s16" data-title="Le réseau national collaboratif">
  <div class="wrap">
    <div class="kick rv" style="--d:60">Aucun État n'avance seul</div>
    <h2 class="title rv" style="--d:180">Un réseau national <em>collaboratif</em>, coordonné par le Conseil</h2>
    <div class="stage">
      <div class="netmap rv" style="--d:340"><svg class="brmap" id="mapNet" role="img" aria-label="Carte du Brésil avec des connexions entre les États à partir de Brasília"></svg></div>
      <div class="vb glass st L" style="left:17%;top:22%"><b>Partager</b><span>les expériences réussies entre les États.</span></div>
      <div class="vb glass st L" style="left:13%;top:50%"><b>Suivre</b><span>les indicateurs des noyaux des États.</span></div>
      <div class="vb glass st L" style="left:17%;top:78%"><b>Produire</b><span>des solutions collaboratives.</span></div>
      <div class="vb glass st R" style="left:83%;top:22%"><b>Développer</b><span>des projets stratégiques intégrés.</span></div>
      <div class="vb glass st R" style="left:87%;top:50%"><b>Promouvoir</b><span>l'apprentissage mutuel.</span></div>
      <div class="vb glass st R" style="left:83%;top:78%"><b>Appuyer</b><span>la mise en œuvre continue de la Politique nationale.</span></div>
    </div>
  </div>
  {NOTES}
</section>'''

S17 = '''
<section class="slide" id="s17" data-title="Au-delà des murs">
  <div class="wrap">
    <div class="kick rv" style="--d:60">Le pont entre la gestion, le savoir et la société</div>
    <h2 class="title rv" style="--d:180">La sécurité des patients exige une concertation <em>au-delà des murs</em> du secrétariat</h2>
    <div class="fanstage">
      <svg class="rays" aria-hidden="true"></svg>
      <div class="hub rv" style="--d:400" id="fanHub">Negesp</div>
      <div class="qd glass st" style="left:46%;top:11%"><h4>Science et <em>innovation</em></h4><p>Universités, centres de recherche et hôpitaux universitaires.</p></div>
      <div class="qd glass st" style="left:56%;top:37%"><h4>Éthique et <em>pratique</em></h4><p>Ordres professionnels, sociétés savantes et écoles de santé publique.</p></div>
      <div class="qd glass st" style="left:56%;top:63%"><h4>Contrôle <em>institutionnel</em></h4><p>Ministère public et cours des comptes.</p></div>
      <div class="qd glass st" style="left:46%;top:89%"><h4>Alignement <em>mondial</em></h4><p>Organismes nationaux et internationaux.</p></div>
    </div>
  </div>
  {NOTES}
</section>'''

S18 = '''
<section class="slide" id="s18" data-title="L'équation de valeur">
  <div class="wrap">
    <div class="kick center rv" style="--d:60">L'équation de valeur du Negesp</div>
    <div class="eqline">
      <div class="term a st"><h4>Relier</h4></div>
      <div class="op st">+</div>
      <div class="term b st"><h4>Produire</h4></div>
      <div class="op st">=</div>
      <div class="term c st"><h4>Livrer</h4></div>
    </div>
    <div class="caps">
      <div class="cap a st">Gestion, soins, surveillance, enseignement et contrôle social.</div>
      <div class="cap b st">Données, données probantes, apprentissage et amélioration continue.</div>
      <div class="cap c st">Gouvernance, décisions éclairées et résultats en santé.</div>
    </div>
  </div>
  {NOTES}
</section>'''

S19 = '''
<section class="slide" id="s19" data-title="Vision : message final">
  <div class="bg"></div><div class="veil"></div>
  <div class="wrap">
    <div class="barlabel rv" style="--d:80">Vision</div>
    <p class="msg" data-words>La sécurité des patients <span class="o">n'est pas un programme isolé.</span> C'est la culture qui transforme les <span class="g">soins de santé primaires</span>, relie le <span class="g">réseau de soins de santé</span> et protège la vie de <span class="o">chaque Brésilien.</span></p>
    <div class="qrs">
      <div class="qr rv" style="--d:820"><span class="qcap">Bibliothèque numérique du Conass</span><div class="qtile"><img src="data:image/svg+xml;base64,%%QRBIB%%" alt="Code QR vers la Bibliothèque numérique du Conass"></div></div>
      <div class="qr rv" style="--d:960"><span class="qcap">Réseau Negesp</span><div class="qtile"><img src="data:image/svg+xml;base64,%%QRNEG%%" alt="Code QR vers le Réseau Negesp"></div></div>
    </div>
  </div>
  {NOTES}
</section>'''

S20 = '''
<section class="slide" id="s20" data-title="Clôture">
  <div class="wrap">
    <div class="left">
      <div class="thanks rv" style="--d:100">Merci !</div>
    </div>
    <div class="right rv" style="--d:750">
      <div class="cphoto"><img src="data:image/jpeg;base64,%%CARLA%%" alt="Carla Ulhoa André"></div>
      <div class="cap">Contact</div>
      <div class="who"><b>Carla Ulhoa André</b><span>Conseillère technique · Conseil national des secrétaires à la santé</span></div>
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
  <div class="motto"><span>La force des États dans la garantie du droit à la santé</span></div>
  {NOTES}
</section>'''

SECTIONS_B_FR = {'s11':S11,'s12':S12,'s13':S13,'s14':S14,'s15':S15,'s16':S16,'s17':S17,'s18':S18,'s19':S19,'s20':S20}
