# THÈSE DOCUMENTAIRE R8 — Miroir sémantique C, états de capacité et reprise exacte

**Auteur et propriétaire intellectuel : Jonathan Therrien, Marieville, Québec.**

Date initiale de la lignée : 2026-08-18  
Révision : R8 — extension cumulative de R7  
Horodatage : 2026-08-19 12:00 America/Montreal  
Statut : THÈSE DE TRAVAIL / DOCTRINE D'IMPLÉMENTATION À PROUVER  
Projet : TEBDLC — Tout est bon dans le cochon

## 0. Doctrine R8 — continuité et non-perte

R8 ne modifie, ne remplace et n'écrase pas R7. Elle ajoute une doctrine spécifique de miroir sémantique C et de gestion non destructive des limites de représentation.

Ancêtre documentaire immédiat :

    docs/THESE_ARITHMETIQUE_DES_GAINS_R7_2026-08-19.md

Ancêtres conservés : R6, R5, R4 et l'ensemble de la généalogie documentée antérieurement.

    R8 = R7 + delta_capacité_et_miroir_C
    extension ≠ remplacement
    erreur_de_capacité ≠ perte_du_gain
    changement_de_représentation ≠ changement_de_valeur
    reprise_exacte ≠ recalcul_approximatif

Toutes les hypothèses, lois, contre-exemples, erreurs historiques, questions ouvertes et statuts antérieurs restent inchangés sauf lorsqu'une future révision explicitement autorisée les transforme.

---

## 57. Miroir exact : exactitude sémantique, pas identité mémoire

Le miroir C doit viser :

    Sem(C) ≡ Sem(Python-reference)

sur le sous-ensemble TEBDLC testé.

Il ne doit pas viser :

    Representation(C) = Representation(Python)

Python peut employer des entiers arbitraires et des objets dynamiques. Le C peut employer une représentation interne différente, à condition que la valeur, les contraintes, les interdictions, le contexte, la provenance, la généalogie et le résultat canonique demeurent sémantiquement équivalents.

L'exactitude du miroir est donc une propriété observable de comportement et de conservation, non une exigence de disposition mémoire identique.

## 58. Séparation valeur / représentation / capacité

R8 distingue trois niveaux :

    VALUE         = valeur mathématique/sémantique TEBDLC
    REPRESENTATION = forme interne utilisée pour porter VALUE
    CAPACITY      = capacité de REPRESENTATION à porter VALUE exactement

Ainsi :

    valeur inchangée + représentation changée

est un cas valide.

Inversement :

    représentation inchangée + valeur tronquée

est une violation.

Invariant candidat :

    changement_de_représentation ⇏ changement_de_valeur

## 59. Overflow : événement de capacité, pas résultat numérique

Un dépassement de capacité ne doit jamais produire une valeur numérique valide par défaut.

Interdit :

    overflow_machine → wraparound
    overflow_machine → troncature
    overflow_machine → approximation silencieuse
    overflow_machine → zéro
    overflow_machine → unité

Admis comme modèle candidat :

    opération(A,B)
      → capacité_insuffisante
      → état typé
      → expansion de représentation
      → reprise exacte
      → résultat exact

L'overflow devient donc un événement de représentation et de capacité, pas une valeur du domaine des gains.

## 60. Anticipation avant opération dangereuse

Lorsque le coût ou la taille du résultat peut être déterminé avant l'opération, le Core C doit préférer l'anticipation à la détection après corruption.

Exemple conceptuel :

    required_bits(product) > available_bits

entraîne :

    CAPACITY_EXPANSION_REQUIRED

avant d'exécuter une multiplication bornée susceptible de déborder.

R8 privilégie donc :

    overflow_anticipé
      → état_de_capacité

plutôt que :

    overflow_provoqué
      → tentative_de_récupération

Cette préférence n'interdit pas les contrôles post-opération lorsque la plateforme, la primitive ou la bibliothèque impose une autre stratégie; elle interdit seulement de considérer une corruption intermédiaire comme acceptable.

## 61. États de capacité typés

