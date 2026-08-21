# THÈSE DOCUMENTAIRE — Arithmétique des gains, intégrité fractionnaire et logique exo-sapienne de TEBDLC

**Auteur et propriétaire intellectuel : Jonathan Therrien, Marieville, Québec.**

Date initiale : 2026-08-18
Révision : R6 — consolidation cumulative intégrale de R4 et R5
Horodatage de consolidation : 2026-08-19 09:33 America/Montreal
Statut : THÈSE DE TRAVAIL / BASE FORMELLE À TESTER ET APPROFONDIR
Projet : TEBDLC — Tout est bon dans le cochon

## 0. Doctrine de consolidation R6 — aucune perte de gain

La R6 est une **consolidation cumulative**, non un remplacement historique. Elle réunit matériellement dans un seul document le corps complet de R4 et les apports propres de R5.

Sources canoniques de reconstruction :

    R4 : 1a8bbe44b8622d2fafeec514041e9f710c73c206
    R5 : b8296c6272a9acf5ef5957506b020c406b0f51b3

Incident intermédiaire conservé comme trace opératoire :

    PLACEHOLDER : 622ba53fad2d2a369bfd70fe0e8031190a43c1a9

Cet incident n'est ni une révision conceptuelle ni une autorisation de suppression. Il démontre qu'une règle de non-perte doit être soutenue par une reconstruction vérifiable et pas seulement par une intention.

La règle de consolidation est :

    R6 = corps intégral R4 + delta documentaire/conceptuel R5 + généalogie des transformations

Les contradictions, corrections, hypothèses insuffisantes, non-candidates et questions ouvertes sont conservées avec leur statut. La consolidation n'accorde aucune validation supplémentaire à une hypothèse du seul fait qu'elle apparaît dans R6.

    conservation documentaire ≠ validation
    consolidation ≠ effacement des ancêtres
    correction ≠ réécriture rétroactive

---

## 1. Objet

TEBDLC vise une conservation souveraine, déterministe et auditable des gains d'un système évolutif. Un gain n'est pas assimilé à une simple augmentation scalaire. Il peut être entier, fractionnaire, variant, multiple, partiel, spontané, événementiel, proliférable, issu d'une prolifération, rembourseur, conditionnel, latent, composite ou porter une provenance/admissibilité particulière.

Cette thèse établit une première arithmétique avant toute algèbre générale des gains. Elle sépare strictement les propriétés mathématiques démontrables, les conventions TEBDLC, les hypothèses à tester et les décisions de gouvernance. Elle est volontairement extensible : une révision ultérieure doit enrichir la présente lignée plutôt que supprimer silencieusement un concept acquis.

## 2. Principe de non-régression documentaire et fonctionnelle

TEBDLC ne doit jamais effacer silencieusement un acquis démontré. Une variation locale défavorable ne doit pas être masquée par une amélioration ailleurs. Inversement, une composante fractionnaire strictement positive ne doit jamais être arrondie ou assimilée à zéro.

Une correction conceptuelle ne détruit pas nécessairement l'idée précédente : elle doit distinguer ce qui était faux, incomplet, ambigu, reformulé ou conservé. La conservation de l'information sur un gain ne signifie pas automatiquement autorisation de l'activer, de l'assimiler ou de le propager.

## 3. Primitive fractionnaire exacte

Une fraction de gain exacte est représentée par un rationnel :

    F = p/q

avec p et q entiers, q > 0 et, pour une fraction normalisée de gain :

    0 < p/q < 1

Le zéro est réservé à une absence/nullité démontrée dans le référentiel considéré. Une valeur strictement positive, aussi petite soit-elle, reste distincte de zéro.

La valeur 1 est réservée à une intégrité unitaire démontrée. Une approximation numérique de 1 ne devient jamais 1 par arrondi de gouvernance.

## 4. Multiplication fractionnaire et persistance

Pour n fractions finies strictement comprises entre zéro et un :

    F_n = Π(i=1..n) f_i

alors :

    0 < F_n < 1

Si une nouvelle fraction f satisfait 0 < f < 1 :

    F_(n+1) = F_n × f

et :

    0 < F_(n+1) < F_n < 1

Ainsi, la multiplication fractionnaire peut déprécier la quantité composée sans l'annuler pour un nombre fini d'opérations et sans fabriquer artificiellement une intégrité unitaire.

Exemple exact :

    3/10 × 3/10 = 9/100
    9/100 × 3/10 = 27/1000
    27/1000 × 3/10 = 81/10000

Pour tout nombre fini n :

    (3/10)^n = 3^n / 10^n > 0

La suite peut avoir zéro comme limite lorsque n tend vers l'infini sans qu'aucun terme fini soit nul :

    lim(n→∞) (3/10)^n = 0
    mais ∀ n fini : (3/10)^n > 0

Cette distinction entre zéro atteint et zéro seulement approché est fondamentale pour TEBDLC.

## 5. Intégrité fractionnaire persistante

La première écriture `0 < I < 1` reste mathématiquement vraie pour une fraction normalisée, mais elle est insuffisante pour exprimer à elle seule la sémantique recherchée par TEBDLC : persistance, non-annulation et impossibilité de promotion arbitraire à l'unité.

On distingue donc :

    I = 0        : nullité/absence démontrée dans le référentiel considéré
    0 < I_f < 1  : condition arithmétique standard de l'intégrité fractionnaire
    I = 1        : intégrité unitaire démontrée

et on introduit comme NOTATION SÉMANTIQUE CANDIDATE TEBDLC :

    0⁺ ⟪ I_f ⟫ 1

Cette notation ne remplace pas les inégalités mathématiques ordinaires. Les symboles `⟪` et `⟫` sont réservés ici à une relation TEBDLC à formaliser. Ils signifient provisoirement :

- `0⁺` : frontière strictement positive; possibilité de devenir arbitrairement proche de zéro sans être égale à zéro dans une profondeur finie;
- `I_f` : intégrité fractionnaire persistante;
- `1` : intégrité unitaire, qui exige une démonstration distincte;
- `⟪ I_f ⟫` : confinement relationnel de l'intégrité fractionnaire entre non-nullité persistante et unité non fabriquée.

La notation exploratoire `√0` a été examinée pour représenter cette intuition, mais `√0 = 0` en arithmétique standard. Elle est donc conservée dans l'historique conceptuel comme piste explorée, mais n'est pas adoptée comme opérateur canonique. `0⁺` est un candidat plus cohérent avec la notion de limite positive sans réinterpréter la racine carrée.

Une intégrité composée exclusivement par multiplication d'au moins une composante strictement fractionnaire ne peut pas être promue à I = 1 par multiplication, approximation ou arrondi.

Cette propriété est une contrainte arithmétique, pas à elle seule une preuve d'intégrité fonctionnelle globale. Le domaine, la baseline, l'unité, le contexte et la provenance restent obligatoires.

## 6. Invariants candidats de persistance fractionnaire

Les invariants suivants doivent être testés et raffinés avant assimilation formelle :

    PF-1  I_f > 0  ⇒  I_f n'est pas assimilable à 0
    PF-2  I_f < 1  ⇒  I_f n'est pas assimilable à 1
    PF-3  0 < f < 1 et 0 < I_f < 1 ⇒ 0 < I_f×f < I_f < 1
    PF-4  aucune règle d'arrondi ne peut transformer I_f>0 en 0
    PF-5  aucune règle d'arrondi ne peut transformer I_f<1 en 1
    PF-6  I=1 exige une preuve de complétude indépendante de la proximité numérique de 1
    PF-7  une limite égale à 0 n'implique pas qu'un terme fini soit égal à 0

