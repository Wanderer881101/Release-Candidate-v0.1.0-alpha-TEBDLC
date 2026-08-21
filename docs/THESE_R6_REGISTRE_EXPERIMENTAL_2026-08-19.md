# THÈSE R6 — REGISTRE EXPÉRIMENTAL ET REPRODUCTIBILITÉ

**Auteur et propriétaire intellectuel : Jonathan Therrien, Marieville, Québec.**

Projet : TEBDLC — Tout est bon dans le cochon
Référence doctrinale : `docs/THESE_ARITHMETIQUE_DES_GAINS_R6_2026-08-19.md`
Branche d'expérimentation : `proof/r6-executable-invariants`
PR : #4
Date : 2026-08-19
Statut : ANNEXE EXPÉRIMENTALE DE LA THÈSE R6 — les résultats n'élèvent pas automatiquement une hypothèse au rang de théorème général.

## 1. Pourquoi ce registre existe

La thèse TEBDLC doit documenter non seulement les résultats retenus, mais aussi :

- ce qui a été testé;
- pourquoi le test a été construit;
- comment il a été exécuté;
- son domaine exact;
- les résultats obtenus;
- les différences entre répétitions;
- ce que les résultats permettent de conclure;
- ce qu'ils ne permettent pas de conclure;
- les anomalies de l'infrastructure de test;
- les contre-exemples recherchés et non observés dans le domaine testé.

Cette discipline empêche qu'une exécution unique soit transformée en preuve abusive et permet à un professionnel indépendant de reprendre le protocole, le critiquer, le reproduire ou l'étendre.

## 2. Objet du corpus R6-EXE-001

Le corpus `tests/test_r6_executable_proofs.py` éprouve principalement :

1. persistance strictement positive des gains fractionnaires exacts;
2. impossibilité de promotion automatique à l'unité par multiplication;
3. absence des primitives `+`, `-` et `/` sur `ExactFractionalGain`;
4. frontières de composabilité par domaine, dimension, unité, référence et contexte;
5. conservation/déduplication de provenance lors d'une composition;
6. comportement d'une chaîne finie profonde `(3/10)^1000`;
7. distinction entre masse arithmétique descriptive et intégrabilité unitaire pour le gain impotent;
8. cas de masse `<1`, `=1` et `>1` sans promotion automatique de `unitary_attained`.

Le corpus est un mécanisme de falsification : une assertion doit échouer dès qu'un comportement observé contredit la propriété testée.

## 3. Domaine exhaustif fini utilisé

La famille générée est :

    F = { n/d | 2 <= d <= 40 et 1 <= n < d }

Le générateur parcourt 780 couples `(n,d)` avant réduction canonique par `Fraction`.

Chaque élément est composé avec chaque élément :

    780 × 780 = 608 400 compositions binaires

Le domaine est exhaustif **pour ce générateur fini**, mais il n'est pas l'ensemble des rationnels strictement compris entre 0 et 1.

## 4. Environnement des répétitions indépendantes

Exécutions de répétition réalisées dans :

    Python : CPython 3.13.5
    OS : Linux 6.18.35 x86_64, glibc 2.41
    Arithmétique : `fractions.Fraction` exacte

Le protocole reproduit les mécanismes publics utilisés par la branche de preuve : validation `0 < value < 1`, multiplication exacte, composabilité typée, provenance combinée et enveloppe de gain impotent.

La durée murale n'est pas considérée comme invariant. Elle est conservée uniquement comme donnée expérimentale contextuelle.

## 5. Exécution de référence antérieure — RUN-01

La matrice `PROOF_MATRIX_R6_2026-08-19.md` avait enregistré le premier résultat :

    fractions générées : 780
    compositions binaires : 608 400
    violation 0 < produit < 1 : aucune observée
    produit == 0 : aucun observé
    produit == 1 : aucun observé
    produit >= un facteur : aucun observé
    (3/10)^1000 : strictement positif et strictement inférieur à 1
    masse impotente 600/361 : > 1, unitary_attained=False
    masse impotente 361/361 : = 1, unitary_attained=False
    masse impotente 2/361 : < 1, unitary_attained=False

Cette exécution est conservée comme baseline expérimentale de la série.

## 6. Répétition indépendante — RUN-02

Même générateur, mêmes règles, mêmes assertions.

Résultat :

    fractions générées : 780
    compositions binaires : 608 400
    assertions échouées : 0
    contre-exemple fractionnaire trouvé : 0
    résultat chaîne profonde : 3^1000 / 10^1000
    chiffres du numérateur 3^1000 : 478
    chiffres du dénominateur 10^1000 : 1001
    masse >1 : 600/361
    unitary_attained : False
    durée observée : 5.313632706 s

Interprétation : aucun changement logique par rapport à RUN-01 n'a été observé dans le domaine fini testé.

## 7. Répétition indépendante — RUN-03

Même générateur, mêmes règles, mêmes assertions.

