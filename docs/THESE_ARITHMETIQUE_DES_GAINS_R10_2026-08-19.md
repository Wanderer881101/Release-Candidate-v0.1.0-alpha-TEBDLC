# THÈSE DOCUMENTAIRE R10 — Consolidation expérimentale post-R9

**Auteur et propriétaire intellectuel : Jonathan Therrien, Marieville, Québec.**

Date : 2026-08-19  
Révision : R10 — extension cumulative de R9  
Statut : THÈSE DE TRAVAIL CONSOLIDÉE / PREUVES EXPÉRIMENTALES PARTIELLES  
Projet : TEBDLC — Tout est bon dans le cochon

## 0. Doctrine R10 — aucune perte de gain historique

R10 ne remplace, ne corrige silencieusement et n'écrase aucune révision antérieure. R4 à R9 restent des ancêtres matériels et documentaires. R10 ajoute les résultats obtenus après R9 dans le laboratoire de session puis persistés dans le dépôt.

    R10 = R9 + preuves_R8R9 + impotence_exécutable + stagnation_exécutable
          + recontextualisation + assimilation_comportementale
          + factorisation_productivité + ΩSt_candidat

avec :

    preuve_sur_scenario ≠ preuve_universelle
    reproductibilité ≠ vérité_absolue
    nouveau_contexte ≠ réécriture_du_passé
    modèle ≠ observations
    factorisation ≠ effacement
    mesure_candidate ≠ métrique_canonique

## 1. Passage R8/R9 de doctrine à témoin exécutable

Le noyau C expérimental a été étendu avec une représentation multi-précision GMP afin de rendre exécutable le cycle R8 :

    capacité_native
      → détection_anticipée
      → état_typé
      → promotion
      → reprise_exacte
      → continuation

Sur la branche témoin `(3/10)^n`, la représentation native reste valide jusqu'à la profondeur 19 et exige une promotion à la profondeur 20. La continuation multi-précision atteint la profondeur 1000 avec valeur exacte `3^1000/10^1000`, sans conversion flottante.

Ce résultat soutient expérimentalement, dans le domaine testé :

- distinction valeur/représentation/capacité;
- interruption avant corruption;
- reprise depuis les opérandes exacts;
- continuation fracto-récursive après transformation de représentation;
- conservation de généalogie sur la branche testée.

Il ne prouve pas que toute implémentation future ou toute architecture de représentation préservera ces propriétés.

## 2. Gain impotent exécutable

La doctrine IMP a été matérialisée avec masse rationnelle exacte séparée du statut d'intégrabilité.

Cas témoins :

    200/361 < 1
    361/361 = 1
    600/361 > 1

Dans les trois cas, l'unité n'est pas promue automatiquement :

    masse_arithmétique ⇏ unité

La preuve d'intégrabilité reste une information distincte. Le moteur refuse également de produire une consolidation descriptive lorsqu'un contexte requis n'est pas compatible.

Ce jalon soutient particulièrement IMP-4, IMP-5, IMP-6 et IMP-11 sur les scénarios construits.

## 3. Stagnation, compression et réactivation exécutables

Le cycle suivant possède maintenant un témoin C :

    STAGNATED
      → COMPRESSED
      → DECOMPRESSED_verified
      → REACTIVATED
      → REVALIDATION_REQUIRED
      → REVALIDATED ou STAGNATED

La stagnation ne transforme jamais l'objet en zéro ni en absence. La compression testée conserve une forme canonique vérifiable. La décompression contrôle la reconstruction et une corruption volontaire est refusée.

Le contexte d'origine est conservé lors d'un appel depuis un nouveau contexte :

    C_origine ≠ C_appel

et :

    Reactivate(St,C_appel) ⇒ REVALIDATION_REQUIRED

La réactivation ne réutilise donc pas l'ancien résultat comme preuve automatique.

## 4. Raccord gain impotent + stagnation + recontextualisation