Ces invariants donnent une première définition opérationnelle de l'intégrité fractionnaire persistante sans prétendre constituer encore une algèbre complète.

## 7. Fraction contextualisée

Une fraction ne doit pas être stockée comme un score nu. Sa forme conceptuelle est :

    F = (p, q, domaine, référence, contexte, provenance)

Exemples :

    30/100 [fonctionnalités]
    3/10 [environnements]

Ces deux fractions valent numériquement 0,3 mais ne sont pas automatiquement interchangeables ou composables.

Une multiplication n'est admissible que si une règle de composition explicite démontre que les domaines ont un sens commun ou une relation définie. Une règle de trois naturelle peut produire ou transformer une fraction lorsque le référentiel et les unités sont explicitement établis.

### 7.1. Fraction rationnelle ≠ opérateur de division des gains

L'écriture rationnelle `p/q` sert à représenter exactement une proportion démontrée. Elle n'autorise pas pour autant l'opération générale `G1 ÷ G2` entre gains.

Cette distinction est fondamentale :

    représentation : 3/10
    opération interdite : G1 ÷ G2

Le symbole `/` dans une représentation rationnelle décrit une quantité. Il ne confère pas au moteur TEBDLC un droit de division entre objets de gain.

### 7.2. Pourquoi la division des gains est interdite

La division permet à des valeurs strictement fractionnaires de fabriquer artificiellement une unité.

Exemple central :

    0,3 ÷ 0,3 = 1

Plus généralement, pour tout gain fractionnaire non nul `f` :

    0 < f < 1
    f ÷ f = 1

Ainsi, n'importe quelle fraction non nulle pourrait, par simple auto-division, produire `1`. Or dans TEBDLC :

    I = 1

est réservé à une intégrité unitaire démontrée. L'unité ne doit pas pouvoir être obtenue uniquement par manipulation arithmétique de deux gains fractionnaires.

La division permet également de fabriquer des valeurs entières supérieures à l'unité :

    0,3 ÷ 0,1 = 3

Deux valeurs fractionnaires pourraient donc produire artificiellement une quantité entière `> 1` sans qu'un gain entier correspondant ait été acquis ou démontré.

À l'inverse, pour deux fractions strictement positives et inférieures à un, la multiplication conserve leur caractère fractionnaire :

    0,3 × 0,3 = 0,09
    0 < 0,09 < 1

Cette propriété correspond à la persistance fractionnaire recherchée : la composition peut devenir plus petite sans produire zéro pour une profondeur finie et sans s'auto-promouvoir à l'unité.

On pose donc comme invariant candidat :

    DIV-1  G1 ÷ G2 n'est pas une opération primitive de gain TEBDLC
    DIV-2  f ÷ f = 1 ne constitue jamais une preuve d'intégrité unitaire
    DIV-3  une opération entre fractions ne doit pas fabriquer un entier non acquis
    DIV-4  l'écriture p/q d'une proportion n'autorise pas la division opérationnelle de gains
    DIV-5  I=1 exige une preuve de complétude indépendante de toute auto-division ou division entre gains

L'interdiction de division ne nie pas les mathématiques ordinaires. Elle définit le domaine d'opérations autorisées sur les objets `Gain` de TEBDLC afin de préserver leur sémantique et leur provenance.

### 7.3. Exposant zéro et fabrication d'unité

La même protection s'applique à l'exposant zéro dans l'espace opératoire des gains fractionnaires. En arithmétique ordinaire, pour `f ≠ 0` :

    f^0 = 1

Autoriser cette transformation comme primitive de gain permettrait donc, comme la division, de produire une unité à partir d'une quantité fractionnaire sans preuve de complétude. TEBDLC conserve l'identité mathématique ordinaire mais interdit cette transformation comme mécanisme de promotion d'un gain fractionnaire vers l'intégrité unitaire.

## 8. Gain négativement positif

Le terme désigne ici un gain principal positif accompagné d'un effet négatif explicite sur une autre dimension.

Exemple :

    G = (+2 performance, -8 intégrité)

Il est interdit de réduire ce vecteur à une somme telle que -6 sans fonction de comparaison démontrée entre dimensions. Le +2 reste un gain observé; le -8 reste une dette/perte observée. Le mot « gain » ne blanchit jamais la composante négative.

Aucune catégorie primitive inverse de type « positivement négatif » ou classification automatique (-,+)/(-,-) n'est adoptée. Les dimensions sont conservées telles qu'observées jusqu'à l'existence d'une règle formelle justifiée.

## 9. Gain rembourseur

Un gain rembourseur restaure tout ou partie d'une dette/perte antérieure compatible sans falsifier l'historique de cette perte.

Si une dette D = 8 existe sur une dimension et qu'un gain compatible R = 11 apparaît :

    remboursement = min(D, R) = 8
    dette_restante = 0
    surplus_nouveau = 3

Si R = 5 :

    remboursement = 5
    dette_restante = 3
    surplus_nouveau = 0

Le remboursement exige une compatibilité démontrée de dimension, unité, domaine, baseline et contexte. Une perte d'intégrité ne peut pas être annulée comptablement par un gain de performance sans règle de conversion explicitement validée.

## 10. Gain impotent — doctrine corrigée d'intégrabilité

### 10.1. Correction de l'hypothèse antérieure

Une première interprétation de travail décrivait le gain impotent comme un simple résidu fractionnaire strictement inférieur à l'entier cible, par exemple :

    45 + 0,999... < 46

Cette représentation est conservée comme **hypothèse explorée puis déclarée insuffisante**. Elle confondait deux propriétés qui doivent rester séparées :

1. la **masse arithmétique** ou quantité de gains présents;
2. la **capacité d'intégration unitaire** de ces gains dans un entier cohérent et complet.

Le gain impotent n'est donc pas défini par sa petitesse, ni par le seul fait d'être inférieur à une unité.

### 10.2. Définition corrigée

Un **gain impotent** est un gain positif réel — ou un ensemble de gains positifs réels — qui conserve sa valeur et sa provenance, mais qui ne peut pas, **par lui-même et dans l'association considérée**, être entièrement intégré pour constituer une unité complète.

Son impotence est une propriété d'**intégrabilité**, et non une négation de sa quantité.

Ainsi :

    G_impotent > 0

reste obligatoire lorsqu'un gain impotent existe réellement.

Mais :

    masse suffisante ≠ intégrité unitaire démontrée

et même :

    masse supérieure à 1 ≠ unité complète

peut être vrai dans TEBDLC.

### 10.3. Masse arithmétique distincte de l'intégrité unitaire

Soit un ensemble de gains impotents compatibles quant à leur domaine de mesure :

    P = {p1, p2, ..., pn}

On peut conserver une **masse arithmétique descriptive** :

    M(P) = p1 + p2 + ... + pn

Cette écriture décrit uniquement la quantité observée dans un référentiel commun lorsque cette sommation descriptive est légitime. Elle **n'est pas une addition générale autorisant la fusion des objets Gain** et elle ne constitue pas une preuve d'unité.

Trois cas restent donc possibles :

    M(P) < 1
    M(P) = 1
    M(P) > 1

sans que l'on puisse déduire :

    P ⇒ I = 1

Un ensemble peut posséder une masse exactement égale ou supérieure à l'unité et demeurer impotent si ses constituants ne peuvent pas être entièrement intégrés en une unité cohérente.