Une interface candidate peut distinguer, au minimum :

    TEBDLC_OK
    TEBDLC_CAPACITY_EXPANSION_REQUIRED
    TEBDLC_CAPACITY_UNRESOLVED
    TEBDLC_FORBIDDEN_OPERATION
    TEBDLC_INCOMPATIBLE_CONTEXT
    TEBDLC_INVALID_REPRESENTATION
    TEBDLC_INTERNAL_INVARIANT_VIOLATION

Ces noms ne constituent pas encore une ABI canonique.

Un état de capacité doit être accompagné, lorsque pertinent, de :

- l'opération demandée;
- la représentation courante;
- la capacité disponible;
- la capacité estimée/requise;
- les opérandes ou références reconstructibles vers eux;
- le contexte;
- la provenance;
- la généalogie;
- la tentative de transformation de représentation;
- le résultat de cette tentative.

L'état d'erreur ne doit donc jamais être un simple entier opaque dépourvu de contexte.

## 62. Promotion de représentation sans perte

Une trajectoire admissible peut être :

    SMALL_INT
      → WIDER_INT
      → MULTI_PRECISION

à condition que chaque transition conserve exactement la valeur.

Pour une fraction :

    p/q

la transformation de représentation peut modifier la manière de stocker `p` et `q`, mais doit préserver :

    p_exact
    q_exact
    gcd-normalisation
    signe
    domaine
    dimension
    unité
    référence
    contexte
    provenance
    généalogie

Aucune promotion de représentation ne peut autoriser une réduction sémantique des métadonnées requises.

## 63. Reprise exacte

Après expansion de capacité, l'opération doit être reprise depuis des opérandes exacts/reconstructibles.

Le schéma candidat est :

    O = Operation(A,B)

si capacité insuffisante :

    E = CapacityEvent(A,B,O,representation_old)
    representation_old → representation_new
    R = ReExecuteExact(A,B,O,representation_new)

La reprise ne doit pas dépendre d'un résultat partiellement calculé ayant déjà subi une perte.

Ainsi :

    reprise_exacte ≠ continuation_depuis_valeur_corrompue

## 64. Cas témoin : (3/10)^1000

Le cas :

    (3/10)^1000 = 3^1000 / 10^1000

sert de témoin de capacité.

Un miroir C conforme ne peut pas déclarer la valeur non représentable simplement parce qu'un entier machine borné est insuffisant, si une représentation multi-précision autorisée est disponible.

Le comportement attendu devient conceptuellement :

    capacité_native insuffisante
      → promotion_multi_precision
      → résultat_exact

avec :

    résultat > 0
    résultat < 1
    résultat ≠ 0
    résultat ≠ 1

## 65. Une erreur de capacité peut être un état productif

R8 distingue :

    ERROR_capacity ≠ gain

mais aussi :

    ERROR_capacity ≠ perte_du_gain

L'événement de capacité peut produire des informations utiles :

- seuil de représentation atteint;
- besoin de promotion;
- coût réel de l'opération;
- comportement de la plateforme;
- validation d'un mécanisme de reprise;
- preuve qu'une représentation bornée est insuffisante.

Ces informations peuvent devenir des gains analytiques distincts si elles satisfont les règles TEBDLC; l'erreur elle-même ne devient pas automatiquement un gain.

## 66. Échec non résolu

Si aucune représentation autorisée ou disponible ne permet la poursuite exacte :

    CAPACITY_EXPANSION_REQUIRED
      → tentative_expansion
      → CAPACITY_UNRESOLVED

La valeur initiale et les opérandes doivent rester reconstructibles.

Le système ne doit pas fabriquer un résultat de substitution.

    CAPACITY_UNRESOLVED ⇏ 0
    CAPACITY_UNRESOLVED ⇏ approximation
    CAPACITY_UNRESOLVED ⇏ unité

L'état signifie seulement : le calcul exact demandé n'a pas pu être produit dans les capacités autorisées de cette exécution.

## 67. Conservation de provenance pendant la promotion