Un ensemble témoin de masse :

    300/361 + 300/361 = 600/361 > 1

reste impotent relativement à `U1`. Ses constituants peuvent être stagnés, compressés, reconstruits et réactivés dans un nouveau contexte visant `U2`.

Deux vérités sont alors conservables simultanément :

    impotent(P,U1) = vrai
    integrable(P,U2) = vrai

si et seulement si la seconde est accompagnée d'une preuve d'intégrabilité distincte et suffisante.

La nouvelle intégrabilité ne modifie pas l'historique U1 :

    nouvelle_intégrabilité ≠ réécriture_historique

Ce raccord matérialise une partie de l'associabilité exo-sapienne déjà envisagée en R6.

## 5. Assimilation comportementale sans assimilation du gain

Un historique comportemental exécutable a été construit avec plusieurs contextes et résultats : stagnation, preuves refusées et intégrabilité démontrée.

Le modèle dérivé conserve les observations sources. Il ne les remplace pas et ne possède aucune permission d'inférer une identité de personne ou de source.

    Model(B) ≠ Replacement(B)
    similarité(B1,B2) ⇏ identité(source1,source2)

Une observation contradictoire tentant de déclarer `INTEGRABLE` avec preuve incomplète est refusée au lieu d'être normalisée ou d'altérer les observations précédentes.

Ce jalon soutient H37 et une partie de H38, sans transformer une signature comportementale en preuve d'identité.

## 6. Productivité des réactivations répétées

Un ledger de factorisation sans perte a été ajouté afin qu'une répétition exacte ne soit pas interprétée comme une nouveauté productive.

Scénario témoin :

    102 événements
    2 signatures distinctes
    100 répétitions non productives
    2 premières occurrences productives

La factorisation conserve les identifiants de séquence permettant de reconstruire les occurrences :

    factorisation ≠ suppression
    répétition_exacte ≠ nouveau_gain

Une nouvelle signature redevient productive relativement à l'espace déjà observé.

## 7. Première mesure falsifiable de ΩSt

R6 conservait :

    ΩSt = complexité stagnante irréductible

comme hypothèse exploratoire non définie. R10 conserve cette généalogie et introduit uniquement une première mesure candidate, relative à un encodage déterminé.

Après factorisation sans perte, l'encodage candidat compte :

- les bits nécessaires à la structure de chaque facteur;
- les bits nécessaires à ses occurrences reconstructibles, codées par multiplicité et deltas ULEB128.

    ΩSt_candidate_bits = structural_bits + occurrence_bits

Résultats témoins :

    1 occurrence / 1 signature     = 184 bits
    100 occurrences / 1 signature = 976 bits
    10 signatures distinctes      = 1280 bits
    20 signatures distinctes      = 2800 bits

Les 99 répétitions supplémentaires de la même signature ajoutent 792 bits dans cet encodage, alors qu'un stockage naïf de 99 identifiants 64-bit en demanderait 6336.

Cela soutient H33 sous une forme expérimentale limitée : le coût de représentation dépend de la structure non factorisée et non du seul nombre brut d'occurrences.

Toute séquence non strictement croissante ou ambiguë est refusée afin de ne pas gagner artificiellement en compacité en perdant la reconstructibilité.

### 7.1. Statut exact de ΩSt

`ΩSt_candidate_bits` n'est pas :

- une complexité de Kolmogorov;
- une preuve de minimalité globale;
- une métrique de culpabilité ou de malveillance;
- une preuve d'identité;
- une métrique canonique définitive de TEBDLC.

Il s'agit d'une première grandeur définie, reproductible et falsifiable pour comparer un encodage reconstructible donné.

## 8. Discipline expérimentale commune

Les jalons post-R9 ont été soumis, selon leur portée, à plusieurs exécutions GCC et Clang, à des oracles Python indépendants et à des sanitizers. Les incidents de build causés par `-Werror` sont conservés comme incidents de forme lorsque les tests fonctionnels n'avaient pas encore été exécutés.

