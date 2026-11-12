import json
T = json.load(open('donnees/textes.json'))
R = lambda s: f'<span class="ref">§ {s}</span>'

essentiel = {
 "hero": {"title": "Socrate : la raison contre l’opinion",
          "text": "Un Athénien qui n’a rien écrit, condamné à mort en –399, et qui refuse de s’évader. Son idée-force : <strong style=\"color:inherit;text-decoration:underline\">la sagesse commence quand on sait qu’on ne sait pas</strong>, et la raison, pas la foule, doit guider nos actes."},
 "sections": [
  {"title": "Qui est Socrate ?", "html":
   "<p>Le philosophe le plus connu… et le paradoxe : <strong>il n’a jamais rien écrit</strong>. Pour lui, la philosophie se fait <strong>en conversation, en dialogue</strong>, pas par la lecture. On le connaît surtout par <strong>Platon</strong>, son élève (et aussi par Xénophon). Les dialogues de jeunesse de Platon seraient les plus fidèles à Socrate ; plus tard, c’est la philosophie de Platon lui-même qui apparaît.</p>"
   "<ul><li><strong>Un Athénien modeste</strong> : né vers –470 à Athènes, ni riche ni noble, ni pauvre. Père sculpteur, mère sage-femme.</li>"
   "<li><strong>Un soldat courageux</strong> : hoplite (fantassin lourdement armé qui payait son propre équipement), décrit comme brave et endurant.</li>"
   "<li><strong>Marié à Xanthippe</strong>, père de trois enfants. La réputation de « femme difficile » de Xanthippe n’est qu’une rumeur.</li>"
   "<li><strong>Laid… selon les Grecs</strong> : nez écrasé. Pour eux, un beau corps révèle une belle âme ; Socrate oblige à regarder au-delà de l’apparence.</li></ul>"
   "<p class=\"quote\">Comme sa mère aidait les femmes à accoucher des enfants, lui aide les esprits à « accoucher » de leurs idées : c’est la maïeutique.</p>"},
  {"title": "Deux refus qui annoncent le Criton", "html":
   "<p><strong>Le procès des généraux (–406)</strong> : après une victoire navale, des généraux n’ont pas secouru des marins naufragés. La foule en colère veut les juger <strong>en bloc</strong>, contre la loi qui exige un jugement individuel. Membre du conseil, Socrate est <strong>le seul</strong> à exiger le respect de la loi.</p>"
   "<p><strong>Les Trente Tyrans (–404)</strong> : après la défaite contre Sparte, un petit groupe dirigé par <strong>Critias</strong> (un ancien proche de Socrate) fait régner la terreur. On ordonne à Socrate d’aller arrêter <strong>Léon de Salamine</strong> pour qu’il soit exécuté. Il refuse, au risque de sa vie, car l’ordre est injuste.</p>"
   "<p class=\"quote\">À retenir : Socrate agit comme il pense, même seul contre tous, même contre la foule ou l’autorité, et même quand c’est dangereux.</p>"},
  {"title": "Le procès de –399", "html":
   "<p><strong>Le contexte</strong> : Athènes sort de la longue guerre contre Sparte et du règne des Trente ; la démocratie vient d’être rétablie et reste fragile. Un homme qui remet tout en question dérange. Plusieurs anciens amis de Socrate ont « mal tourné » (Critias), on le confond avec les sophistes, et <strong>Aristophane</strong> le caricature dans <em>Les Nuées</em> (un vieux fou la tête dans les nuages).</p>"
   "<p><strong>Trois accusations</strong> :</p><ul><li><strong>Impiété</strong> : ne pas respecter les dieux de la cité (la religion est publique : offenser les dieux met toute la cité en danger).</li><li><strong>Introduire de nouvelles divinités</strong> : il parlait d’une petite voix intérieure (son <em>daïmon</em>) qui le guidait.</li><li><strong>Corrompre la jeunesse</strong> : les jeunes le suivaient parce qu’il remettait en question l’autorité, les parents, les traditions.</li></ul>"
   "<p><strong>Trois accusateurs, trois milieux</strong> : <strong>Mélétos</strong> (poètes et écrivains), <strong>Anytos</strong> (artisans et marchands), <strong>Lycon</strong> (politiciens et orateurs) : une grande partie de la société.</p>"
   "<p><strong>Les votes</strong> (≈ 500 citoyens jurés) : <strong>281 contre 220</strong> pour la culpabilité, une faible majorité. Socrate propose alors comme « peine »… d’être nourri aux frais de la cité. L’ironie passe mal : <strong>368 contre 133</strong> pour la mort.</p>"
   "<p><strong>L’exécution</strong> : retardée d’<strong>environ un mois</strong>, car on attend le retour du navire sacré envoyé à Délos en l’honneur d’Apollon. Ses amis le visitent en prison et veulent le faire évader (c’est le <em>Criton</em>). Il refuse et boit la <strong>ciguë</strong>, un poison qui paralyse peu à peu le corps.</p>"},
  {"title": "L’enseignement de Socrate", "html":
   "<p>Bien vivre = utiliser sa raison pour savoir ce qui est bien, car savoir ce qui est bien rend heureux. Quatre idées qui s’enchaînent :</p>"
   "<ol class=\"steps\"><li><strong>Connais-toi toi-même</strong>. Inscription du temple d’Apollon à Delphes (« souviens-toi que tu es mortel, pas un dieu »). Socrate en fait le cœur de sa philosophie : avant de prétendre connaître le monde, sache ce que tu sais… et ce que tu ignores.</li>"
   "<li><strong>La raison fonde la morale</strong>. Pas la religion ni la tradition : la raison, présente en chaque être humain quelle que soit son origine, permet une morale universelle et objective.</li>"
   "<li><strong>Nul n’est méchant volontairement</strong>. Le mal vient de l’ignorance : le voleur vole parce qu’il croit que cela le rendra heureux. Qui connaît vraiment le bien le fait. D’où la solution : non pas punir, mais <strong>éduquer</strong>.</li>"
   "<li><strong>Bonheur = vertu</strong>. Tout le monde veut être heureux ; on ne l’est pas par l’argent mais par la vertu : être sage, courageux et juste.</li></ol>"
   "<p class=\"quote\">Je me connais et je réfléchis → ma raison découvre le bien → si je sais le bien, je le fais → en faisant le bien, je suis heureux.</p>"},
  {"title": "L’Apologie : l’enquête de Socrate", "html":
   "<p><em>Apologia</em> = <strong>défense</strong>, pas éloge : c’est le plaidoyer de Socrate devant ses juges, écrit par Platon qui y assistait. Trois temps : il répond aux accusations (notre extrait), il propose sa peine, il commente sa condamnation.</p>"
   "<p><strong>Un procès qui dépasse un homme</strong> : comme le procès de <strong>Galilée</strong> (1633) opposait la science à l’autorité religieuse, celui de Socrate oppose deux visions de la société : une population qui veut protéger ses traditions, ses croyances et sa sécurité, et un homme qui pousse chacun à penser par lui-même.</p>"
   "<ul><li><strong>Religion</strong> : à Athènes, elle est publique, c’est le ciment de la cité (règles, fêtes, calendrier). Offenser les dieux met toute la cité en danger (défaite, épidémie…).</li>"
   "<li><strong>Science</strong> : chercher des causes naturelles plutôt que la volonté des dieux est très mal vu. Mélétos attribue à Socrate l’idée que le Soleil est une pierre et la Lune une terre, idée qui est en fait d’<strong>Anaxagore</strong>. Socrate n’est pas un scientifique : la science cherche des causes, la philosophie cherche le <strong>sens</strong>.</li>"
   "<li><strong>Le « taon »</strong> : Socrate se compare à cette grosse mouche qui pique un cheval endormi et paresseux (Athènes) pour le réveiller. Sa mission : poser des questions dérangeantes jusqu’à ce que ses concitoyens se mettent à philosopher, et exiger que les valeurs se justifient.</li></ul>"
   "<p><strong>L’oracle</strong> : Chéréphon demande à la Pythie de Delphes s’il existe un homme plus sage que Socrate : « aucun ». Socrate, qui se sait sans sagesse, veut comprendre et enquête auprès des <strong>politiques</strong>, des <strong>poètes</strong> et des <strong>artisans</strong>. Tous croient savoir ce qu’ils ne savent pas.</p>"
   "<p class=\"quote\">« Le plus sage d’entre vous, c’est celui qui, comme Socrate, reconnaît que sa sagesse n’est rien. » (§ 8)</p>"},
  {"title": "La discussion rationnelle : ironie et maïeutique", "html":
   "<p><strong>Trois états</strong> :</p><ul><li><strong>Double ignorance</strong> : j’ignore que j’ignore. On ne cherche pas, on croit déjà savoir.</li><li><strong>Simple ignorance</strong> : je sais que j’ignore. Le doute ouvre la recherche.</li><li><strong>Connaissance</strong> : je sais, et je sais pourquoi.</li></ul>"
   "<p><strong>L’ironie</strong> (pour passer de la double à la simple ignorance) : pour celui qui croit tout savoir. Socrate fait l’ignorant et pose des questions qui font apparaître les contradictions. But : dégonfler la prétention et faire naître le doute.</p>"
   "<p><strong>La maïeutique</strong> (pour passer de la simple ignorance à la connaissance) : pour celui qui sait qu’il ignore et veut chercher. Des questions qui l’aident à trouver par lui-même. But : « accoucher » une vérité que sa raison porte déjà. On cherche alors à définir rigoureusement les mots (justice, courage, amitié…).</p>"},
  {"title": "Le Criton : faut-il s’évader ?", "html":
   "<p>À l’aube, dans la prison. Criton veille Socrate qui dort paisiblement. Le navire de Délos arrive : l’exécution est imminente. Tout est prêt pour l’évasion, il faut décider avant la nuit.</p>"
   "<ul><li><strong>Partie 1 (§ 1-34)</strong> : les arguments de Criton (perdre un ami, sa réputation, l’argent n’est pas un problème, les enfants, la honte…). Socrate : l’opinion de la foule ne compte pas.</li>"
   "<li><strong>Partie 2 (§ 35-84)</strong> : les principes : n’écouter que la raison ; seule compte l’opinion du compétent ; l’important n’est pas de vivre mais de <strong>bien vivre</strong> ; ne jamais commettre l’injustice, même en réponse à une injustice ; tenir ses engagements justes.</li>"
   "<li><strong>Partie 3 (§ 85-101)</strong> : les <strong>Lois</strong> d’Athènes prennent la parole : s’évader, ce serait les détruire et trahir le contrat qu’il a passé avec elles en vivant 70 ans à Athènes.</li></ul>"
   "<p><strong>L’argument reconstruit</strong> :</p><ol class=\"steps\"><li>Il ne faut jamais commettre d’injustice, même pour répondre à une injustice.</li><li>S’évader serait commettre une injustice (détruire les lois, rompre un engagement juste).</li><li>Donc Socrate ne doit pas s’évader.</li></ol>"
   "<p class=\"quote\">« Tu partiras condamné injustement, non par nous, les lois, mais par les hommes. » (§ 98)</p>"},
  {"title": "Pour réfléchir et disserter", "html":
   "<p><strong>Question</strong> : les citoyens d’une démocratie doivent-ils quelque chose à leur pays, même quand ses lois les traitent injustement ?</p>"
   "<ul><li><strong>Devoir quoi ?</strong> Obéir aux lois, payer ses impôts, voter, défendre son pays… ou de la loyauté ?</li><li><strong>À qui ?</strong> Aux lois, au gouvernement en place, ou à la communauté des citoyens ?</li><li><strong>Même dans l’injustice ?</strong> C’est la situation de Socrate.</li></ul>"
   "<p><strong>Juger l’argument</strong> : est-il valide ? Quelle prémisse est la plus fragile (souvent la 2<sup>e</sup> : un engagement « tacite » oblige-t-il vraiment ?) ? Une loi appliquée injustement est-elle encore juste ?</p>"
   "<p><strong>Pistes</strong> : Socrate est-il sage ou fou de refuser l’évasion ? Vaut-il la peine de mourir pour ses idées ?</p>"
   "<p class=\"quote\">À emporter : 1. La sagesse commence par la conscience de son ignorance. 2. Ironie puis maïeutique : du doute à la recherche du vrai. 3. Socrate préfère mourir que commettre une injustice.</p>"},
 ],
 "glossary": [
  {"term": "Maïeutique", "def": "Du grec « art d’accoucher ». Art de poser des questions pour aider quelqu’un à trouver la vérité par lui-même."},
  {"term": "Ironie socratique", "def": "Feindre l’ignorance et questionner pour révéler les contradictions de celui qui croit savoir."},
  {"term": "Double ignorance", "def": "Ignorer qu’on ignore : croire savoir ce qu’on ne sait pas."},
  {"term": "Apologie", "def": "Du grec <em>apologia</em> : défense, plaidoyer (pas un éloge)."},
  {"term": "Oracle / Pythie", "def": "Réponse d’un dieu à une question ; à Delphes, la Pythie transmet la réponse d’Apollon."},
  {"term": "Sophistes", "def": "Maîtres de rhétorique payés pour enseigner à défendre n’importe quelle thèse. Socrate s’y oppose."},
  {"term": "Ciguë", "def": "Poison qui paralyse progressivement le corps ; mode d’exécution de Socrate."},
  {"term": "Hoplite", "def": "Fantassin grec lourdement armé, qui achetait lui-même son équipement."},
  {"term": "Sycophantes", "def": "Délateurs professionnels qui accusaient les gens en justice pour leur soutirer de l’argent."},
  {"term": "Vertu", "def": "Excellence morale : être sage, courageux et juste. Pour Socrate, la seule voie vers le bonheur."},
 ],
}