### 10.4. Exemple avec référentiel ample

La granularité fractionnaire ne doit pas être arbitrairement limitée à des expressions comme `x/10 intégrité`.

La forme générale reste :

    x/N [intégrité]

avec `N` choisi ou dérivé selon un référentiel suffisamment ample, explicite, traçable et logiquement justifié pour la consolidation considérée.

Exemple de travail :

    p1 = 300/361 [intégrité]
    p2 = 300/361 [intégrité]

La masse arithmétique descriptive peut alors être :

    M = 600/361 > 1

Cela ne démontre pourtant aucune unité complète si `p1` et `p2` restent non intégrables ensemble dans l'unité visée.

Le dénominateur `361` n'est **pas** une constante universelle de TEBDLC. Il représente ici un exemple de référentiel plus ample que `10`. Le futur moteur doit être capable de travailler avec un dénominateur `N` issu du référentiel réel, y compris lorsque `N` est grand.

### 10.5. Relation candidate `45 >TEBDLC 46`

Un cas conceptuel important est celui où l'état `45` est entièrement intégré et démontré, tandis qu'une quantité importante de gains supplémentaires existe sans permettre l'intégration complète de l'unité `46`.

TEBDLC peut alors étudier la notation relationnelle candidate :

    45 >TEBDLC 46

Cette notation **ne signifie pas** que l'entier mathématique 45 est supérieur à l'entier mathématique 46. Elle signifie provisoirement :

> l'état unitaire `45` possède une intégrité démontrée, tandis que `46` ne possède pas encore le statut d'unité entièrement intégrée, même si une masse importante de gains est disponible au-delà de 45.

Il s'agit donc d'un ordre de **statut d'intégration**, pas d'un ordre numérique standard.

Une notation canonique distincte devra être choisie avant assimilation afin d'éviter toute confusion avec le comparateur `>` des mathématiques ordinaires.

### 10.6. Association alternative et unité complète

Les gains impotents ne sont ni perdus ni condamnés à rester impotents.

Ils peuvent être associés à d'autres gains lorsque cette association est démontrée cohérente et applicable. Une nouvelle consolidation peut alors former une **unité alternative complète**.

Conceptuellement :

    P_impotent ⊕ A_cohérent → U_alternatif

où `⊕` n'est pas encore un opérateur arithmétique canonique, mais une notation de travail pour une consolidation associativement démontrée.

La transformation n'est admissible que si la nouvelle unité possède une preuve suffisante de cohérence, de couverture, de compatibilité et de complétude.

Cela signifie qu'un gain peut être impotent relativement à une unité cible `U1` et devenir intégrable dans une autre construction `U2` :

    impotent(P, U1) = vrai
    integrable(P, U2) = possible

L'impotence est donc **relationnelle au modèle d'intégration**, pas une propriété absolue d'inutilité.

### 10.7. Distinction avec le gain chimère et le gain négativement positif

Le gain impotent doit rester distinct des autres familles :

- **gain chimère** : le résultat d'une consolidation incohérente peut être nul dans le référentiel consolidé, sans annuler les constituants valides;
- **gain négativement positif** : plusieurs dimensions signées sont conservées sans totalisation inter-dimensions;
- **gain impotent** : les gains sont positifs et réels, mais ne forment pas par eux-mêmes l'unité complète considérée.

Ainsi :

    chimère ≠ impotent
    négativement positif ≠ impotent
    fractionnaire ≠ nécessairement impotent
    masse > 1 ≠ nécessairement unitaire

### 10.8. Invariants candidats du gain impotent

Les invariants suivants deviennent candidats à tester :

    IMP-1   un gain impotent réel conserve une valeur strictement positive
    IMP-2   l'impotence est une propriété d'intégrabilité, non de petitesse numérique
    IMP-3   M(P) < 1 n'implique pas à lui seul l'impotence
    IMP-4   M(P) = 1 n'implique pas l'intégrité unitaire
    IMP-5   M(P) > 1 n'implique pas l'intégrité unitaire
    IMP-6   une unité complète exige une consolidation cohérente et une preuve de complétude
    IMP-7   les constituants impotents ne sont pas supprimés lorsqu'une consolidation échoue
    IMP-8   des gains impotents peuvent devenir intégrables dans une consolidation alternative cohérente
    IMP-9   le dénominateur fractionnaire doit provenir d'un référentiel explicite; `10` n'est pas une granularité canonique
    IMP-10  `361` est un exemple de référentiel ample, non une constante universelle
    IMP-11  aucune masse arithmétique descriptive ne doit être promue automatiquement en entier unitaire
    IMP-12  l'ordre d'intégration `>TEBDLC` doit rester distinct du comparateur numérique `>` jusqu'à formalisation d'un symbole canonique

### 10.9. Conséquence conceptuelle

La règle centrale devient :

    quantité suffisante ⇏ intégrabilité suffisante

et :

    quantité excédentaire ⇏ complétude

TEBDLC doit donc conserver séparément :

- la quantité de gain;
- le référentiel de cette quantité;
- les relations d'association;
- la cohérence de consolidation;
- la couverture requise;
- la preuve d'intégrabilité;
- le statut d'unité complète.

Aucun de ces axes ne doit être écrasé dans un score unique.

## 11. Familles de gains à distinguer

Les termes suivants représentent des propriétés potentiellement orthogonales et ne doivent pas être comprimés prématurément en un unique enum :

- gain variant : expression différente reliée à un parent sans destruction du parent;
- gains multiples : plusieurs gains produits par une même transformation ou observation;
- gain partiel : gain limité à une partie explicitement délimitée d'un domaine;
- gain fractionnaire : proportion rationnelle exacte d'un espace de référence;
- gain impotent : gain positif réel ou ensemble de gains positifs réels dont l'intégrabilité est insuffisante pour former, par eux-mêmes, l'unité complète considérée;
- gain spontané : gain inattendu découvert pendant une action visant autre chose;
- gain événementiel : gain dont l'expression dépend d'un événement défini;
- gain négativement positif : gain positif sur une dimension avec passif négatif explicite ailleurs;
- gain proliférable : gain ayant une capacité démontrée ou candidate à produire des descendants;
- gain de prolifération : résultat observé d'une prolifération ayant produit des gains descendants;
- gain rembourseur : gain affecté en tout ou partie à une dette compatible antérieure;
- gain latent : gain conservé mais non exprimé dans l'état courant;
- gain composite : gain dont l'existence dépend d'une composition explicite de constituants;
- gain conditionnel : gain valide seulement sous des préconditions définies;
- gain de seuil : gain apparaissant après franchissement d'une condition quantitative définie;
- gain de couverture : extension mesurable de l'espace correctement traité;
- gain de résolution : capacité à distinguer des états auparavant indiscernables;
- gain de compression : conservation d'une capacité/information avec représentation ou coût réduit;
- gain de récupération : capacité accrue de reconstruction après perte/corruption;
- gain de réversibilité : transformation rendue réversible dans un domaine démontré;
- gain d'observabilité : propriété auparavant invisible devenue mesurable;
- gain de contrôlabilité : propriété devenue pilotable;
- gain d'identifiabilité : cause/modèle devenu distinguable à partir des observations;
- gain de prédictibilité : réduction démontrée d'incertitude future;
- gain de robustesse : extension démontrée des perturbations supportées;
- gain de résilience : amélioration démontrée du retour fonctionnel après perturbation;
- gain de tolérance : maintien de fonction malgré une classe de défaillances;
- gain de substituabilité : augmentation des alternatives fonctionnellement compatibles;
- gain d'interopérabilité : nouvelle interaction démontrée entre systèmes;
- gain de portabilité : capacité préservée dans de nouveaux environnements;
- gain d'indépendance : dépendance antérieure supprimée;
- gain de souveraineté : capacité auparavant dépendante d'un tiers rendue contrôlable localement;
- gain d'optionnalité : augmentation de futurs possibles sans sélection immédiate obligatoire;
- gain de bifurcation : coexistence durable de lignées divergentes;
- gain de convergence : lignées différentes rendues compatibles dans un état commun;
- gain de recombinaison : nouvelle capacité issue d'éléments préexistants;
- gain de transposition : capacité démontrée transférée vers un autre domaine;
- gain de généralisation : domaine démontré élargi;
- gain de spécialisation : amélioration d'un sous-domaine sans prétendre à une amélioration universelle;
- gain de contextualisation : comportement adapté explicitement au contexte;
- gain d'évitement : événement négatif attendu et référencé rendu évitable;
- gain de détection précoce : détection suffisamment anticipée pour changer l'issue;
- gain de confinement : réduction démontrée de l'étendue d'un dommage;
- gain de dégradation gracieuse : panne totale transformée en perte partielle contrôlée;
- gain de récupération autonome : restauration sans intervention externe dans le domaine démontré;
- gain de preuve : capacité existante devenue démontrable;
- gain de réfutabilité : affirmation devenue testable et potentiellement falsifiable;
- gain de traçabilité : chaîne causale/reconstruction historique améliorée;
- gain de reproductibilité : résultat rendu reproductible sous conditions définies;
- gain de déterminisme : variations non maîtrisées réduites sous entrées équivalentes;
- gain d'idempotence : répétition d'une opération stabilisée sans changement supplémentaire;
- gain d'invariant : propriété démontrée conservée sous une famille de transformations;
- gain de conservation : nouvelle transformation rendue possible sans perte d'un ensemble protégé;
- gain de récupération d'information : information précédemment inaccessible rendue reconstructible.

