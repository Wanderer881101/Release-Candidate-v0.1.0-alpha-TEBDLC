# FAMILLES DE GAINS FORMALISÉES — TEBDLC

**Jonathan Therrien, Marieville, Québec.**

Horodatage : 2026-08-19 06:55:50 America/Montreal
Statut : FORMALISATION CANDIDATE / R&D

## Méthode

Chaque famille doit posséder :

- une définition non pléonastique;
- une condition d'existence;
- une condition de distinction;
- au moins un contre-exemple;
- une relation avec les autres couches `GAIN / RELATION / RÉSULTAT / PREUVE`;
- une règle de non-perte.

## FG-01 — Gain fractionnaire

Définition : gain quantifié par une valeur rationnelle exacte strictement comprise entre zéro et un dans un référentiel défini.

    0 < Gf < 1

Condition d'existence : numérateur, dénominateur, domaine, référentiel, contexte et provenance définis.

Distinction : il décrit une proportion réellement référencée; il n'est pas créé par division d'un autre gain.

Contre-exemple : `0.3 ÷ 0.3 = 1` ne transforme pas deux gains fractionnaires en intégrité unitaire TEBDLC.

Non-perte : aucune profondeur finie de multiplication exacte ne peut le transformer en zéro.

## FG-02 — Gain partiel

Définition : gain dont le domaine d'application ne couvre qu'une partie explicitement délimitée d'un domaine plus large.

Un gain partiel n'est pas nécessairement fractionnaire : sa quantité peut être entière ou qualitative, tandis que sa portée est partielle.

Condition de distinction :

    quantité(G) et support(G)

sont deux dimensions différentes.

Contre-exemple : une capacité complète sur 3 environnements parmi 10 est partielle par couverture sans nécessairement valoir `3/10` comme amplitude.

## FG-03 — Gain variant

Définition : gain relié à un gain parent par une variation de forme, contexte, implémentation ou expression, sans annulation du parent.

Relation :

    VARIANT_OF(Gv, Gp)

Condition d'existence : la relation au parent et les dimensions modifiées doivent être explicites.

Contre-exemple : deux gains indépendants mais similaires ne sont pas automatiquement variants.

Non-perte : le parent reste conservé.

## FG-04 — Gains multiples

Définition : une même action/observation produit plusieurs gains distincts.

    EVENT -> {G1,G2,...,Gn}

Condition de distinction : les gains doivent avoir des identités ou propriétés indépendamment traçables.

Contre-exemple : observer deux fois le même gain n'est pas automatiquement « gains multiples ».

## FG-05 — Gain spontané

Définition : gain observé alors que l'action en cours ne le ciblait pas explicitement.

La spontanéité décrit la relation entre intention de l'action et observation, non une absence de cause.

Contre-exemple : un gain recherché puis trouvé n'est pas spontané au sens TEBDLC.

Preuve minimale : intention/action documentée antérieurement à l'observation.

## FG-06 — Gain événementiel

Définition : gain dont l'expression ou la validité dépend d'un événement ou d'une fenêtre événementielle définie.

    G(E)=actif/observable lorsque E est satisfait

Il reste un gain même hors événement si son existence est démontrée; son expression peut alors être zéro typé `ZERO_EXPRESSION`.

Contre-exemple : un gain permanent observé pendant un événement n'est pas événementiel par simple coïncidence temporelle.

## FG-07 — Gain proliférable

Définition : gain possédant une capacité démontrée ou candidate à produire des gains descendants sous conditions définies.

Il décrit une capacité potentielle.

    can_proliferate(G)=true

n'implique pas qu'une prolifération a déjà eu lieu.

## FG-08 — Gain de prolifération

Définition : résultat/gain descendant effectivement observé à la suite d'un événement de prolifération.

    PROLIFERATES_TO(Gparent,Gdescendant)

Distinction : `proliférable` = capacité; `proliféré` = occurrence/descendance observée.

Contre-exemple : zéro descendant observé dans une fenêtre n'annule pas la proliférabilité.

## FG-09 — Gain impotent

Définition : gain strictement positif qui, relativement à un seuil entier cible, ne suffit pas à former l'unité suivante.

    G = N + Gi
    0 < Gi < 1
    N + Gi < N+1

L'impotence est relationnelle au seuil, pas à la valeur intrinsèque du gain.

Contre-exemple : `0.999...` à répétition infinie n'est pas un gain impotent car il vaut 1 en mathématiques réelles standards.

## FG-10 — Gain rembourseur

Définition : gain explicitement relié à une dette/perte historique compatible par une relation `REFUNDS`.

    REFUNDS(Gr,D)

Il ne détruit jamais `D`, même si le résultat de solde devient zéro.

Distinction : le gain rembourseur est un opérande historique; le solde est un résultat.

Contre-exemple : un gain de performance ne rembourse pas automatiquement une dette d'intégrité.

## FG-11 — Gain négativement positif