apologie_corr = [
 {"title": "Étape 1 · Le point de départ", "html":
  "<p><strong>L’événement</strong> : Chéréphon, ami d’enfance de Socrate, demande à l’oracle de Delphes s’il existe un homme plus sage que Socrate ; la Pythie répond qu’il n’y en a aucun." + R("3") + "</p>"
  "<p><strong>Pourquoi la surprise ?</strong> Socrate sait qu’il n’a « aucune sagesse, ni petite ni grande », mais un dieu ne peut pas mentir." + R("4") + "</p>"
  "<p><strong>Ce qu’il cherche</strong> : comprendre le sens de l’oracle, et d’abord le « confondre » en trouvant quelqu’un de plus sage que lui." + R("4") + "</p>"},
 {"title": "Étape 2 · Le tableau de l’enquête", "html":
  "<table class=\"ctable\"><tr><th>Qui</th><th>Ce qu’ils savent / croient savoir</th><th>Conclusion de Socrate</th></tr>"
  "<tr><td>Les politiques" + R("4-5") + "</td><td><b>Savent</b> : rien de « fort merveilleux ».<br><b>Croient</b> : être sages ; ils passent pour sages aux yeux de tous, surtout aux leurs.</td><td>« Je suis plus sage que cet homme » : lui croit savoir sans savoir, moi je ne crois pas savoir. Les plus vantés sont les moins sages. Il se fait des ennemis.</td></tr>"
  "<tr><td>Les poètes" + R("6") + "</td><td><b>Savent</b> : composer de belles œuvres, par inspiration, comme les devins.<br><b>Croient</b> : comprendre ce qu’ils disent, et être les plus sages sur tout le reste.</td><td>Ce n’est pas la raison qui les guide ; n’importe qui explique mieux leurs poèmes qu’eux. Socrate leur est supérieur pour la même raison qu’aux politiques.</td></tr>"
  "<tr><td>Les artisans" + R("7") + "</td><td><b>Savent</b> : vraiment leur métier, « mille secrets » que Socrate ignore.<br><b>Croient</b> : savoir aussi « les choses les plus importantes ».</td><td>Leur présomption gâte leur habileté. Socrate préfère être comme il est : sans leur savoir-faire, mais sans leur ignorance.</td></tr></table>"},
 {"title": "Étape 3 · Thème, thèse, arguments", "html":
  "<p><strong>Thème</strong> : la sagesse humaine (et l’origine de la réputation de Socrate).</p>"
  "<p><strong>Thèse</strong> : la seule vraie sagesse humaine consiste à reconnaître son ignorance ; le plus sage n’est pas celui qui sait le plus, mais celui qui, comme Socrate, sait que sa sagesse n’est rien." + R("8") + "</p>"
  "<ol class=\"steps\"><li>Les politiques, réputés sages, croient savoir mais ne savent pas : Socrate est plus sage parce qu’il ne croit pas savoir ce qu’il ignore." + R("4") + "</li>"
  "<li>Les poètes créent par inspiration sans comprendre leurs œuvres, et se croient sages en tout : même défaut." + R("6") + "</li>"
  "<li>Les artisans ont un vrai savoir technique, mais se croient compétents sur les questions les plus importantes : leur prétention gâte leur savoir." + R("7") + "</li></ol>"
  "<p>Donc l’oracle se sert de Socrate comme exemple : la sagesse humaine « n’est pas grand-chose », et seule la conscience de cette limite rend sage." + R("8") + "</p>"},
 {"title": "Pour aller plus loin", "html":
  "<p>Sans croire aux oracles, la thèse tient encore : elle repose sur l’<strong>enquête</strong> elle-même. Socrate a examiné rationnellement, un par un, ceux qui prétendaient savoir, et a constaté partout le même écart entre ce qu’ils savent et ce qu’ils croient savoir. L’oracle n’est que le point de départ ; c’est l’examen par questions (la raison) qui prouve la thèse.</p>"},
]

