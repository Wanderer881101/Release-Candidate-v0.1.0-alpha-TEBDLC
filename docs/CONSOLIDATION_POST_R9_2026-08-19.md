# CONSOLIDATION POST-R9 — Registre professionnel de continuité

**Auteur : Jonathan Therrien, Marieville, Québec.**  
Date : 2026-08-19  
Objet : indexer les travaux exécutés après R9 sans écraser leur généalogie ni surévaluer leur niveau de preuve.

## 1. Règle de lecture

Ce registre ne remplace ni les manifestes de jalon, ni les rapports, ni les logs bruts. Il fournit une carte de navigation.

Chaque jalon doit être lu selon quatre questions :

1. qu'est-ce qui a été réellement exécuté ?
2. qu'est-ce qui a été reproduit ?
3. qu'est-ce qui reste seulement candidat ?
4. quelles limites empêchent une généralisation ?

## 2. Jalons consolidés

### R8R9-lab-2026-08-19
Objet : multi-précision, promotion de représentation, reprise exacte et continuation fracto-récursive.

Éléments matériels :
- `c_core/r8r9/`
- `evidence/milestones/R8R9-lab-2026-08-19/`

Gain expérimental : démonstration d'une transition native → capacité → multi-précision → reprise exacte sur scénarios construits.

Limites : corpus fini, dépendance GMP, absence de preuve universelle.

### IMPOTENT-lab-2026-08-19
Objet : séparation masse rationnelle / intégrabilité / statut unitaire.

Éléments matériels :
- `c_core/impotent/`
- `evidence/milestones/IMPOTENT-lab-2026-08-19/`

Gain expérimental : `<1`, `=1`, `>1` restent distincts d'une preuve d'unité.

### STAGNATION-lab-2026-08-19
Objet : stagnation, compression, décompression vérifiée, réactivation et revalidation.

Éléments matériels :
- `c_core/stagnation/`
- `evidence/milestones/STAGNATION-lab-2026-08-19/`

Gain expérimental : conservation du contexte d'origine et refus d'auto-validation lors d'une réactivation.

### impotent-stagnation-recontextualization-2026-08-19
Objet : relier impotence historique U1 à intégrabilité nouvelle U2 sans réécriture rétroactive.

Éléments matériels :
- `c_core/exo/`
- `evidence/milestones/impotent-stagnation-recontextualization-2026-08-19/`

Gain expérimental : `impotent(P,U1)=vrai` peut coexister avec `integrable(P,U2)=vrai` si U2 possède une preuve distincte.

### behavioral-assimilation-2026-08-19
Objet : dériver un modèle comportemental tout en préservant chaque observation.

Éléments matériels :
- `c_core/behavior/`
- `evidence/milestones/behavioral-assimilation-2026-08-19/`

Gain expérimental : `Model(B) != Replacement(B)`; une observation contradictoire non prouvée est refusée; aucune permission d'inférence d'identité.

### reactivation-productivity-factorization-2026-08-19
Objet : distinguer nouveauté productive et répétition exacte tout en conservant les occurrences.

Éléments matériels :
- `c_core/productivity/`
- `evidence/milestones/reactivation-productivity-factorization-2026-08-19/`

Gain expérimental : 102 événements peuvent être représentés par 2 signatures reconstructibles; 100 répétitions identiques restent historiques mais non productives.

### omegast-candidate-2026-08-19
Objet : donner à `ΩSt` une première mesure falsifiable relative à un encodage reconstructible.

Éléments matériels :
- `c_core/omega/`
- `evidence/milestones/omegast-candidate-2026-08-19/`
- `docs/REPORT_OMEGAST_CANDIDATE_2026-08-19.md`

Résultats témoins :
- 1 occurrence / 1 signature : 184 bits;
- 100 occurrences / 1 signature : 976 bits;
- 10 signatures distinctes : 1280 bits;
- 20 signatures distinctes : 2800 bits.

Interprétation permise : une structure fortement répétitive peut être moins coûteuse qu'un nombre plus faible de structures indépendantes dans cet encodage.

Interprétations interdites : complexité de Kolmogorov, malveillance, identité, minimalité universelle.

## 3. Discipline de test commune

Les travaux récents ont utilisé selon leur portée :

- compilations strictes GCC et Clang;
- répétitions indépendantes;
- oracles Python;
- UBSan;
- ASan / détection de fuite;
- corruption volontaire ou scénarios contradictoires;
- conservation des builds refusés par `-Werror` comme incidents antérieurs à l'exécution fonctionnelle.

Un incident d'infrastructure ou de runner ne doit pas être converti en échec logique du noyau sans causalité démontrée.

## 4. Incidents utiles conservés

Plusieurs premières compilations ont été arrêtées par `-Werror` pour des formes C ambiguës, principalement `misleading-indentation` ou déclarations manquantes. Ces incidents sont conservés comme éléments de discipline et ne sont pas comptés comme FAIL fonctionnels puisqu'aucun invariant n'avait encore été exécuté.

Lors du jalon `ΩSt`, les exécutions de l'oracle Python ont aussi produit un bruit de warmup `artifact_tool` après le PASS, avec `exit=0`. Le log local complet le conserve; le résultat TEBDLC est séparé de ce bruit externe.

## 5. Règle de continuité matérielle appliquée

Pour chaque jalon solide, la cible reste :

    source + tests + vecteurs + logs + empreintes + résultats + documentation

Le registre ne doit jamais être utilisé pour déclarer un jalon complet si son manifeste matériel contredit cette affirmation.

## 6. État de la lignée

La progression documentaire devient :

    R4 → R5 → R6 → R7 → R8 → R9 → R10

La progression expérimentale récente devient :

    miroir C borné
      → multi-précision / reprise exacte
      → gain impotent
      → stagnation / compression / réactivation
      → recontextualisation U1→U2
      → assimilation comportementale
      → factorisation de répétitions
      → ΩSt candidat

Aucune flèche ne signifie effacement du nœud précédent.

## 7. Questions encore ouvertes

- définition plus générale et éventuellement plus compacte de `ΩSt`;
- preuve ou réfutation d'une forme d'irréductibilité indépendante de l'encodage choisi;
- confinement généalogique à plus grande échelle;
- revalidation autonome au lieu de preuves injectées par harnais;
- limites et promotion des capacités de provenance/généalogie;
- généralisation multi-architecture et multi-implémentation;
- formalisation de l'associabilité exo-sapienne au-delà des scénarios construits.

Ces questions ne sont ni des pertes ni des défauts cachés : elles constituent explicitement le front de recherche restant.

---

**Jonathan Therrien, Marieville, Québec.**