Définition : observation structurée dans laquelle une dimension de gain positive coexiste avec une conséquence négative explicite sur une autre dimension.

Exemple canonique actuel :

    (+2 performance, -8 intégrité)

Aucune soustraction entre les dimensions n'est autorisée. `-8` décrit une mesure/variation externe sur sa dimension; ce n'est pas l'opérateur TEBDLC `G1-G2`.

Contre-exemple : calculer `+2 + (-8) = -6` détruit la séparation des dimensions et est interdit sans règle de conversion dédiée.

## FG-12 — Gain chimère

Définition : résultat consolidé de valeur nulle lorsque la cohérence nécessaire à l'unification de plusieurs observations/gains est réfutée.

    C_H = CONSOLIDE(G1,...,Gn | H)
    invalid(H) => C_H = ZERO_CHIMERA_CONSOLIDATION

Le gain chimère ne signifie pas que les constituants sont faux ou nuls.

Cas d'identité : données de plusieurs personnes fusionnées sous un même profil.

Cas de continuité : événements attribués à une même continuité réelle uniquement parce qu'ils partagent un compte/session apparent.

Non-perte : tous les constituants et la cause de la chimère restent reconstructibles.

## FG-13 — Gain latent

Définition : gain dont l'existence est conservée mais dont l'expression actuelle est nulle ou absente.

    existence(G)>0
    expression(G,t)=ZERO_EXPRESSION

Distinction : latent n'est ni inconnu ni inexistant.

## FG-14 — Gain composite

Définition : gain dont l'existence dépend d'une structure de plusieurs constituants et de leurs relations.

    Gc = COMPOSITION({Gi}, relations, rule)

Aucune somme universelle n'est présupposée.

Contre-exemple : la simple coexistence de deux gains ne prouve pas l'existence d'un gain composite.

## FG-15 — Gain conditionnel

Définition : gain dont la validité ou l'expression est liée à des préconditions explicitement définies.

Il diffère du gain événementiel lorsque la condition n'est pas nécessairement un événement temporel mais un état logique, matériel, juridique ou contextuel.

## FG-16 — Gain de seuil

Définition : gain dont une propriété devient disponible seulement lorsqu'un seuil défini est satisfait.

Le seuil est une relation/condition; il ne doit pas permettre l'arrondi d'un gain impotent à l'unité.

## FG-17 — Gain de couverture

Définition : gain qui augmente ou établit une couverture mesurable d'un support défini.

La valeur de couverture exige le support, pas seulement une fraction.

Deux couvertures ne sont additionnables qu'après traitement explicite de leur intersection.

## FG-18 — Gain de résolution

Définition : gain permettant de distinguer des états auparavant indiscernables dans un domaine défini.

Preuve : existence d'au moins deux états non distinguables avant, distinguables après selon une procédure reproductible.

## FG-19 — Gain d'observabilité

Définition : gain rendant observable/mesurable une propriété auparavant non accessible à une procédure donnée.

Il se distingue du gain de résolution : observer une propriété et distinguer finement plusieurs états ne sont pas la même capacité.

## FG-20 — Gain de contrôlabilité

Définition : gain permettant d'influencer/piloter une propriété dans un domaine où elle pouvait éventuellement déjà être observée.

Contre-exemple : meilleure télémétrie n'implique pas meilleure contrôlabilité.

## FG-21 — Gain de traçabilité

Définition : gain augmentant la capacité à reconstruire provenance, séquence ou causalité documentée d'un état.

Il ne constitue pas lui-même une conclusion causale.

## FG-22 — Gain de reproductibilité

Définition : gain rendant un résultat reproductible sous conditions et procédure explicitement décrites.

La répétition accidentelle d'un résultat n'est pas une preuve suffisante.

## FG-23 — Gain de déterminisme

Définition : gain réduisant l'espace des sorties possibles pour des entrées et conditions équivalentes selon une règle définie.

Il ne signifie pas absence universelle d'aléa.

## FG-24 — Gain de récupération

Définition : gain permettant de reconstruire/restaurer une capacité ou information après une classe définie de perte/corruption.

Il se distingue d'un gain rembourseur : récupération concerne restauration de capacité/information; remboursement concerne relation avec une dette/perte historisée.

## FG-25 — Gain de réversibilité

Définition : gain rendant une transformation inverse démontrable dans un domaine déterminé.

Réversibilité structurelle et équivalence sémantique doivent rester séparées, conformément aux acquis de conservation polymorphe.

## FG-26 — Gain de robustesse

Définition : gain augmentant l'ensemble des perturbations compatibles avec un comportement attendu.

Il se distingue de résilience : robustesse porte sur maintien sous perturbation; résilience porte sur retour après perturbation.

## FG-27 — Gain de résilience

Définition : gain améliorant la capacité de retour à un état fonctionnel après une perturbation définie.

## FG-28 — Gain de tolérance

Définition : gain permettant une continuité fonctionnelle malgré une classe de défaillances explicitement supportée.