criton_corr = [
 {"title": "Partie 1 · Les arguments de Criton (§ 1-34)", "html":
  "<p><strong>Thèse de Criton</strong> : Socrate doit s’évader cette nuit même.</p>"
  "<ol class=\"steps\"><li>Criton perdrait un ami irremplaçable." + R("26") + "</li>"
  "<li>Sa réputation : on croira qu’il a préféré son argent à son ami." + R("26") + "</li>"
  "<li>Il faut se soucier de l’opinion du grand nombre : elle peut faire « le plus grand mal » (la preuve : la condamnation)." + R("28") + "</li>"
  "<li>Les risques (sycophantes, argent) ne doivent pas l’arrêter : l’évasion coûte peu, Criton, Simmias et Cébès sont prêts à payer." + R("30-32") + "</li>"
  "<li>Il sera bien accueilli à l’étranger, en Thessalie." + R("32") + "</li>"
  "<li>Se livrer, c’est faire ce que souhaitent ses ennemis : une faute." + R("33") + "</li>"
  "<li>Il trahit ses fils, qui seront orphelins." + R("33") + "</li>"
  "<li>Honte et lâcheté pour lui et ses amis ; il faut agir vite." + R("34") + "</li></ol>"
  "<p><strong>Première réponse de Socrate</strong> : pourquoi se soucier de l’opinion du « vulgaire » ? Les gens sensés sauront la vérité" + R("27") + " ; la foule ne peut rendre ni sage ni insensé, elle agit au hasard." + R("29") + "</p>"
  "<p class=\"quote\">« Peut-il y avoir de réputation plus honteuse que de passer pour être plus attaché à l’argent qu’à ses amis ? » (§ 26)</p>"},
 {"title": "Partie 2 · Les principes de Socrate (§ 35-84)", "html":
  "<p><strong>Thèse</strong> : il faut décider par la seule raison, en restant fidèle à ses principes, et la seule question qui compte est : <strong>s’évader est-il juste ?</strong></p>"
  "<ol class=\"steps\"><li>N’écouter que la raison ; on ne renie pas ses principes parce qu’un malheur arrive." + R("35") + "</li>"
  "<li>Toutes les opinions ne se valent pas : seule compte celle du compétent. Exemple : le gymnaste écoute le médecin ou le pédotribe, pas la foule." + R("35-46") + "</li>"
  "<li>Écouter les incompétents ruine le corps ; de même, l’injustice ruine l’âme, plus précieuse que le corps." + R("47-60") + "</li>"
  "<li>Le plus important n’est pas de vivre, mais de <strong>bien vivre</strong> ; et bien vivre = vivre de façon belle et juste." + R("63-66") + "</li>"
  "<li>Il ne faut jamais commettre l’injustice, ni rendre le mal pour le mal, même quand on a subi une injustice." + R("71-81") + "</li>"
  "<li>Quand on a reconnu qu’une chose est juste, il faut la faire (tenir parole)." + R("83-84") + "</li></ol>"
  "<p><strong>Conclusion</strong> : argent, réputation, enfants sont des considérations « de la foule » ; seule compte la justice de l’évasion." + R("67") + "</p>"
  "<p class=\"quote\">« Le plus important n’est pas de vivre, mais de bien vivre. » (§ 63)</p>"},
 {"title": "Partie 3 · Les Lois prennent la parole (§ 85-101)", "html":
  "<p><strong>Thèse des Lois</strong> : s’évader serait une injustice, car ce serait détruire les lois et violer un engagement ; Socrate doit donc rester.</p>"
  "<ol class=\"steps\"><li>S’évader, c’est détruire les lois : un État ne peut subsister si les jugements n’ont aucune force." + R("87") + "</li>"
  "<li>Les Lois sont comme des parents : elles l’ont fait naître, nourri, éduqué. Il n’a pas les mêmes droits qu’elles ; la patrie est plus sacrée qu’un père ou une mère. Il faut la <strong>persuader ou obéir</strong>." + R("90") + "</li>"
  "<li>Le contrat tacite : chacun est libre de quitter Athènes ; celui qui reste s’engage à obéir. Désobéir le rend trois fois coupable." + R("92") + "</li>"
  "<li>Socrate s’est engagé plus que tout autre : 70 ans sans quitter la ville, des enfants à Athènes, et il a refusé de proposer l’exil au procès." + R("93-95") + "</li>"
  "<li>Les conséquences : ses amis risquent l’exil ou la ruine ; dans les cités bien gouvernées, il serait vu comme un corrupteur des lois et confirmerait le jugement ; en Thessalie, il serait ridicule et ses discours sur la vertu perdraient tout sens." + R("96-97") + "</li>"
  "<li>Ses enfants seront mieux élevés à Athènes par ses amis que comme étrangers en Thessalie." + R("97") + "</li>"
  "<li>Ne rien mettre au-dessus de la justice : mort, il sera victime des hommes et non des lois ; en fuyant, il rendrait l’injustice pour l’injustice." + R("98") + "</li></ol>"
  "<p><strong>Conclusion</strong> : Socrate reste et accepte la mort ; les responsables sont <strong>les hommes</strong> qui l’ont mal jugé, pas les lois." + R("98-101") + "</p>"
  "<p class=\"quote\">« Si tu pars aujourd’hui pour l’autre monde, tu partiras condamné injustement, non par nous, les lois, mais par les hommes. » (§ 98)</p>"},
 {"title": "Reconstruire et juger l’argument", "html":
  "<ol class=\"steps\"><li><strong>Prémisse 1</strong> : il ne faut jamais commettre d’injustice, même en réponse à une injustice." + R("71-81") + "</li>"
  "<li><strong>Prémisse 2</strong> : s’évader serait commettre une injustice (détruire les lois, rompre un engagement juste)." + R("87-95") + "</li>"
  "<li><strong>Conclusion</strong> : donc Socrate ne doit pas s’évader." + R("98-101") + "</li></ol>"
  "<p><strong>Valide ?</strong> Oui : si les deux prémisses sont vraies, la conclusion suit nécessairement.</p>"
  "<p><strong>Prémisse la plus fragile</strong> : la 2<sup>e</sup>. Rester dans un pays vaut-il vraiment un engagement ? Désobéir une fois détruit-il réellement toutes les lois ? Et une loi appliquée injustement est-elle encore juste ? (Socrate répond que les lois sont justes, ce sont les hommes qui ont mal jugé.)</p>"},
]

