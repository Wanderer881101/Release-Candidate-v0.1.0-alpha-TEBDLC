# MATRICE DE PREUVE R6 — TEBDLC

**Jonathan Therrien, Marieville, Québec.**

Horodatage : 2026-08-19 09:51 America/Montreal
Branche : `proof/r6-executable-invariants`
PR : #4
Thèse de référence : `docs/THESE_ARITHMETIQUE_DES_GAINS_R6_2026-08-19.md`
Registre expérimental détaillé : `docs/THESE_R6_REGISTRE_EXPERIMENTAL_2026-08-19.md`

## 1. Règle de preuve

Cette matrice interdit de confondre :

- preuve mathématique générale;
- preuve par construction de l'API;
- preuve exhaustive sur domaine fini;
- exemple positif;
- contre-exemple;
- test de non-régression;
- validation CI;
- reproductibilité expérimentale.

Un test réussi ne transforme pas automatiquement une hypothèse en théorème général. Les résultats expérimentaux synthétisés ici doivent être lus avec le protocole, l'environnement, les limites et les répétitions détaillés dans le registre expérimental R6.

## 2. Fractionnaire exact — état observé

Corpus exécuté sur un modèle reproduisant exactement les mécanismes publics de `ExactFractionalGain` utilisés par la PR #4 :

- dénominateurs `2..40`;
- tous numérateurs `1..d-1`;
- 780 fractions rationnelles candidates avant répétitions de valeurs réduites;
- 608 400 compositions binaires exécutées par run;
- trois exécutions documentées de la même famille de tests;
- aucune composition égale à zéro;
- aucune composition égale à un;
- toutes les compositions sont strictement inférieures à chacun des deux facteurs positifs strictement fractionnaires;
- aucune divergence logique observée entre RUN-01, RUN-02 et RUN-03.

Statut : **PREUVE EXHAUSTIVE SUR DOMAINE FINI + REPRODUCTIBILITÉ OBSERVÉE**, compatible avec PF-1, PF-2, PF-3, PF-7 et les interdictions de promotion arbitraire.

Ce résultat n'est pas présenté comme preuve exhaustive de tous les rationnels.

## 3. Chaîne profonde

Cas exécuté :

    (3/10)^1000 = 3^1000 / 10^1000

Résultat observé sur les répétitions documentées :

    > 0
    < 1
    != 1

La représentation reste rationnelle exacte; aucun sous-flux flottant n'intervient.

Statut : **TÉMOIN PROFOND FINI / NON-RÉGRESSION / REPRODUCTIBILITÉ OBSERVÉE**.

## 4. Opérateurs interdits

Sur `ExactFractionalGain`, les opérations suivantes lèvent `TypeError` :

    a + b
    a - b
    a / b

La multiplication reste exposée sous condition de composabilité.

Statut : **PREUVE PAR CONSTRUCTION DE L'API ACTUELLE** pour l'interdiction opérationnelle de `+`, `-`, `/` sur cet objet.

Limite : cela ne prouve pas qu'aucun autre chemin dans tout TEBDLC ne puisse réintroduire une opération équivalente; cette propriété doit faire l'objet d'une recherche transversale.

## 5. Frontières de composition

Des gains de même valeur numérique mais de domaine, dimension, unité, référence ou contexte différents sont rejetés à la multiplication.

Statut : **PREUVE PAR TEST DE L'IMPLÉMENTATION ACTUELLE**.

La provenance combinée est dédupliquée et conservée dans le résultat testé.

## 6. Gain impotent — trois régimes de masse

### 6.1. Masse supérieure à 1

    p1 = 300/361
    p2 = 300/361
    M = 600/361 > 1

Résultat :

    unitary_attained = False
    precedence = 45>_TEBDLC46

Statut : **CONTRE-EXEMPLE EXÉCUTABLE REPRODUCTIBLE** à la proposition `masse > 1 => unité`.

### 6.2. Masse égale à 1

    180/361 + 181/361 = 1

Résultat :

    unitary_attained = False

Statut : **CONTRE-EXEMPLE EXÉCUTABLE REPRODUCTIBLE** à la proposition `masse = 1 => unité`.

### 6.3. Masse inférieure à 1

    1/361 + 1/361 = 2/361

Résultat : constituants positifs conservés, aucune unité automatique.

Statut : **TÉMOIN EXÉCUTABLE REPRODUCTIBLE**.

## 7. Répétitions et différences observées

Les répétitions indépendantes RUN-02 et RUN-03 ont produit exactement les mêmes résultats logiques que la baseline RUN-01 pour le domaine testé.

Environnement des répétitions :

    CPython 3.13.5
    Linux 6.18.35 x86_64
    glibc 2.41

Durées observées :

    RUN-02 : 5.313632706 s
    RUN-03 : 5.256784611 s
    delta  : 0.056848095 s

La différence de durée est conservée comme donnée contextuelle, mais elle n'est pas interprétée comme variation de gain faute de métrique de performance et de référentiel explicitement définis.

Statut : **REPRODUCTIBILITÉ LOGIQUE OBSERVÉE SUR DOMAINE FINI**.

Le détail complet du pourquoi, du comment, de l'environnement, des limites et de l'interprétation est conservé dans `docs/THESE_R6_REGISTRE_EXPERIMENTAL_2026-08-19.md`.

## 8. CI GitHub — état distinct

Workflow : `TEBDLC CI`, run `32260311734`.

Les trois jobs Python 3.11, 3.12 et 3.13 terminent en `failure`, mais GitHub renvoie :

    steps = []
    logs = BlobNotFound

Cet état se produit avant qu'une étape exploitable soit observable. Il ne constitue donc ni un PASS ni une preuve d'échec des invariants R6.

Statut : **CI BLOQUÉE / CAUSE NON OBSERVABLE**.

## 9. Ce qui n'est pas encore prouvé

Ne sont notamment pas encore prouvés de bout en bout :

- la totalité de PF-1..PF-7 sur tous les chemins runtime;
- H1..H40;
- EXO-T1..EXO-T5 dans un moteur d'action réel;
- stagnation contextuelle;
- compression/décompression sans perte;
- réactivation/revalidation;
- assimilation comportementale;
- `ΩSt` comme métrique;
- non-pléonasme d'autorité;
- conservation transformationnelle de chaque action du moteur historique;
- absence de chemins indirects permettant une promotion artificielle à l'unité.

Ces éléments doivent être transformés en objets exécutables ou recevoir une preuve formelle avant toute promotion de statut.

## 10. Prochaine couche de preuve

Priorité recommandée : construire un noyau expérimental `ExoState/TransformationRecord/StagnationRecord` sans l'exporter dans l'API publique, puis tester :

    état -> stagnation -> compression -> décompression -> réactivation -> revalidation

avec une condition stricte de reconstruction informationnelle et des contextes d'origine/appel distincts.

Aucune assimilation canonique ne doit avoir lieu tant que les contre-exemples ne sont pas épuisés sur le domaine de test défini.

## 11. Règle de documentation expérimentale

Toute expérience significative appelée à soutenir la thèse doit désormais être accompagnée d'un enregistrement permettant à un tiers de retrouver au minimum : hypothèse visée, commit, environnement, préconditions, générateur/données, procédure, nombre d'itérations, résultat brut, répétitions, différences, contre-exemples, interprétation, limites, statut de preuve et conséquence proposée.

Une conclusion sans protocole reconstructible est une observation insuffisamment documentée, pas une preuve TEBDLC complète.

---

**Jonathan Therrien, Marieville, Québec.**
**TEBDLC — Tout est bon dans le cochon. Tous droits réservés sauf autorisation explicite du propriétaire.**