# THÈSE TEBDLC — R6 CONSOLIDÉE R4 + R5

**Auteur et propriétaire intellectuel : Jonathan Therrien, Marieville, Québec.**

Date initiale de la lignée : 2026-08-18
Révision : R6 — consolidation lossless de R4 et R5
Horodatage : 2026-08-19 09:26 America/Montreal
Statut : THÈSE DE TRAVAIL / CONSOLIDATION GÉNÉALOGIQUE SANS PERTE
Projet : TEBDLC — Tout est bon dans le cochon

## 0. Objet de R6

R6 ne remplace ni ne réécrit rétroactivement R4 ou R5. Elle les **consolide comme deux états généalogiques nécessaires d'une même thèse**.

La règle de construction est :

    R6 = R4 intégrale + ΔR5 intégral + généalogie(R4 → R5 → R6)

avec les contraintes :

    aucune suppression silencieuse;
    aucune correction rétroactive non signalée;
    aucune promotion d'une hypothèse par simple consolidation;
    aucune perte des erreurs documentées;
    aucune perte des statuts épistémiques;
    aucune perte des contre-exemples;
    aucune perte des questions ouvertes.

La consolidation est **référentielle et cryptographiquement ancrée dans Git**, plutôt qu'une recopie manuelle susceptible d'introduire une nouvelle perte. Les deux constituants canoniques sont identifiés par leurs commits et blobs Git.

## 1. Constituant R4 — baseline doctrinale intégrale

R4 canonique :

    commit = 1a8bbe44b8622d2fafeec514041e9f710c73c206
    blob   = 38de08f7fc76257eb1e758ca56b726acb4139a5c
    fichier = docs/THESE_ARITHMETIQUE_DES_GAINS_2026-08-18.md

R4 demeure la source normative intégrale de ses sections 1 à 24.

Elle contient notamment, sans que cette énumération remplace son contenu :

- arithmétique fractionnaire exacte;
- persistance fractionnaire;
- notation candidate `0⁺ ⟪ I_f ⟫ 1`;
- fraction contextualisée;
- distinction représentation rationnelle / division opérationnelle;
- interdiction de la division entre gains comme primitive;
- interdiction de l'exposant zéro comme mécanisme de promotion vers l'unité;
- gain négativement positif;
- gain rembourseur;
- doctrine corrigée du gain impotent;
- séparation masse arithmétique / intégrabilité unitaire;
- référentiel général `x/N`, avec `361` comme exemple non universel;
- relation candidate `45 >TEBDLC 46` comme ordre d'intégration et non ordre numérique;
- association alternative des gains impotents;
- familles de gains;
- provenance, légitimité et admissibilité;
- méta-gains;
- contraintes numériques d'implémentation;
- hypothèses H1 à H17;
- architecture TEBDLC pré-algébrique;
- catégorie exo-sapienne;
- expansion sans validation automatique;
- non-ivresse contextuelle;
- révisabilité non destructive;
- principe `rien ne se perd, tout se transforme`;
- conservation transformationnelle;
- émergence conservatrice;
- logique d'action transformationnelle;
- lois EXO-T1 à EXO-T5;
- hypothèses H18 à H24;
- principe directeur enrichi R4.

**Règle R6-R4-1 :** toute lecture de R6 doit considérer le contenu exact du blob R4 ci-dessus comme incorporé à R6 sans modification.

**Règle R6-R4-2 :** un résumé, un index ou une reformulation de R4 dans R6 ne remplace jamais R4.

## 2. Constituant R5 — delta généalogique intégral

R5 canonique :

    commit = b8296c6272a9acf5ef5957506b020c406b0f51b3
    blob   = 0509935d0025face479f802a43c521c9e3237c87
    fichier = docs/THESE_ARITHMETIQUE_DES_GAINS_2026-08-18.md

R5 doit être interprétée comme **delta généalogique post-R4**, et non comme remplacement matériel légitime des sections R4 absentes de son fichier courant.

R5 conserve notamment :

- la classification `ACQUIS / CANDIDAT / HYPOTHÈSE EXPLORATOIRE / HYPOTHÈSE NON-CANDIDATE / HYPOTHÈSE RÉFUTÉE-INSUFFISANTE / QUESTION OUVERTE / TRANSFORMATION`;
- la règle `conservation documentaire ≠ validation`;
- objet rencontré hors référentiel;
- suspension productive;
- expansion référentielle;
- associabilité exo-sapienne;
- « gain catalytique » comme nom non adopté;
- extension de l'anti-pléonasme aux responsabilités et autorités;
- distinction `Observation ≠ Preuve ≠ Décision ≠ Action`;
- correction du miroir de fusion vers la stagnation de séparation;
- distinction frontière logique / frontière d'exécution comme question ouverte;
- stagnation contextuelle;
- insuffisance du simple nombre de stagnations comme mesure de coût;
- `ΩSt` comme hypothèse exploratoire de complexité stagnante irréductible;
- limites d'interprétation de la stagnation comme comportement malveillant;
- confinement généalogique;
- compression et décompression sans perte;
- réactivation et revalidation dans le nouveau contexte d'appel;
- assimilation comportementale distincte de l'assimilation du gain;
- hypothèses non-candidates et erreurs utiles;
- hypothèses H25 à H40;
- principe directeur R5.