texts = [
 {"intro": "<p><b>Athènes, –399.</b> Socrate, environ 70 ans, se défend devant un tribunal populaire. Il explique que les vieilles rumeurs (savant qui étudie le ciel, rêveur ridicule des <em>Nuées</em>, sophiste payé) sont plus dangereuses que les accusations officielles.</p><p>Question de l’extrait : <b>pourquoi a-t-il une telle réputation et autant d’ennemis ?</b></p>",
  "source": "Platon, Apologie de Socrate, trad. Victor Cousin (domaine public).",
  "corrige": apologie_corr, "paras": T['apologie']},
 {"intro": "<p><b>Dans la prison, à l’aube.</b> L’exécution attend le retour du navire sacré envoyé à Délos. Criton annonce qu’il arrive : Socrate mourra demain. Tout est prêt pour l’évasion. Socrate veut d’abord réfléchir : <b>est-il juste de s’évader ?</b></p>",
  "source": "Platon, Criton, trad. Émile Chambry (domaine public).",
  "corrige": criton_corr, "paras": T['criton'],
  "parts": {"1": "Partie 1 · Les arguments de Criton", "35": "Partie 2 · Les principes de Socrate", "85": "Partie 3 · Les Lois prennent la parole"}},
]

cards = [
 {"tag": "Repère", "q": "Pourquoi Socrate est-il un paradoxe pour l’histoire de la philosophie ?", "a": "C’est le philosophe le plus célèbre, mais <strong>il n’a jamais rien écrit</strong> : pour lui, la philosophie se fait en dialogue. On le connaît surtout par Platon (et Xénophon)."},
 {"tag": "Repère", "q": "Quel métier exerçait la mère de Socrate, et quel lien avec sa méthode ?", "a": "Sage-femme. Socrate se dit « sage-femme des esprits » : il aide les gens à <strong>accoucher de leurs idées</strong>. C’est la <strong>maïeutique</strong>."},
 {"tag": "Repère", "q": "Que montre le fait que Socrate soit « laid » aux yeux des Grecs ?", "a": "Pour les Grecs, un beau corps révèle une belle âme. Socrate, laid mais vertueux, <strong>oblige à regarder au-delà des apparences</strong>."},
 {"tag": "Événement", "q": "Que fait Socrate lors du procès des généraux (–406) ?", "a": "La foule veut juger les généraux <strong>en bloc</strong>, contre la loi. Socrate est <strong>le seul</strong> à exiger le respect de la loi : un jugement individuel."},
 {"tag": "Événement", "q": "Quel ordre Socrate refuse-t-il sous les Trente Tyrans (–404) ?", "a": "Aller arrêter <strong>Léon de Salamine</strong> pour qu’il soit exécuté. Il refuse, au risque de mourir, plutôt que de commettre une injustice."},
 {"tag": "Procès", "q": "Quelles sont les trois accusations portées contre Socrate ?", "a": "1. <strong>Impiété</strong> envers les dieux de la cité<br>2. <strong>Introduction de nouvelles divinités</strong> (sa voix intérieure)<br>3. <strong>Corruption de la jeunesse</strong>"},
 {"tag": "Procès", "q": "Qui sont les trois accusateurs et quels milieux représentent-ils ?", "a": "<strong>Mélétos</strong> : poètes et écrivains<br><strong>Anytos</strong> : artisans et marchands<br><strong>Lycon</strong> : politiciens et orateurs"},
 {"tag": "Procès", "q": "Quels ont été les résultats des deux votes ?", "a": "Culpabilité : <strong>281 contre 220</strong> (faible majorité).<br>Peine de mort : <strong>368 contre 133</strong>, après que Socrate a ironiquement proposé d’être nourri aux frais de la cité."},
 {"tag": "Procès", "q": "Pourquoi l’exécution de Socrate a-t-elle été retardée d’environ un mois ?", "a": "On attendait le retour du <strong>navire sacré envoyé à Délos</strong> pour une fête d’Apollon : aucune exécution n’était permise avant."},
 {"tag": "Procès", "q": "Quelle pièce d’Aristophane a nui à la réputation de Socrate ?", "a": "<strong>Les Nuées</strong> : Socrate y est caricaturé en vieux rêveur ridicule, la tête dans les nuages."},
 {"tag": "Doctrine", "q": "« Connais-toi toi-même » : d’où vient la formule, et qu’en fait Socrate ?", "a": "Inscrite au temple d’Apollon à <strong>Delphes</strong> (« souviens-toi que tu es mortel »). Pour Socrate : avant de prétendre connaître le monde, <strong>sache ce que tu sais et ce que tu ignores</strong>."},
 {"tag": "Doctrine", "q": "Que signifie « Nul n’est méchant volontairement » ?", "a": "Le mal vient de l’<strong>ignorance</strong>, jamais de la méchanceté : qui connaît vraiment le bien le fait. La solution n’est donc pas de punir mais d’<strong>éduquer</strong>."},
 {"tag": "Doctrine", "q": "Sur quoi Socrate fonde-t-il la morale ?", "a": "Sur la <strong>raison</strong>, présente en chaque humain, et non sur la religion ou la tradition : elle permet une morale universelle."},
 {"tag": "Doctrine", "q": "Bonheur = ?", "a": "<strong>Vertu</strong>. On n’est pas heureux par l’argent mais en étant sage, courageux et juste."},
 {"tag": "Apologie", "q": "Que signifie le mot grec « apologia » ?", "a": "<strong>Défense</strong>, plaidoyer (et non éloge). C’est le discours de Socrate devant ses juges."},
 {"tag": "Apologie", "q": "Que répond l’oracle de Delphes à Chéréphon ?", "a": "Qu’<strong>aucun homme n’est plus sage que Socrate</strong>." + R("3")},
 {"tag": "Apologie", "q": "Quels trois groupes Socrate interroge-t-il, et dans quel ordre ?", "a": "Les <strong>politiques</strong>, puis les <strong>poètes</strong>, puis les <strong>artisans</strong>."},
 {"tag": "Apologie", "q": "Qu’est-ce que les artisans savent vraiment, et où est leur erreur ?", "a": "Ils maîtrisent vraiment leur métier. Mais ils croient aussi savoir « les choses les plus importantes » : cette <strong>présomption gâte leur habileté</strong>." + R("7")},
 {"tag": "Apologie", "q": "Selon Socrate, qu’est-ce qui guide les poètes ?", "a": "Non pas la raison, mais une <strong>inspiration</strong>, un enthousiasme comme celui des devins : ils disent de belles choses sans les comprendre." + R("6")},
 {"tag": "Apologie", "q": "Quelle est la thèse de l’extrait de l’Apologie ?", "a": "Le plus sage est celui qui, comme Socrate, <strong>reconnaît que sa sagesse n’est rien</strong> : la vraie sagesse humaine, c’est la conscience de son ignorance." + R("8")},
 {"tag": "Apologie", "q": "À quel animal Socrate se compare-t-il, et pourquoi ?", "a": "Au <strong>taon</strong>, une grosse mouche qui pique un cheval endormi (Athènes) pour le réveiller : il harcèle ses concitoyens de questions pour qu’ils se mettent à réfléchir."},
 {"tag": "Apologie", "q": "Quelle idée Mélétos attribue-t-il faussement à Socrate, et à qui appartient-elle ?", "a": "Que le Soleil est une pierre et la Lune une terre. C’est une idée d’<strong>Anaxagore</strong>, un des premiers penseurs scientifiques. Socrate répond qu’il s’intéresse aux humains, pas aux astres."},
 {"tag": "Apologie", "q": "Quelle différence le cours fait-il entre science et philosophie ?", "a": "La <strong>science</strong> cherche les causes naturelles des choses ; la <strong>philosophie</strong> cherche le <strong>sens</strong> (de la vie, des valeurs). Socrate utilise la raison, mais pour chercher le sens."},
 {"tag": "Apologie", "q": "Pourquoi compare-t-on le procès de Socrate à celui de Galilée ?", "a": "Dans les deux cas, le procès d’un homme met en jeu un conflit plus large : science contre autorité religieuse pour Galilée ; tradition et sécurité de la cité contre pensée critique pour Socrate."},
 {"tag": "Méthode", "q": "Double ignorance, simple ignorance, connaissance : définissez.", "a": "<strong>Double</strong> : j’ignore que j’ignore.<br><strong>Simple</strong> : je sais que j’ignore.<br><strong>Connaissance</strong> : je sais, et je sais pourquoi."},
 {"tag": "Méthode", "q": "L’ironie socratique : pour qui, comment, pourquoi ?", "a": "Pour celui qui <strong>croit tout savoir</strong>. Des questions qui font apparaître ses contradictions. But : dégonfler sa prétention et faire naître le doute."},
 {"tag": "Méthode", "q": "La maïeutique : pour qui, comment, pourquoi ?", "a": "Pour celui qui <strong>sait qu’il ignore</strong> et veut chercher. Des questions qui l’aident à trouver par lui-même. But : « accoucher » une vérité que sa raison porte déjà."},
 {"tag": "Criton", "q": "Citez trois arguments de Criton pour l’évasion.", "a": "Au choix : perdre un ami irremplaçable ; sa réputation (on le croira avare) ; l’opinion de la foule est dangereuse ; l’argent n’est pas un problème ; accueil en Thessalie ; ce serait faire le jeu des ennemis ; abandonner ses fils ; la honte." + R("26-34")},
 {"tag": "Criton", "q": "Quel exemple Socrate utilise-t-il pour montrer que seule compte l’opinion du compétent ?", "a": "Le <strong>gymnaste</strong> écoute le médecin ou l’entraîneur (pédotribe), pas la foule ; sinon il ruine son corps. De même, l’injustice ruine l’âme." + R("41-60")},
 {"tag": "Criton", "q": "Quel principe Socrate rappelle-t-il au § 63 ?", "a": "« Le plus important n’est pas de <strong>vivre</strong>, mais de <strong>bien vivre</strong>. »"},
 {"tag": "Criton", "q": "Peut-on répondre à une injustice par une injustice selon Socrate ?", "a": "<strong>Jamais</strong>. Rendre le mal pour le mal est injuste, quoi qu’on nous ait fait." + R("71-81")},
 {"tag": "Criton", "q": "Pourquoi les Lois disent-elles que Socrate a passé un « contrat » avec elles ?", "a": "Tout Athénien est libre de partir ; en restant <strong>70 ans</strong> à Athènes (et en y ayant ses enfants), Socrate s’est engagé à obéir : <strong>persuader ou obéir</strong>." + R("92-95")},
 {"tag": "Criton", "q": "Selon les Lois, qui serait responsable de la mort de Socrate ?", "a": "<strong>Les hommes</strong> qui l’ont mal jugé, pas les lois." + R("98")},
 {"tag": "Criton", "q": "Reconstruisez l’argument de Socrate en deux prémisses et une conclusion.", "a": "P1 : il ne faut jamais commettre d’injustice.<br>P2 : s’évader serait une injustice (détruire les lois, rompre un engagement).<br>C : donc il ne faut pas s’évader."},
]