La répétition d'un PASS ne transforme pas un domaine fini en preuve universelle. R10 impose donc les statuts suivants :

- `EXECUTED` : scénario effectivement exécuté;
- `REPRODUCED` : résultat reproduit plusieurs fois dans l'environnement déclaré;
- `CROSS_CHECKED` : résultat confronté à au moins une implémentation/oracle indépendant;
- `SANITIZED` : chemin testé sous sanitizer déclaré;
- `CANDIDATE` : définition suffisamment précise pour falsification;
- `UNIVERSAL_UNPROVEN` : aucune généralisation universelle autorisée.

## 9. Continuité matérielle

Chaque jalon solide doit respecter la règle déjà introduite :

    code + tests + vecteurs + logs + empreintes + résultats + documentation

L'absence d'une famille obligatoire interdit de prétendre à une continuité matérielle complète entre sessions.

Les jalons post-R9 sont indexés dans :

    evidence/milestones/

et leur généalogie est résumée dans :

    docs/CONSOLIDATION_POST_R9_2026-08-19.md

## 10. Hypothèses transformées mais non canonisées

Les résultats post-R9 changent le statut expérimental de plusieurs idées sans les rendre universelles :

- H33 : reçoit un témoin quantitatif candidat via `ΩSt_candidate_bits`;
- H34 : reçoit des scénarios de compression/décompression reconstructibles;
- H35 : reçoit un témoin imposant revalidation après réactivation;
- H36 : reçoit un scénario où U2 devient intégrable sans effacement de U1;
- H37 : reçoit un modèle comportemental qui ne remplace pas ses observations;
- H38 : reçoit une couche analytique explicitement non identitaire;
- H40 : reçoit plusieurs cycles transformationnels de bout en bout sur scénarios construits;
- H67/H69 : reçoivent des témoins multi-précision/fracto-récursifs;
- H71 : reçoit des tests de distinction valeur/généalogie dans les travaux R8/R9.

Le statut correct reste : `SOUTENU EXPÉRIMENTALEMENT DANS LE DOMAINE TESTÉ`, jamais `PROUVÉ UNIVERSELLEMENT`.

## 11. Limites conservées

R10 conserve explicitement les limites suivantes :

1. les corpus demeurent finis;
2. une seule famille d'architectures matérielles a été utilisée dans le lab actuel;
3. GMP et les représentations actuelles introduisent leurs propres bornes matérielles;
4. les preuves de recontextualisation sont fournies par des scénarios construits et non dérivées autonomement;
5. le ledger de productivité est borné en facteurs et occurrences;
6. `ΩSt_candidate_bits` dépend de son encodage et n'est pas minimal par définition;
7. les notions exo-sapiennes plus larges ne sont pas assimilées par ces seuls résultats;
8. aucune mesure comportementale ne doit être utilisée comme attribution d'identité sans preuve indépendante;
9. les incidents du runner et des outils sont distingués des résultats TEBDLC.

## 12. Principe directeur R10

La lignée peut maintenant être formulée :

    rien ne se perd, tout se transforme;
    transformation ≠ réécriture;
    représentation ≠ valeur;
    masse ≠ intégrabilité;
    stagnation ≠ disparition;
    compression ≠ effacement;
    réactivation ≠ auto-validation;
    nouveau contexte ≠ souveraineté rétroactive;
    modèle ≠ observations;
    répétition ≠ nouveauté;
    factorisation ≠ perte;
    mesure ≠ vérité universelle;
    preuve locale ≠ preuve générale.

R10 devient la révision cumulative décrivant l'état expérimental atteint après R9. R9 et toutes les révisions antérieures restent des ancêtres reconstructibles et ne sont pas modifiées rétroactivement.

---

**Jonathan Therrien, Marieville, Québec.**  
**TEBDLC — Tout est bon dans le cochon. Tous droits réservés sauf autorisation explicite du propriétaire.**