Résultat :

    fractions générées : 780
    compositions binaires : 608 400
    assertions échouées : 0
    contre-exemple fractionnaire trouvé : 0
    résultat chaîne profonde : 3^1000 / 10^1000
    chiffres du numérateur 3^1000 : 478
    chiffres du dénominateur 10^1000 : 1001
    masse >1 : 600/361
    unitary_attained : False
    durée observée : 5.256784611 s

Interprétation : aucun changement logique par rapport à RUN-01 ou RUN-02 n'a été observé dans le domaine fini testé.

## 8. Comparaison des trois exécutions

Les résultats déterministes sont identiques sur les trois exécutions documentées :

    nombre de fractions : identique
    nombre de compositions : identique
    ensemble des assertions : identique
    violations observées : aucune
    résultat exact de la chaîne profonde : identique
    masse 600/361 : identique
    statut unitaire : identique

Différence observée entre RUN-02 et RUN-03 :

    temps RUN-02 = 5.313632706 s
    temps RUN-03 = 5.256784611 s
    delta = 0.056848095 s

Cette variation temporelle est attribuable à l'environnement d'exécution et ne modifie aucune valeur mathématique. Elle ne doit pas être assimilée à une variation de gain sans métrique et référentiel de performance explicitement établis.

## 9. Compréhension du résultat

### 9.1. Ce qui est renforcé empiriquement

La répétition renforce la confiance que, pour le domaine fini défini et l'implémentation reproduite :

    0 < a < 1 et 0 < b < 1
    => 0 < a*b < 1

et que la multiplication ne produit ni zéro ni unité dans les 608 400 compositions de chaque exécution.

Elle renforce également le constat que la masse descriptive d'une enveloppe de gains impotents ne suffit pas, dans l'implémentation actuelle, à produire l'unité :

    M < 1  => pas de promotion automatique
    M = 1  => pas de promotion automatique
    M > 1  => pas de promotion automatique

### 9.2. Pourquoi trois résultats identiques ne constituent pas une preuve universelle

La répétition mesure la reproductibilité du protocole dans un environnement et un domaine donnés. Elle ne transforme pas un échantillon fini en démonstration de tous les rationnels ni de tous les chemins logiciels possibles.

La partie mathématique `0<a<1` et `0<b<1 => 0<a*b<1` peut recevoir une preuve générale indépendante des tests. Les tests servent alors à vérifier que l'implémentation respecte cette propriété sur les cas exécutés.

### 9.3. Pourquoi répéter demeure nécessaire

Même lorsqu'une propriété mathématique est démontrable, une implémentation peut diverger à cause de :

- état caché;
- sérialisation;
- cache;
- concurrence;
- ordre d'exécution;
- mutation involontaire;
- dépendance à l'environnement;
- erreur de conversion numérique;
- chemin alternatif non couvert.

La répétition permet donc de distinguer la stabilité observée du simple succès ponctuel.

## 10. Limites actuelles

Ce protocole ne démontre pas encore :

- les propriétés R6 dans tous les modules du dépôt;
- la résistance aux chemins indirects contournant les opérateurs interdits;
- la persistance après sérialisation/désérialisation et snapshots;
- la concurrence ou l'exécution multi-processus;
- la stagnation, compression, décompression, réactivation et revalidation;
- l'assimilation comportementale;
- `ΩSt`;
- EXO-T1 à EXO-T5 de bout en bout;
- H1 à H40 dans leur totalité.

## 11. Incident CI séparé

La CI GitHub de la PR a retourné trois jobs en `failure`, mais les interfaces disponibles ont fourni :

    steps = []
    logs = BlobNotFound

L'absence de logs et de steps exploitables interdit d'attribuer cet état au corpus de preuve ou à une assertion particulière.

Ce résultat est donc classé :

    INFRASTRUCTURE / CAUSE NON OBSERVABLE

et non :

    INVARIANT R6 RÉFUTÉ

## 12. Règle documentaire proposée pour la suite

Chaque expérience significative liée à la thèse doit recevoir un identifiant stable et enregistrer au minimum :

    ID expérience
    hypothèse/invariant visé
    version/commit du code
    environnement
    préconditions
    données/générateur
    procédure
    nombre d'itérations
    résultat brut
    différences entre répétitions
    contre-exemples
    interprétation
    limites
    statut de preuve
    conséquences proposées
    décision d'assimilation ou non-assimilation

Une révision doctrinale ne doit pas citer un résultat expérimental sans permettre de retrouver son protocole et sa généalogie.

## 13. Conclusion expérimentale provisoire

Après trois exécutions documentées de la même famille de tests, aucun écart logique n'a été observé dans le domaine fini défini.

Le statut approprié reste :

    REPRODUCTIBILITÉ OBSERVÉE SUR DOMAINE FINI

et non :

    PREUVE UNIVERSELLE DE R6

La prochaine étape de preuve doit élargir les axes indépendants plutôt que simplement répéter indéfiniment le même domaine : sérialisation, contextes changeants, chemins alternatifs, état transformationnel et cycle exo-sapien.

---

**Jonathan Therrien, Marieville, Québec.**
**TEBDLC — Tout est bon dans le cochon. Tous droits réservés sauf autorisation explicite du propriétaire.**