Une transformation de représentation doit être ajoutée à la généalogie :

    Representation_A
      --[raison: capacité]-->
    Representation_B

Le résultat final doit permettre de reconstruire :

- quelle représentation a été utilisée initialement;
- pourquoi elle était insuffisante;
- quelle représentation l'a remplacée;
- si la valeur a été recalculée ou migrée;
- les vérifications d'intégrité effectuées;
- le contexte et les versions de composants impliqués.

La promotion de capacité devient ainsi une transformation TEBDLC auditable.

## 68. Miroir Python/C et divergence

Pour toute entrée canonique `X` dans le domaine commun :

    R_P = PythonReference(X)
    R_C = CoreC(X)

Condition candidate :

    Canon(R_P) = Canon(R_C)

Si le C exige une promotion de capacité mais Python non, cela ne constitue pas une divergence sémantique si les deux résultats finaux canoniques sont équivalents et si la promotion C est correctement documentée.

La divergence de représentation doit donc être distinguée de la divergence de valeur :

    representation_P ≠ representation_C

peut être acceptable;

    value_P ≠ value_C

ne l'est pas sans explication conforme à la spécification.

## 69. Tests de seuil et tests de transition

R8 exige des tests construits autour des frontières de capacité, pas uniquement des valeurs ordinaires.

Le futur corpus doit inclure :

- valeur maximale exactement représentable dans chaque classe bornée;
- première valeur nécessitant promotion;
- produit juste avant overflow;
- produit juste après seuil de capacité;
- numérateurs très grands;
- dénominateurs très grands;
- chaînes profondes;
- répétition après promotion;
- sérialisation/désérialisation après promotion;
- provenance avant/après promotion;
- comparaison Python/C après chaque transition.

Chaque test doit être répété et documenté selon la discipline expérimentale établie en R6/R7.

## 70. Tests de corruption interdite

Le banc de preuve doit tenter explicitement de provoquer :

- wraparound signé/non signé;
- troncature lors de conversion;
- perte de bits;
- perte de signe;
- dénominateur nul après conversion;
- normalisation incorrecte;
- perte de provenance pendant allocation/reallocation;
- utilisation d'un résultat partiel après détection d'overflow;
- fallback flottant silencieux;
- réduction d'une erreur de capacité à zéro.

Un seul de ces cas observé dans un chemin déclaré conforme doit provoquer un échec de conformité.

## 71. Discipline mémoire associée

La multi-précision impose une gestion mémoire rigoureuse.

R8 n'assimile pas l'augmentation de capacité numérique à une autorisation d'allocation illimitée non contrôlée.

Le Core C devra distinguer :

    impossibilité_mathématique
    impossibilité_de_capacité_autorisée
    échec_d'allocation
    limite_de_politique
    erreur_interne

Ces états ne doivent pas être fusionnés sous un même code générique si leur distinction est nécessaire à la reconstruction et à la décision.

## 72. Critères de conformité du miroir C

Pour le sous-ensemble testé, un miroir C candidat ne peut être déclaré conforme que s'il démontre notamment :

1. exactitude de valeur;
2. conservation du contexte;
3. conservation de provenance;
4. conservation de généalogie;
5. refus des opérations interdites;
6. absence de promotion artificielle à l'unité;
7. absence de perte vers zéro;
8. transitions de capacité explicites;
9. aucune corruption intermédiaire réutilisée;
10. reprise exacte après promotion;
11. sérialisation canonique cohérente;
12. divergence avec Python enregistrée et investigable;
13. répétabilité sur les mêmes entrées;
14. comportement défini sous plusieurs compilateurs/options lorsque testés.

## 73. Hypothèses R8 — H53 à H64

H53. Une implémentation C peut être un miroir sémantiquement exact d'un modèle Python sans employer les mêmes représentations mémoire.

H54. Une limite de capacité de représentation peut être traitée comme état typé sans perdre la valeur ou la provenance des opérandes.

H55. Une promotion de représentation peut préserver exactement la valeur tout en modifiant la structure interne.