Tolérance, robustesse et résilience doivent rester distinctes tant que des tests permettent de les faire varier indépendamment.

## FG-29 — Gain de portabilité

Définition : gain étendant une capacité démontrée à de nouveaux environnements sans présumer l'identité de leur implémentation.

## FG-30 — Gain d'interopérabilité

Définition : gain établissant une interaction fonctionnelle démontrée entre systèmes auparavant non interopérables dans le domaine testé.

## FG-31 — Gain d'indépendance

Définition : gain supprimant la nécessité d'une dépendance précise pour une capacité donnée.

La dépendance historique reste tracée.

## FG-32 — Gain de souveraineté

Définition : gain rendant localement contrôlable une capacité auparavant dépendante d'une autorité ou ressource externe, dans un périmètre explicite.

Il ne s'agit pas d'un jugement politique automatique; le domaine de contrôle doit être démontré.

## FG-33 — Gain d'optionnalité

Définition : gain augmentant le nombre d'alternatives futures réellement accessibles sans obliger une sélection immédiate.

Le simple nombre d'idées non réalisables ne constitue pas de l'optionnalité démontrée.

## FG-34 — Gain de bifurcation

Définition : gain permettant à plusieurs lignées de continuer séparément sans destruction mutuelle de leurs acquis.

## FG-35 — Gain de convergence

Définition : gain permettant à plusieurs lignées distinctes d'atteindre un état compatible commun selon une règle démontrée.

Il ne signifie pas fusion destructive des historiques.

## FG-36 — Gain de recombinaison

Définition : gain émergent d'une composition structurée de constituants préexistants lorsque le résultat possède une propriété non attribuable à un constituant seul.

## FG-37 — Gain de transposition

Définition : gain permettant l'application démontrée d'une capacité à un domaine différent de celui de sa validation initiale.

Il ne doit pas être confondu avec généralisation automatique.

## FG-38 — Gain de généralisation

Définition : gain élargissant le domaine dans lequel une propriété reste démontrée.

## FG-39 — Gain de spécialisation

Définition : gain améliorant ou enrichissant un sous-domaine explicitement circonscrit sans prétendre à une amélioration générale.

## FG-40 — Gain de contextualisation

Définition : gain permettant de sélectionner ou adapter un comportement en fonction d'un contexte explicitement reconnu.

## FG-41 — Gain de confinement

Définition : gain limitant l'étendue d'un effet indésirable à un périmètre plus restreint selon une mesure définie.

Aucune réduction arithmétique de gains n'est impliquée par le mot « limitant ».

## FG-42 — Gain de dégradation gracieuse

Définition : gain permettant de conserver une partie structurée des capacités lorsqu'une condition empêche l'état nominal complet.

Il doit préserver explicitement quelles capacités restent disponibles.

## FG-43 — Gain de preuve

Définition : gain consistant à rendre démontrable une affirmation/capacité auparavant non suffisamment étayée.

La preuve reste une couche distincte; le gain réside dans la nouvelle capacité de démonstration.

## FG-44 — Gain de réfutabilité

Définition : gain rendant une affirmation soumise à une procédure capable de produire un résultat contradictoire vérifiable.

Il ne signifie pas que l'affirmation est réfutée.

## FG-45 — Gain d'invariant

Définition : gain correspondant à l'établissement d'une propriété démontrée stable à travers une famille de transformations.

## FG-46 — Gain de conservation

Définition : gain permettant une transformation nouvelle tout en démontrant la préservation d'un ensemble explicitement protégé de propriétés/gains.

## FG-47 — Gain de récupération d'information

Définition : gain rendant reconstructible une information auparavant inaccessible à partir de traces/provenances conservées.

Il ne réécrit jamais la source comme si l'information avait toujours été directement présente.

## FG-48 — Gain qualitatif non quantifié

Définition : gain dont l'existence et la nature sont démontrées mais pour lequel aucune quantité arithmétique pertinente n'est encore définie.

    G != 0
    quantification(G)=UNQUANTIFIED

Il protège TEBDLC contre la fabrication de scores arbitraires.

## FG-49 — Gain symbolique exact

Définition : gain quantifié par une expression exacte conservée symboliquement lorsque son développement numérique serait inutilement gigantesque.

Exemple :

    (3/10)^1000000

Cette représentation reste exacte et strictement positive sans nécessiter un float ni l'expansion du dénominateur complet pour toutes les opérations de stockage/audit.

## Règle de clôture provisoire

Cette liste n'est pas déclarée exhaustive. Toutefois, tout nouveau type proposé doit démontrer qu'il ne peut pas être représenté correctement par une combinaison des axes ou familles existantes. Sinon il doit être traité comme alias, relation, résultat ou propriété plutôt que comme nouvelle famille.

---

**Jonathan Therrien, Marieville, Québec.**
**TEBDLC — Tous droits réservés sauf autorisation explicite du propriétaire.**