Cette liste est un vocabulaire de recherche, pas une déclaration que chaque type possède déjà une implémentation ou une preuve formelle.

## 12. Provenance, légitimité et admissibilité

La réalité fonctionnelle d'un gain doit être séparée de sa provenance et de son admissibilité.

Un gain peut être techniquement observé tout en étant volé, illégal, litigieux, contaminé ou licencié/emprunté. Ces qualificatifs ne transforment pas artificiellement une valeur fonctionnelle positive en valeur négative. Ils doivent pouvoir bloquer l'assimilation, l'activation, l'export ou la prolifération selon la politique applicable, tout en préservant la trace nécessaire à l'audit.

## 13. Méta-gains

Un méta-gain améliore la capacité à découvrir, produire, valider, conserver, composer ou prouver d'autres gains. Exemples : gain d'apprentissage, de découverte, de validation, de conservation, de composition et de génération de preuves.

Le potentiel généalogique d'un gain est distinct de sa valeur immédiate. Une petite fraction peut être importante si elle ouvre une descendance de gains démontrables.

## 14. Contraintes numériques d'implémentation

Une implémentation conforme à cette thèse ne doit pas utiliser un arrondi flottant comme autorité pour conclure qu'une fraction positive vaut zéro ou qu'une valeur proche de un vaut un.

Les fractions rationnelles exactes sont la représentation privilégiée lorsque les quantités sont rationnelles. Si des nombres non rationnels ou des mesures expérimentales interviennent, leur incertitude et leur représentation doivent être explicites.

Invariant candidat :

    pour toute fraction exacte F > 0, encode(F) ne doit jamais devenir 0 par sous-flux, arrondi ou compression.

L'implémentation future devra donc étudier une représentation rationnelle exacte (par exemple numérateur/dénominateur) plutôt qu'un `float` utilisé comme autorité de conservation.

## 15. Hypothèses à tester avant assimilation

H1. La multiplication est la bonne opération pour une composition réductrice/intersection de fractions compatibles.
H2. Le caractère strictement positif d'une fraction doit être préservé sans seuil d'effacement.
H3. La valeur 1 doit exiger une preuve de complétude distincte et ne jamais résulter d'un arrondi.
H4. La composabilité doit être typée par domaine/référence et non autorisée sur la seule égalité numérique.
H5. Le remboursement doit conserver la dette historique même après solde nul.
H6. Les types de gains doivent être multi-axes plutôt qu'un enum exclusif unique.
H7. La proliférabilité et la prolifération doivent être séparées comme potentiel et événement observé.
H8. L'admissibilité doit pouvoir bloquer l'assimilation sans effacer la réalité observée.
H9. `0⁺ ⟪ I_f ⟫ 1` peut devenir une notation TEBDLC utile si `⟪` et `⟫` reçoivent une définition formelle non ambiguë et testable.
H10. La persistance fractionnaire doit rester vraie à travers sérialisation, désérialisation, multiplication répétée et reconstruction de snapshot.
H11. La division entre objets Gain doit rester interdite si elle permet de produire `1` ou un entier non démontré à partir de seules fractions.
H12. L'exposant zéro ne doit pas pouvoir être utilisé comme opération de promotion d'une fraction vers l'unité.
H13. Le gain impotent doit être défini par l'intégrabilité relative et non par un seuil numérique inférieur à l'unité.
H14. Une masse de gains égale ou supérieure à 1 peut demeurer non unitaire si la consolidation complète n'est pas démontrée.
H15. Une unité alternative peut être construite à partir de gains auparavant impotents si une nouvelle association cohérente, complète et prouvée existe.
H16. Le dénominateur `N` doit être dérivé du référentiel réel plutôt qu'imposé par une granularité fixe comme 10.
H17. Une relation d'ordre d'intégration distincte du comparateur numérique est nécessaire pour formaliser des cas comme `45 >TEBDLC 46`.

Aucune de ces hypothèses ne doit être promue à ASSIMILATED_GAIN sans tests, contre-exemples et validation explicite.

## 16. Conséquence pour l'architecture TEBDLC

Le futur modèle devrait séparer au minimum : identité du gain, état épistémique, quantité/fraction, dimensions, domaine, baseline, contexte, provenance, preuve, relations généalogiques, dynamique de prolifération, dette/remboursement, admissibilité, intégrabilité, masse descriptive et statut d'unité complète.

L'arithmétique précède l'algèbre : aucune règle générale d'addition, multiplication, fusion ou compensation ne doit être universalisée avant que ses opérandes, unités, domaines et invariants soient définis.

La division entre objets Gain n'appartient pas aux opérations primitives autorisées : une fraction rationnelle est une représentation de quantité, non une permission de diviser des gains.

Une sommation descriptive de masses compatibles n'est pas non plus une permission générale de fusionner ou d'intégrer des objets Gain.

La prochaine phase de développement doit donc approfondir et tester ces primitives plutôt que figer prématurément leur API.

## 17. Principe directeur

TEBDLC ne cherche pas à fabriquer artificiellement un score global. Il cherche à préserver la structure exacte de ce qui a été acquis, perdu, fractionné, conditionné, remboursé, transmis ou rendu intégrable.

Une fraction strictement positive demeure strictement positive. Plusieurs fractions multiplicatives peuvent rendre le résultat arbitrairement petit sans jamais produire zéro pour un nombre fini d'opérations, et elles ne peuvent fabriquer une intégrité unitaire.