quiz = [
 {"q": "Par qui connaissons-nous surtout la pensée de Socrate ?", "options": ["Par ses propres livres", "Par Platon, son élève", "Par Aristote", "Par Aristophane"], "answer": 1, "explain": "Socrate n’a rien écrit. Platon, son élève, est notre source principale (avec Xénophon). Aristophane ne fait que le caricaturer."},
 {"q": "Que signifie littéralement « maïeutique » ?", "options": ["L’art de discuter", "L’art d’accoucher", "L’amour de la sagesse", "L’art de convaincre"], "answer": 1, "explain": "Comme sa mère sage-femme, Socrate aide les esprits à « accoucher » des idées qu’ils portent déjà."},
 {"q": "Sous les Trente Tyrans, Socrate refuse…", "options": ["de payer une amende", "de quitter Athènes", "d’aller arrêter Léon de Salamine", "de juger les généraux"], "answer": 2, "explain": "Il refuse d’arrêter un homme condamné injustement, au risque d’être lui-même exécuté."},
 {"q": "Lequel n’est PAS un chef d’accusation contre Socrate ?", "options": ["Corrompre la jeunesse", "Introduire de nouvelles divinités", "Trahir Athènes au profit de Sparte", "Ne pas respecter les dieux de la cité"], "answer": 2, "explain": "Les trois accusations sont : impiété, nouvelles divinités, corruption de la jeunesse."},
 {"q": "Quel accusateur représente les artisans et les marchands ?", "options": ["Mélétos", "Anytos", "Lycon", "Criton"], "answer": 1, "explain": "Mélétos : poètes ; Anytos : artisans et marchands ; Lycon : politiciens et orateurs. Criton, lui, est l’ami de Socrate."},
 {"q": "Pourquoi le second vote (pour la mort) a-t-il été plus sévère que le premier ?", "options": ["De nouveaux jurés sont arrivés", "Socrate a ironiquement proposé d’être nourri aux frais de la cité", "Socrate a avoué", "Criton a témoigné contre lui"], "answer": 1, "explain": "Cette provocation a irrité les jurés : on passe de 281/220 à 368/133."},
 {"q": "« Nul n’est méchant volontairement » signifie que le mal vient…", "options": ["de la nature humaine", "des dieux", "de l’ignorance", "de la pauvreté"], "answer": 2, "explain": "Qui connaît vraiment le bien le fait. D’où l’importance d’éduquer plutôt que de punir."},
 {"q": "Pour Socrate, le bonheur s’obtient par…", "options": ["la richesse", "la vertu", "le plaisir", "la gloire"], "answer": 1, "explain": "Bonheur = vertu : être sage, courageux et juste."},
 {"q": "Dans l’Apologie, que cherche d’abord à faire Socrate après l’oracle ?", "options": ["Le faire connaître à tous", "Le réfuter en trouvant plus sage que lui", "Fonder une école", "Se rendre à Delphes"], "answer": 1, "explain": "Il veut « confondre l’oracle » (§ 4) en trouvant quelqu’un de plus sage, et découvre au contraire que tous croient savoir sans savoir."},
 {"q": "Qu’est-ce que les artisans savent VRAIMENT selon Socrate ?", "options": ["Rien du tout", "Leur métier, leur technique", "Ce qu’est la justice", "Interpréter les poèmes"], "answer": 1, "explain": "Ils ont un vrai savoir technique, mais se croient aussi compétents sur les questions les plus importantes (§ 7)."},
 {"q": "Dans l’Apologie, Socrate se compare à…", "options": ["un berger", "un taon qui pique un cheval endormi", "un médecin", "un soldat à son poste"], "answer": 1, "explain": "Athènes est un grand cheval paresseux ; Socrate, le taon envoyé par le dieu pour la réveiller à coups de questions."},
 {"q": "Pourquoi l’impiété était-elle un crime si grave à Athènes ?", "options": ["Parce que la religion était une affaire privée", "Parce que la religion était publique : offenser les dieux menaçait toute la cité", "Parce que les prêtres gouvernaient la cité", "Parce que Socrate était prêtre"], "answer": 1, "explain": "La religion est le « ciment » de la cité : elle fixe les règles, les fêtes, et assure la protection des dieux."},
 {"q": "Celui qui ignore qu’il ignore est dans…", "options": ["la simple ignorance", "la double ignorance", "le doute", "la connaissance"], "answer": 1, "explain": "La double ignorance empêche de chercher. L’ironie sert à en faire sortir."},
 {"q": "À qui s’adresse l’ironie socratique ?", "options": ["À celui qui croit tout savoir", "À celui qui sait qu’il ignore", "Aux enfants", "Aux dieux"], "answer": 0, "explain": "L’ironie dégonfle la prétention ; la maïeutique aide ensuite celui qui veut chercher."},
 {"q": "Dans le Criton, quel est l’argument de Criton sur la réputation ?", "options": ["On dira que Socrate a eu peur", "On croira que Criton a préféré son argent à son ami", "On oubliera Socrate", "Les Lois seront humiliées"], "answer": 1, "explain": "« Peut-il y avoir de réputation plus honteuse que de passer pour être plus attaché à l’argent qu’à ses amis ? » (§ 26)"},
 {"q": "Quel exemple Socrate utilise-t-il pour l’opinion du compétent ?", "options": ["Le soldat et son général", "Le gymnaste et son médecin/entraîneur", "Le marin et le capitaine", "L’enfant et son père"], "answer": 1, "explain": "Le gymnaste n’écoute pas la foule mais le médecin ou le pédotribe (§ 41-46)."},
 {"q": "« Le plus important n’est pas de vivre, mais… »", "options": ["de vivre longtemps", "de bien vivre", "de mourir en héros", "d’être libre"], "answer": 1, "explain": "§ 63 : et bien vivre, c’est vivre de façon belle et juste."},
 {"q": "Selon les Lois, que doit faire un citoyen en désaccord avec elles ?", "options": ["Fuir", "Se révolter", "Les persuader ou leur obéir", "Les ignorer"], "answer": 2, "explain": "« Persuader ou obéir » : le citoyen libre de partir qui reste s’est engagé à obéir (§ 90-92)."},
 {"q": "Selon les Lois, si Socrate meurt, il est victime…", "options": ["des Lois", "des dieux", "des hommes", "de Criton"], "answer": 2, "explain": "« Tu partiras condamné injustement, non par nous, les lois, mais par les hommes. » (§ 98)"},
 {"q": "Quelle prémisse de l’argument du Criton est souvent jugée la plus fragile ?", "options": ["Il ne faut jamais commettre d’injustice", "S’évader serait une injustice", "Socrate est mortel", "Criton est riche"], "answer": 1, "explain": "On peut discuter l’idée qu’un engagement tacite oblige, ou qu’une seule désobéissance « détruit » les lois."},
]

c = {"files": ["seance1.jsonl", "seance2.jsonl"], "partTitles": ["Séance 1 · Vie, procès et pensée", "Séance 2"],
     "chapters": [{}, {}], "essentiel": essentiel, "texts": texts, "cards": cards, "quiz": quiz}
try:
    c.update(json.load(open('transcript_meta.json')))
except FileNotFoundError:
    pass
json.dump(c, open('content.json', 'w'), ensure_ascii=False, indent=1)
print('cards', len(cards), 'quiz', len(quiz))