H56. L'anticipation de capacité avant une opération réduit le risque de corruption silencieuse par rapport à une stratégie qui dépend seulement de la détection après débordement.

H57. Une reprise exacte après promotion doit repartir d'opérandes exacts ou reconstructibles plutôt que d'une valeur partiellement corrompue.

H58. Une divergence de représentation entre Python et C peut être acceptable lorsque leur sémantique canonique finale est équivalente.

H59. Un état `CAPACITY_UNRESOLVED` peut préserver l'intégrité documentaire d'un calcul non produit sans fabriquer de valeur de substitution.

H60. Les transitions de capacité doivent être généalogiquement enregistrées comme transformations TEBDLC.

H61. Les tests de seuil sont nécessaires pour détecter des pertes que des tests centrés sur des valeurs ordinaires peuvent manquer.

H62. Un fallback flottant silencieux après dépassement de capacité viole les invariants fractionnaires exacts.

H63. Les erreurs d'allocation, limites politiques, impossibilités de représentation autorisée et erreurs internes doivent rester distinguables lorsqu'elles ont des conséquences différentes.

H64. Le couple `Python-reference + Core-C` peut fournir une validation différentielle plus riche si les divergences de représentation sont séparées des divergences sémantiques.

Aucune hypothèse H53–H64 n'est assimilée automatiquement.

## 74. Protocole expérimental R8

Le premier protocole R8 devra :

1. définir une petite représentation C bornée volontairement;
2. définir une représentation C multi-précision candidate;
3. exécuter les mêmes vecteurs Python sur les deux;
4. provoquer volontairement les seuils de capacité bornée;
5. vérifier que le seuil produit un état typé et non une valeur corrompue;
6. promouvoir la représentation;
7. reprendre exactement l'opération;
8. comparer la sortie canonique avec Python;
9. répéter chaque scénario au moins trois fois;
10. tester plusieurs niveaux de capacité;
11. documenter les temps sans les confondre avec les invariants;
12. conserver chaque divergence, même transitoire;
13. exécuter sanitizers/analyse statique lorsque l'outillage est disponible;
14. consigner précisément environnement, compilateur, options, bibliothèque multi-précision et versions.

## 75. Ce que R8 ne prétend pas encore démontrer

R8 ne démontre pas encore :

- que la future représentation multi-précision est correcte;
- qu'une bibliothèque particulière doit être adoptée;
- qu'un mécanisme d'expansion dynamique est sans faille;
- que toutes les opérations TEBDLC seront reprenables après un événement de capacité;
- que le coût mémoire sera acceptable;
- que le C sera exempt de comportements indéfinis;
- que Python constitue un oracle absolu;
- que tous les états d'erreur nécessaires ont été identifiés;
- que les hypothèses H53–H64 résisteront aux contre-exemples.

Ces points restent à prouver expérimentalement ou formellement.

## 76. Principe directeur R8

R8 ajoute à la lignée :

    valeur ≠ représentation;
    représentation ≠ capacité;
    capacité insuffisante ≠ valeur invalide;
    overflow ≠ résultat;
    overflow détecté ≠ permission de continuer avec une valeur corrompue;
    promotion de représentation ≠ changement de valeur;
    état d'erreur ≠ zéro;
    état d'erreur ≠ gain automatique;
    reprise exacte ≠ approximation;
    représentation différente ≠ divergence sémantique;
    divergence sémantique ≠ divergence à ignorer.

Formulation opérationnelle candidate :

    overflow_anticipé
      → état_de_capacité_typé
      → transformation_de_représentation
      → reprise_exacte
      → résultat_canonique

et, si la poursuite exacte est impossible dans les capacités autorisées :

    → CAPACITY_UNRESOLVED

avec conservation de la valeur d'entrée, des opérandes, du contexte, de la provenance et de la généalogie nécessaires à la reconstruction.

---

**Jonathan Therrien, Marieville, Québec.**  
**TEBDLC — Tout est bon dans le cochon. Tous droits réservés sauf autorisation explicite du propriétaire.**