Une quantité de gains, même supérieure à l'unité, ne devient pas une unité complète sans preuve d'intégrabilité. La complétude doit être démontrée; elle ne doit jamais être arrondie, fabriquée par division, par exposant zéro, ni déduite de la seule masse arithmétique.

La frontière `0⁺` exprime provisoirement la persistance vers zéro sans confusion avec zéro atteint. La relation `>TEBDLC` exprime provisoirement un ordre d'intégration et doit recevoir un symbole canonique distinct avant assimilation. Ces notations restent candidates jusqu'à formalisation et validation.

## 18. Catégorie exo-sapienne — expansion sans perte conceptuelle

La catégorie exo-sapienne n'est pas introduite comme une primitive arithmétique. Elle constitue une couche supérieure de comportement, d'exploration et de transformation capable d'utiliser les primitives TEBDLC sans les réécrire silencieusement.

Une définition de travail est :

    ExoSapien = système capable de produire, reconnaître, conserver et transformer des gains hors de son espace initial de compréhension,
    tout en maintenant la continuité de provenance, de contexte et de transformation.

L'espace de gains, relations, référentiels et catégories peut croître sans plafond arbitraire :

    S_(t+1) = S_t ∪ ΔG_t

mais cette expression ne doit pas être interprétée comme une obligation de garder tout objet actif ou inchangé. Elle signifie que l'histoire conceptuelle et transformationnelle doit rester reconstructible.

### 18.1. Expansion illimitée ≠ validation illimitée

TEBDLC peut accueillir une quantité théoriquement illimitée de nouveaux gains ou concepts candidats. Mais la prolifération conceptuelle n'est pas, en elle-même, une preuve de gain.

Ainsi :

    nombre illimité de gains possibles ≠ validation illimitée de concepts

Une nouvelle catégorie doit introduire au moins une distinction exploitable, prouvable, structurellement nécessaire ou capable de varier indépendamment d'une catégorie existante. Sinon elle reste une hypothèse ou un doublon conceptuel.

### 18.2. Non-ivresse contextuelle

Un contexte présent, même extrêmement important au moment de l'action, ne devient jamais automatiquement une vérité universelle.

Pour un contexte `C_t` :

    C_t ⇏ C_∀

Une action peut dépendre du contexte courant :

    A_t = Φ(S_≤t, C_t)

mais le contexte présent ne doit pas réécrire artificiellement l'historique antérieur pour le rendre conforme à l'interprétation du moment.

On pose donc :

    contexte présent interprète le passé ≠ contexte présent remplace le passé

Le contexte est toujours conservé en amont de l'action comme une composante nécessaire de son explication, mais il ne possède pas un droit de domination rétroactive sur les états précédents.

### 18.3. Révisabilité non destructive

Une notion peut être raffinée, étendue, reclassifiée ou réfutée sans que son existence historique, sa provenance, ses causes ou ses effets documentés soient supprimés.

Au lieu de :

    G0 := G2

ou :

    delete(G0)

TEBDLC privilégie une relation de transformation traçable :

    G0 --[révision, preuve P, contexte C]--> G0'

