# THÈSE DOCUMENTAIRE — Arithmétique des gains et intégrité fractionnaire de TEBDLC

**Auteur et propriétaire intellectuel : Jonathan Therrien, Marieville, Québec.**

Date initiale : 2026-08-18
Révision : R5 — généalogie de recherche exo-sapienne, stagnation et réactivation
Horodatage de révision : 2026-08-19 09:18 America/Montreal
Statut : THÈSE DE TRAVAIL / BASE FORMELLE À TESTER ET APPROFONDIR
Projet : TEBDLC — Tout est bon dans le cochon

## 0. Continuité documentaire R4 → R5 — règle de non-perte

La présente R5 est **cumulative** avec la R4. La R4 complète demeure un ancêtre canonique et reconstructible dans l'historique Git au commit :

    1a8bbe44b8622d2fafeec514041e9f710c73c206

La R4 contient intégralement les sections 1 à 24 : arithmétique fractionnaire exacte, persistance, interdiction de division entre gains, interdiction de l'exposant zéro comme promotion à l'unité, gain négativement positif, gain rembourseur, doctrine corrigée du gain impotent, référentiel `x/N`, relation candidate `>TEBDLC`, familles de gains, provenance/admissibilité, méta-gains, hypothèses H1–H24, catégorie exo-sapienne, non-ivresse contextuelle, révisabilité non destructive, conservation transformationnelle et lois EXO-T1–EXO-T5.

Aucun de ces acquis n'est révoqué par R5. La présente révision ajoute la généalogie des hypothèses explorées depuis R4, y compris celles qui ne sont pas candidates à assimilation.

### 0.1. Incident documentaire de cette révision

Pendant l'écriture de R5, une opération intermédiaire a remplacé momentanément le fichier courant par le texte `PLACEHOLDER` au commit :

    622ba53fad2d2a369bfd70fe0e8031190a43c1a9

Cet état est une **erreur opératoire documentée**, non une révision conceptuelle et non une suppression autorisée de R4. La source R4 est restée reconstructible dans Git et est explicitement ré-ancrée ci-dessus. L'incident est conservé dans la généalogie conformément à :

    rien ne se perd, tout se transforme

Il démontre aussi une limite pratique : une règle de non-perte doit être soutenue par des mécanismes de restauration, pas seulement par une intention documentaire.

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

---

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

---

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

---

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

---

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

---

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

---

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

---

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

---

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

---

## 34. Principe directeur R5

La R5 conserve les principes R4 et ajoute :

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

---

**Jonathan Therrien, Marieville, Québec.**
**TEBDLC — Tout est bon dans le cochon. Tous droits réservés sauf autorisation explicite du propriétaire.**