**Règle R6-R5-1 :** toute lecture de R6 doit considérer le contenu exact du blob R5 ci-dessus comme incorporé à R6 en tant que delta historique et conceptuel post-R4.

**Règle R6-R5-2 :** lorsqu'une formulation R5 est explicitement marquée comme correction, transformation, réfutation ou insuffisance d'une formulation antérieure, les deux états sont conservés avec leur relation généalogique; le nouvel état ne fait pas disparaître l'ancien.

## 3. Incident PLACEHOLDER — conservation sans promotion

L'état intermédiaire :

    commit = 622ba53fad2d2a369bfd70fe0e8031190a43c1a9
    contenu = PLACEHOLDER

est conservé comme **incident opératoire**, pas comme révision doctrinale.

Il appartient à la généalogie parce qu'il a réellement existé, mais :

    incident documentaire ≠ doctrine;
    conservation de l'incident ≠ validation de l'incident;
    existence historique ≠ autorité conceptuelle.

R6 utilise cet incident comme preuve pratique qu'une politique de non-perte doit être soutenue par une reconstruction vérifiable et non par la seule intention.

## 4. Ordre d'autorité généalogique

Pour reconstruire la thèse R6 :

1. charger exactement R4 depuis son commit/blob canonique;
2. conserver R4 comme baseline intégrale;
3. charger exactement R5 depuis son commit/blob canonique;
4. interpréter R5 comme delta généalogique post-R4;
5. appliquer uniquement les corrections explicitement documentées comme telles;
6. conserver les formulations antérieures lorsqu'elles servent à expliquer le cheminement;
7. conserver les statuts épistémiques de R5;
8. ne jamais transformer une hypothèse en acquis par simple juxtaposition;
9. conserver les contradictions apparentes jusqu'à résolution explicite;
10. produire l'état de travail R6 sans effacer ses deux parents conceptuels.

## 5. Sémantique de « consolidation »

Dans R6 :

    consolidation ≠ écrasement
    consolidation ≠ concaténation aveugle
    consolidation ≠ sélection arbitraire
    consolidation ≠ réécriture rétroactive

La consolidation signifie :

    conservation intégrale des sources
    + relations généalogiques explicites
    + statuts épistémiques conservés
    + corrections explicitement orientées
    + capacité de reconstruction

Cette définition est cohérente avec :

    rien ne se perd, tout se transforme.

## 6. Invariant de non-perte R6

On pose comme invariant documentaire de cette révision :

    ∀ x ∈ R4, x reste reconstructible depuis R6
    ∀ y ∈ ΔR5, y reste reconstructible depuis R6

et :

    R6 ne peut déclarer absent un élément uniquement parce qu'il n'est pas recopié textuellement dans ce manifeste.

L'incorporation par référence Git exacte est volontaire : elle évite qu'une nouvelle copie manuelle imparfaite devienne une troisième variante silencieuse.

## 7. Relation R4 / R5 / R6

La lignée est :

    R4 --[exploration, corrections, nouvelles hypothèses]--> R5

puis :

    {R4 intégrale, ΔR5 intégral} --[consolidation généalogique]--> R6

R6 est donc un **état composite reconstructible**, et non une prétention que R4 et R5 avaient toujours dit exactement la même chose.

Lorsque R5 démontre qu'une compréhension R4 ou post-R4 était incomplète, R6 conserve :

    état antérieur
    + raison de l'état antérieur
    + découverte/contre-exemple
    + transformation
    + état courant

## 8. Baseline de poursuite

À partir de cette révision, le développement peut utiliser R6 comme point d'entrée documentaire, avec les règles suivantes :

- R4 reste intégralement normative pour son contenu non transformé;
- R5 reste intégralement informative et normative selon le statut explicite de chaque élément;
- les hypothèses restent des hypothèses;
- les non-candidats restent documentés sans être assimilés;
- les erreurs utiles restent visibles;
- les questions ouvertes restent ouvertes;
- toute future R7 doit conserver la généalogie R4 → R5 → R6;
- aucune modification d'un acquis déjà établi ne doit être faite silencieusement ou sans la gouvernance prévue.

## 9. Principe directeur R6

    R6 = conservation(R4) + conservation(ΔR5) + généalogie + reconstructibilité

Cette expression est sémantique et ne constitue pas une addition primitive de gains.

La R6 ne prétend pas que tout a été compris à chaque étape. Elle garantit au contraire que les incompréhensions, corrections, hypothèses, contre-exemples et transformations utiles restent disponibles pour comprendre pourquoi TEBDLC est arrivé à son état actuel.

---

**Jonathan Therrien, Marieville, Québec.**
**TEBDLC — Tout est bon dans le cochon. Tous droits réservés sauf autorisation explicite du propriétaire.**