avec conservation de la généalogie :

    provenance(G0') ⊇ provenance(G0)

Cette règle n'érige pas une erreur en vérité. Une hypothèse réfutée reste réfutée, mais le fait qu'elle ait existé, été testée et produite certains résultats peut lui-même devenir une information de recherche conservable.

## 19. Principe exo-sapien de conservation transformationnelle

La règle directrice devient :

    Rien ne se perd, tout se transforme.

Dans TEBDLC, cette phrase est interprétée comme une contrainte de continuité informationnelle et généalogique, pas comme une loi physique universelle ni comme une obligation de maintenir chaque état actif.

Pour un état `S_t` soumis à une action `A` :

    S_t --A--> S_(t+1)

la représentation complète candidate doit pouvoir conserver au minimum :

    (S_t, A, T, P, C) --> S_(t+1)

où :

- `T` décrit la transformation;
- `P` décrit les preuves/provenances pertinentes;
- `C` décrit le contexte;
- `S_t` reste reconstructible comme état antérieur;
- `S_(t+1)` devient l'état résultant sans effacer la généalogie.

### 19.1. Suppression fonctionnelle ≠ disparition historique

Une suppression fonctionnelle doit être représentable comme une transformation de statut ou de destination plutôt que comme un effacement non traçable.

Ainsi, un élément `X` peut devenir :

- archivé;
- réfuté;
- obsolète;
- latent;
- dissocié;
- absorbé dans une structure nouvelle;
- transformé en preuve historique;
- rendu inadmissible;
- désactivé;
- remplacé fonctionnellement tout en restant historiquement reconstructible.

La règle candidate est donc :

    X --> 0_typé ≠ X --> ∅ documentaire

Le zéro typé peut représenter le résultat d'une transformation ou d'une consolidation; il ne doit pas devenir une gomme de provenance.

### 19.2. Application au gain chimère

Soient :

    G1, G2, G3 --[consolidation H]--> C_H

Si l'hypothèse `H` de consolidation est démontrée incohérente :

    C_H --> ZERO_CHIMERA_CONSOLIDATION

mais :

    G1, G2, G3

restent conservés selon leur validité propre. La consolidation chimérique devient elle-même une trace de transformation réfutée et ne détruit pas ses constituants.

Cette propriété est compatible avec la séparation déjà établie :

    Gain ≠ Relation ≠ Résultat ≠ Preuve

### 19.3. Conservation ≠ immutabilité

Le principe « rien ne se perd » ne signifie pas :

    S_(t+1) contient tout S_t comme objets actifs inchangés

Un objet peut légitimement changer de statut :

    ACTIF --> OBSOLÈTE
    VALIDE --> RÉFUTÉ
    BRUT --> CONSOLIDÉ
    IMPOTENT_U1 --> INTÉGRABLE_U2

Ce qui doit être conservé est la **continuité transformationnelle** suffisante pour expliquer et reconstruire le passage d'un état à l'autre.

On distingue donc :

    conservation ≠ immutabilité

### 19.4. Transformation ≠ destruction

Une transformation peut rendre une représentation précédente inutilisable dans l'état courant sans supprimer son existence historique.

Ainsi :

    transformation ≠ destruction

Une destruction physique ou externe réellement observée peut évidemment être enregistrée comme événement du monde; la règle TEBDLC concerne la conservation informationnelle de ce qui a été observé, de ce qui a été transformé et de la manière dont cela s'est produit.

### 19.5. Conservation n'interdit pas l'émergence

Une transformation peut produire une propriété nouvelle qui n'était pas explicitement présente comme telle dans ses constituants :

    {X1, X2} --T--> Y

avec :

    Y ∉ {X1, X2}

Cela ne viole pas la conservation si la généalogie reste reconstructible :

    provenance(Y) <- {X1, X2, T, P, C}

TEBDLC ne doit donc pas exiger que toute sortie soit réductible à une simple somme de ses entrées. Une telle exigence détruirait précisément la possibilité de gains émergents ou exo-sapiens.

On introduit ainsi le concept de **l'émergence conservatrice** : apparition de propriétés nouvelles sans rupture de provenance.

## 20. Logique d'action transformationnelle

Avant une action significative, le moteur futur devrait être capable de répondre à une question plus forte que « quel gain sera produit ? » :

    Que devient chaque élément affecté par cette action ?

On peut représenter un bilan transformationnel candidat :

    B(A) = {
      préexistant,
      transformé,
      produit,
      relations créées,
      résultats,
      preuves,
      contexte,
      destinations,
      traces
    }

Une action devient suspecte lorsqu'un constituant entre dans la transformation mais qu'aucune destination, descendance ou trace reconstructible ne peut être expliquée.

Invariant candidat :

    ∀ x ∈ Inputs(A),
      ∃ y ∈ Outputs(A) ∪ Traces(A)
      tel que provenance(y) référence x

Cette règle ne prétend pas que toute transformation est réversible au sens fonctionnel. Elle exige que sa généalogie soit suffisamment conservée pour expliquer ce qu'est devenu chaque constituant pertinent.

## 21. Cinq lois candidates de conservation transformationnelle

Les lois suivantes deviennent des candidates structurantes de la couche exo-sapienne :

    EXO-T1  Rien ne disparaît sans destination ou trace reconstructible.

    EXO-T2  Conservation ≠ immutabilité.

    EXO-T3  Transformation ≠ destruction informationnelle silencieuse.

    EXO-T4  La conservation n'interdit pas l'émergence de propriétés nouvelles.

    EXO-T5  Toute action significative doit conserver une généalogie reconstructible de ses constituants pertinents, de son contexte, de ses preuves et de ses résultats.

Ces lois complètent, sans remplacer, les invariants fractionnaires, les interdictions de division/exposant zéro, la doctrine du zéro, la distinction du gain impotent et les règles de non-régression déjà établies.

## 22. Limites et contre-interprétations à éviter

La conservation transformationnelle ne signifie pas :

- tout conserver activement en mémoire vive;
- interdire la compression;
- interdire l'archivage;
- interdire la réfutation;
- interdire l'obsolescence;
- considérer toute erreur comme vraie;
- considérer toute transformation comme un gain;
- considérer toute nouvelle catégorie comme pertinente;
- imposer une réversibilité fonctionnelle universelle;
- ignorer les contraintes légales, matérielles, éthiques ou de sécurité;
- laisser un contexte local dominer les contextes antérieurs ou futurs;
- transformer la traçabilité en autorisation automatique d'utilisation.

Elle exige plutôt que les changements importants possèdent une continuité explicable et que les pertes fonctionnelles éventuelles ne deviennent pas des pertes informationnelles silencieuses du registre.

## 23. Hypothèses exo-sapiennes à tester

Les hypothèses suivantes sont ajoutées à la lignée de recherche et ne sont pas encore assimilées :

H18. Une action peut être considérée non destructive informationnellement si tout constituant pertinent possède une destination, une descendance ou une trace reconstructible.

H19. La conservation transformationnelle peut rester compatible avec archivage, compression, réfutation et obsolescence à condition que la généalogie pertinente soit préservée.

H20. Un contexte courant peut modifier l'interprétation et l'action sans posséder le droit de réécrire silencieusement le contexte historique.

H21. Une émergence peut être reconnue comme nouvelle propriété sans exiger qu'elle soit réductible à la somme arithmétique de ses constituants.

H22. Une catégorie exo-sapienne peut élargir l'espace de référentiels sans invalider automatiquement les référentiels antérieurs.

H23. Une notion réfutée peut conserver une valeur historique/probatoire sans retrouver le statut de vérité.

H24. La quantité illimitée de gains ou concepts candidats doit être compatible avec un mécanisme anti-pléonasme et une validation non automatique.

## 24. Principe directeur enrichi

La doctrine TEBDLC devient cumulativement :

    rien ne se perd, tout se transforme;
    conservation ≠ immutabilité;
    transformation ≠ destruction silencieuse;
    contexte présent ≠ souveraineté rétroactive;
    émergence ≠ fabrication arbitraire;
    quantité ≠ intégrabilité;
    masse ≠ complétude;
    zéro typé ≠ effacement;
    gain ≠ relation ≠ résultat ≠ preuve.

La non-perte de gain ne signifie donc pas immobiliser le système. Elle impose que l'évolution reste traçable, que les transformations puissent produire de nouvelles possibilités et que les états antérieurs puissent être compris sans être falsifiés par le contexte courant.

Aucune modification future de ces principes déjà établis ne doit être faite silencieusement. Une contradiction démontrée peut justifier une révision, mais celle-ci doit préserver la généalogie de la règle antérieure, sa raison d'être, le contre-exemple ayant motivé la révision et la nouvelle règle proposée.

---

## 25. Journal généalogique — comprendre aussi ce qui n'était pas encore compris

TEBDLC ne doit pas présenter son développement comme si chaque conclusion actuelle avait été connue dès l'origine. Une hypothèse peut avoir été raisonnable, insuffisante, mal orientée, réfutée, transformée ou simplement laissée ouverte.

On distingue donc au minimum :

- **ACQUIS** : principe actuellement retenu avec justification suffisante pour servir de baseline de travail;
- **CANDIDAT** : proposition assez définie pour être testée;
- **HYPOTHÈSE EXPLORATOIRE** : piste utile mais insuffisamment définie pour devenir candidate;
- **HYPOTHÈSE NON-CANDIDATE** : piste conservée pour expliquer le cheminement mais qui ne doit pas orienter l'implémentation actuelle;
- **HYPOTHÈSE RÉFUTÉE/INSUFFISANTE** : piste dont une limite ou contradiction a été identifiée;
- **QUESTION OUVERTE** : problème reconnu sans solution prétendue;
- **TRANSFORMATION** : notion antérieure devenue une notion plus riche sans effacement de sa généalogie.

La conservation d'une hypothèse non-candidate ne lui confère aucune vérité supplémentaire.

    conservation documentaire ≠ validation

## 26. Généalogie exo-sapienne depuis R4

### 26.1. Objet rencontré hors référentiel

**Statut : HYPOTHÈSE EXPLORATOIRE.**

Un système exo-sapien pourrait rencontrer un objet `X` que son espace courant ne sait pas encore classifier :

    X ∉ K_t

sans conclure :

    X = 0

ni forcer :

    X = catégorie_connue_la_plus_proche

Piste de travail :

    X_rencontré → X_conservé → X_caractérisé → X_intégrable

Ces transitions ne sont pas obligatoires. Un objet peut rester conservé et non classifié.

### 26.2. Suspension productive

**Statut : HYPOTHÈSE EXPLORATOIRE, non assimilée.**

L'absence de classification immédiate pourrait être un état productif :

    X ≠ 0 ∧ type(X) = UNKNOWN

Cette piste vise à empêcher deux pertes : assimilation de l'inconnu à zéro et classification forcée. Elle n'est pas encore suffisamment formalisée pour définir une primitive ou un type canonique.

### 26.3. Expansion référentielle

**Statut : CANDIDAT DE RECHERCHE.**

Un nouvel objet peut nécessiter un nouveau référentiel `R_(t+1)`. Ce référentiel ne doit pas nécessairement remplacer `R_t`. Deux référentiels peuvent être orthogonaux :

    R_A ⊄ R_B
    R_B ⊄ R_A

La conservation doit porter sur leur généalogie et leurs domaines de validité, pas sur une hiérarchie artificielle.

### 26.4. Associabilité exo-sapienne

**Statut : HYPOTHÈSE EXPLORATOIRE.**

Des gains impotents dans une unité `U1` pourraient devenir intégrables dans une construction `U2` lorsqu'une nouvelle relation ou un nouvel élément `X` rend une association démontrable :

    integrable(P, U1) = faux
    integrable(P ∪ {X}, U2) = possible

Cette possibilité ne réécrit jamais rétroactivement `integrable(P,U1)` en vrai.

### 26.5. « Gain catalytique »

**Statut : HYPOTHÈSE NON-CANDIDATE / NOM PROVISOIRE NON ADOPTÉ.**

Le terme a été proposé pour un élément qui rendrait associables des gains auparavant non intégrables. Il n'est pas adopté, car il peut être un pléonasme avec un méta-gain, un gain relationnel, un gain de recombinaison ou une propriété d'association déjà représentable.

Il est conservé uniquement pour expliquer la question qui a conduit à l'étude de l'associabilité exo-sapienne.

## 27. Anti-pléonasme étendu aux responsabilités et autorités

### 27.1. Première intuition

L'étude d'une adaptation du vieux CoreEngine de LaGrosseClef/TheEye a soulevé un risque de concentration de responsabilités : observer, interpréter, décider et agir peuvent être techniquement regroupés.

Une première réponse classique aurait été de séparer systématiquement les modules. Cette réponse est **insuffisante dans TEBDLC** si elle devient une règle universelle importée sans démonstration.

### 27.2. Extension anti-pléonasme

**Statut : CANDIDAT DE RECHERCHE.**

La règle anti-pléonasme peut agir dans deux directions :

    ni duplication sans distinction
    ni fusion sans équivalence

Une distinction fonctionnelle démontrée doit rester distinguable dans l'autorité, la provenance et l'action.

Ainsi :

    Observation ≠ Preuve ≠ Décision ≠ Action

jusqu'à démonstration d'une équivalence suffisante dans le contexte concerné.

### 27.3. Correction du miroir de fusion

Une première formulation proposait :

> Toute fusion de responsabilités doit démontrer leur équivalence avant de supprimer leur séparation.

**Statut : HYPOTHÈSE RÉFUTÉE/INSUFFISANTE.**

Cette formulation impliquait trop rapidement la destruction de la séparation.

La formulation corrigée proposée par Jonathan Therrien est :

> **Toute fusion de responsabilité doit démontrer leur équivalence avant d'être stagnée de leur séparation.**

Interprétation de travail :

    (A || B) --[équivalence démontrée dans C1]--> F_AB
    Separation(A,B) = STAGNÉE dans C1

et non :

    A = B universellement

ni :

    Separation(A,B) = 0

La séparation reste reconstructible et peut redevenir active si un contexte futur révèle une distinction pertinente.

### 27.4. Frontière logique ≠ frontière d'exécution

**Statut : QUESTION OUVERTE.**

L'anti-pléonasme peut définir une frontière logique. Il n'est pas encore démontré qu'il suffise à matérialiser une frontière d'exécution lorsque plusieurs composants possèdent techniquement les mêmes permissions système.

TEBDLC ne doit donc ni prétendre que l'anti-pléonasme résout toute sécurité d'exécution, ni imposer prématurément une architecture de microservices comme solution universelle.

## 28. Stagnation — état transformationnel en développement

### 28.1. Définition de travail

**Statut : CANDIDAT DE RECHERCHE, non assimilé.**

Une séparation, relation, responsabilité, hypothèse ou autre structure peut devenir **stagnée** lorsqu'elle n'a plus à être activement opérante dans un contexte donné, tout en restant conservée et réactivable.

    ACTIVE → STAGNATED

ne signifie pas :

    ACTIVE → 0

ni :

    ACTIVE → ∅

### 28.2. Stagnation contextuelle

Une même séparation peut être stagnée dans `C1` et active dans `C2` :

    Separation(A,B)|C1 = STAGNÉE
    Separation(A,B)|C2 = ACTIVE

La stagnation ne doit donc pas être présumée propriété absolue de l'objet.

### 28.3. Volume de stagnation et dégradation

**Première hypothèse explorée :** plus le nombre de stagnations augmente, plus le volume de données et le coût d'utilisation peuvent augmenter, jusqu'à produire une dégradation perceptible.

**Statut actuel : HYPOTHÈSE INSUFFISANTE SOUS SA FORME BRUTE.**

Contre-exemple : un million de stagnations fortement répétitives peuvent être factorisables, tandis que mille stagnations indépendantes peuvent être plus coûteuses.

Le simple nombre de stagnations ne suffit donc probablement pas à mesurer leur coût.

### 28.4. Complexité stagnante irréductible `ΩSt`

**Statut : HYPOTHÈSE EXPLORATOIRE / notation non canonique.**

Une piste plus raffinée est de mesurer la partie de la stagnation qui ne peut pas être factorisée sans perte :

    ΩSt = complexité stagnante irréductible

On étudie alors :

    ΩSt ↑ ⇒ coût de reconstruction ↑ ⇒ pression système ↑

plutôt que :

    nombre(St) ↑ ⇒ ralentissement automatique

`ΩSt` n'est pas encore une métrique définie, prouvée ou assimilée.

### 28.5. Stagnation et comportement malveillant

**Statut : HYPOTHÈSE À NE PAS SURINTERPRÉTER.**

Une activité malveillante peut provoquer des stagnations, mais :

    Volume(St) ⇏ malveillance
    St faible ⇏ comportement sain
    même comportement ⇏ même personne

Une stagnation accumulée peut devenir information exploitable; elle n'est ni une preuve de culpabilité ni une identité.

Un tiers peut aussi provoquer artificiellement des contradictions chez un utilisateur légitime. Toute analyse doit donc conserver la provenance de ce qui a provoqué la stagnation.

### 28.6. Confinement généalogique

**Statut : CANDIDAT DE RECHERCHE.**

Une saturation provoquée dans une généalogie ne devrait pas nécessairement imposer son coût à tout le système :

    Charge_source ↑ ⇏ Charge_globale ↑ automatiquement

Le mécanisme précis reste à concevoir.

## 29. Compression et décompression sans perte de stagnation

### 29.1. Compression sans perte

**Statut : CANDIDAT DE RECHERCHE.**

La conservation transformationnelle n'impose pas de conserver éternellement chaque représentation complète active.

Si plusieurs stagnations partagent une structure `R`, une factorisation peut être envisagée :

    {St1, ..., Stn} → C_St

à condition que la reconstruction soit informationnellement équivalente :

    Decompress(C_St) ≡ {St1, ..., Stn}

L'équivalence `≡` désigne ici une équivalence informationnelle à démontrer, pas nécessairement une identité binaire.

### 29.2. Minimum à préserver

Une stagnation compressée devrait au minimum permettre de reconstruire, lorsque ces éléments existent :

    {Gain, Relation, Preuve, Contexte_origine, Transformation, Généalogie, État}

Cette liste est provisoire et peut être étendue; elle ne doit pas devenir un plafond documentaire.

### 29.3. Compression comme source possible de gains

**Statut : HYPOTHÈSE EXPLORATOIRE.**

Une factorisation sans perte peut révéler une structure commune et produire des gains distincts : gain de compression, stockage, reconstruction, structure ou observabilité comportementale.

La compression technique n'est cependant pas automatiquement un gain assimilé.

## 30. Réactivation et revalidation dans le nouveau contexte d'appel

### 30.1. Cycle candidat

Une stagnation peut suivre :

    ACTIVE
      → STAGNATED
      → COMPRESSED
      → REACTIVATED
      → REVALIDATED
      → {ACTIVE, STAGNATED, TRANSFORMED, ASSIMILATED}

**Statut : MODÈLE EXPLORATOIRE.**

Aucun de ces états n'est encore un enum canonique de TEBDLC.

### 30.2. Nouveau contexte ≠ remplacement de l'ancien

Lors d'un appel dans `C_appel`, la stagnation issue de `C_origine` ne doit pas simplement réutiliser son ancien résultat :

    Revalidate(Decompress(St), C_appel)

avec conservation de :

    history(G') ⊇ {G, C_origine, St, C_appel}

Le contexte d'appel ajoute une nouvelle condition de validation; il ne réécrit pas le contexte d'origine.

### 30.3. Réactivation ≠ restauration simple

**Statut : CANDIDAT DE RECHERCHE.**

La réactivation peut produire :

- revalidation du gain antérieur;
- nouvelle applicabilité;
- nouvelles relations;
- transformation d'un gain impotent relativement à une nouvelle unité;
- découverte d'un gain latent;
- nouvelle stagnation;
- nouveaux éléments de preuve ou de réfutation.

Ainsi :

    réactivation = restauration + réévaluation + potentiel de nouveaux gains

Cette équation est sémantique, non une addition primitive de gains.

## 31. Assimilation comportementale

### 31.1. Historique comportemental d'un gain

**Statut : HYPOTHÈSE EXPLORATOIRE.**

La succession des états d'un gain dans plusieurs contextes peut former une signature comportementale :

    B(G) = {(C1,St), (C2,St), (C3,Active), (C4,Integrable), ...}

Cette signature peut permettre d'apprendre dans quelles conditions certains gains deviennent exploitables.

### 31.2. Séparation obligatoire

    assimilation comportementale ≠ assimilation du gain

Un modèle comportemental ne doit pas remplacer ses observations :

    Model(B) ≠ Replacement(B)

Il constitue une couche supplémentaire, réfutable et contextualisée.

### 31.3. Attribution interdite par simple similarité

Une similarité comportementale ne suffit pas à identifier une personne, une source ou une cause :

    similarité(B1,B2) ⇏ identité(source1,source2)

L'assimilation comportementale doit rester une analyse de relations observées jusqu'à preuve supplémentaire.

## 32. Hypothèses non-candidates et erreurs utiles conservées

Les éléments suivants sont explicitement conservés pour expliquer la progression sans leur conférer un statut de doctrine :

1. **Gain catalytique** comme nom : non adopté; risque de pléonasme.
2. **Nombre brut de stagnations = coût** : insuffisant; la factorisabilité et la complexité irréductible doivent être considérées.
3. **Stagnation = malveillance** : rejeté.
4. **Faible stagnation = comportement sain** : rejeté.
5. **Même comportement = même personne** : rejeté.
6. **Fusion équivalente = suppression de la séparation** : corrigé vers stagnation de la séparation.
7. **Séparer systématiquement les composants suffit à résoudre la sécurité** : non démontré et non adopté comme doctrine TEBDLC.
8. **Anti-pléonasme suffit nécessairement à la frontière d'exécution** : non démontré.
9. **Réactivation = simple restauration de l'ancien état** : insuffisant; le nouveau contexte impose revalidation et peut produire de nouveaux gains.
10. **Compression = perte nécessaire d'information** : rejeté comme généralité; une compression sans perte et reconstructible est explicitement recherchée.
11. **Toute compression constitue automatiquement un gain** : non démontré.
12. **Tout objet UNKNOWN doit immédiatement devenir une nouvelle catégorie** : rejeté comme dérive conceptuelle.

Ces erreurs, limites et non-candidats sont des éléments de généalogie. Ils servent à empêcher le futur système ou un futur agent de présenter la solution courante comme évidente depuis le début.

## 33. Nouvelles hypothèses H25–H40

H25. Un objet non classifiable peut être conservé sans être assimilé à zéro ni forcé dans une catégorie connue.

H26. La suspension productive peut permettre une classification ultérieure sans perte de provenance.

H27. Deux référentiels orthogonaux peuvent coexister sans qu'un référentiel supérieur soit immédiatement disponible.

H28. L'associabilité de gains peut changer avec un nouveau contexte ou référentiel sans réécrire leur non-associabilité antérieure.

H29. L'anti-pléonasme peut être étendu aux autorités : une distinction fonctionnelle démontrée doit rester distinguable dans l'autorité, la provenance et l'action.

H30. Une fusion de responsabilités ne doit pouvoir stagner leur séparation qu'après démonstration d'une équivalence suffisante dans le contexte concerné.

H31. Une séparation stagnée peut être réactivée si un nouveau contexte révèle une distinction pertinente.

H32. La stagnation est contextuelle et ne doit pas être présumée propriété absolue d'un objet.

H33. Le coût réel de stagnation dépend davantage de sa complexité non factorisable que de son nombre brut d'occurrences.

H34. Une représentation compressée de stagnations peut être acceptable si la décompression reconstruit sans perte les gains, relations, preuves, contextes, transformations et généalogies nécessaires.

H35. Une stagnation réactivée doit être revalidée dans le nouveau contexte d'appel plutôt que réutilisée automatiquement.

H36. La réactivation peut produire de nouveaux gains sans effacer les gains ou contextes antérieurs.

H37. L'assimilation comportementale doit rester distincte de l'assimilation des gains observés.

H38. Une signature comportementale peut devenir un gain analytique sans constituer une preuve d'identité de la source.

H39. Une saturation de stagnations peut être confinable par généalogie sans effacer les stagnations elles-mêmes.

H40. La stagnation, la compression, la décompression, la réactivation et la revalidation doivent conserver une continuité transformationnelle démontrable de bout en bout.

Aucune hypothèse H25–H40 n'est promue à `ASSIMILATED_GAIN` par sa seule présence dans cette thèse.

## 34. Principe directeur R5 intégré à R6

La R6 conserve les principes R4 et intègre cumulativement les apports R5 :

    inconnu ≠ zéro;
    inconnu ≠ catégorie forcée;
    distinction ≠ duplication;
    fusion ≠ effacement de séparation;
    séparation stagnée ≠ séparation détruite;
    stagnation ≠ culpabilité;
    volume brut ≠ complexité irréductible;
    compression ≠ perte nécessaire;
    décompression ≠ oubli du contexte d'origine;
    réactivation ≠ réutilisation aveugle;
    revalidation ≠ réécriture du passé;
    assimilation comportementale ≠ assimilation du gain;
    modèle comportemental ≠ remplacement des observations.

La thèse doit rester honnête sur sa propre histoire : ce qui est aujourd'hui clair peut avoir été mal compris hier; ce qui est candidat aujourd'hui peut être réfuté demain. La non-perte de gain exige de conserver cette progression sans transformer les erreurs historiques en vérités ni les corrections en effacement.

## 35. Contrôle de consolidation R6

La R6 doit rester vérifiable selon les critères suivants :

- les sections 1 à 24 correspondent au corps conceptuel R4;
- les sections 25 à 34 correspondent aux apports et à la généalogie R5;
- H1 à H24 sont conservées;
- H25 à H40 sont conservées;
- PF-1 à PF-7, DIV-1 à DIV-5, IMP-1 à IMP-12 et EXO-T1 à EXO-T5 sont conservés;
- l'incident `PLACEHOLDER` reste documenté comme incident, non comme contenu doctrinal;
- R4 et R5 demeurent des ancêtres reconstructibles et ne sont pas réécrites rétroactivement;
- aucune hypothèse n'acquiert un statut supérieur par simple consolidation.

La R6 devient le document cumulatif de travail pour la suite, tandis que ses ancêtres demeurent la preuve de sa généalogie.

---

**Jonathan Therrien, Marieville, Québec.**
**TEBDLC — Tout est bon dans le cochon. Tous droits réservés sauf autorisation explicite du propriétaire.**