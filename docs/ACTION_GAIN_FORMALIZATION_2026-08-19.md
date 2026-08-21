# ACTION / OBSERVATIONS — Formalisation approfondie des gains

**Jonathan Therrien, Marieville, Québec.**

Date : 2026-08-19
Horodatage de révision : 2026-08-19 06:55:50 America/Montreal
Statut : IMPLEMENTED / CI VERIFY PENDING
Préparation : `docs/PREPARE_GAIN_FORMALIZATION_2026-08-19.md`

## Actions réalisées

- création d'un catalogue fermé initial des zéros;
- séparation explicite des zéros d'existence, quantité, variation, couverture, expression, activation, admissibilité, dette, conflit, chimère, résultat, résidu, prolifération observée et occurrence;
- ajout d'un corpus de contre-exemples arithmétiques;
- ajout d'une ontologie multi-axes pour empêcher les pléonasmes et la compression de propriétés orthogonales dans un enum unique;
- formalisation de 49 familles/propriétés de gains avec critères de distinction et contre-exemples;
- ajout d'un prototype rationnel exact `ExactFractionalGain`;
- ajout du contexte typé `FractionContext`, désormais enrichi de `domain`, `dimension`, `unit`, `reference`, `context`, `provenance`;
- ajout du zéro machine-readable `TypedZero` et du catalogue `ZeroKind`;
- ajout d'une représentation symbolique exacte `SymbolicFractionalGain` pour préserver des compositions très profondes sans expansion numérique inutile;
- ajout de `ProofRef`, `GainRelation`, `ConsolidationResult` et `ConsolidationStatus` pour matérialiser la séparation `GAIN / RELATION / RÉSULTAT / PREUVE`;
- ajout d'une consolidation chimérique exigeant `ZERO_CHIMERA_CONSOLIDATION` tout en conservant les IDs des constituants;
- ajout de `ImpotentGainEnvelope` pour représenter un entier acquis avec résidu fractionnaire strictement positif sous un seuil cible;
- ajout de `DimensionalEffect` et `NegativePositiveGainProfile` pour conserver des effets signés par dimension sans totalisation inter-dimensions;
- multiplication permise uniquement lorsque domaine, dimension, unité, référentiel et contexte sont compatibles;
- addition générale explicitement non disponible sur les primitives fractionnaires expérimentales;
- soustraction explicitement bloquée dans les prototypes fractionnaires;
- division explicitement bloquée dans les prototypes fractionnaires;
- exposant symbolique nul bloqué, car `f^0 = 1` fabriquerait lui aussi une unité à partir d'une base fractionnaire;
- tests montrant que `3/10 ÷ 3/10 = 1` et `3/10 ÷ 1/10 = 3` en arithmétique ordinaire, justifiant l'interdiction TEBDLC;
- tests de non-sous-flux avec multiplication rationnelle exacte répétée;
- test empêchant une fraction très proche de un d'être promue à l'unité;
- test empêchant zéro et un d'être instanciés comme `ExactFractionalGain` strict;
- tests de non-propagation entre types de zéro;
- test exigeant une preuve pour créer un zéro typé;
- préservation et union déterministe de provenance lors d'une multiplication compatible;
- test symbolique de `(3/10)^1_000_000` conservé sans expansion immédiate et sans promotion à zéro ou un;
- tests de gain impotent confirmant qu'une suite finie de 9 sous `46` reste strictement sous `46`;
- tests confirmant qu'un résultat chimérique conserve tous ses constituants;
- tests confirmant qu'un profil `(+2 performance, -8 intégrité)` ne possède aucun total agrégé.

## Observations

### O-01 — représentation rationnelle et division sont effectivement séparables

L'utilisation de `fractions.Fraction` permet de représenter exactement `p/q` sans fournir pour autant une permission sémantique de diviser deux gains. Le prototype surcharge explicitement `/` pour lever une erreur.

### O-02 — la multiplication exacte évite le sous-flux numérique

Une profondeur de composition élevée produit des entiers numérateur/dénominateur croissants, mais pas un faux zéro. Cela valide le choix d'éviter le `float` comme autorité de conservation.

### O-03 — la composabilité doit être plus stricte que le seul contexte

Le premier prototype comparait `domain`, `reference` et `context`. Cette règle a été raffinée avant validation : `dimension` et `unit` sont désormais obligatoires et participent elles aussi au test de composabilité.

### O-04 — le catalogue des zéros reste révisable, mais fermé par défaut

Un nouveau zéro exige désormais une définition formelle; l'absence de type de zéro ne permet pas d'en créer un implicitement.

### O-05 — zéro typé sans propagation implicite

`TypedZero.implies()` n'autorise actuellement qu'une implication vers son propre `ZeroKind`. Par exemple `ZERO_RESULT` ne devient jamais `ZERO_EXISTENCE` sans future règle explicite et testée.

### O-06 — représentation symbolique nécessaire à grande profondeur

Une fraction exacte peut être préservée symboliquement sous forme facteurs/exposants. `(3/10)^1_000_000` reste ainsi compact, strictement positif et strictement non unitaire sans nécessiter l'expansion immédiate de nombres énormes.

### O-07 — l'exposant zéro appartient à la même famille de risque que la division

En arithmétique standard, `f^0 = 1` pour `f != 0`. Autoriser `pow(0)` sur un gain fractionnaire fabriquerait donc artificiellement l'unité. Le prototype l'interdit.

### O-08 — les familles de gains doivent être évaluées par axes

La formalisation montre qu'un même gain peut porter plusieurs propriétés indépendantes. Le modèle cible doit rester multi-axes plutôt que multiplier artificiellement les statuts exclusifs.

### O-09 — le gain chimère exige une couche résultat distincte

La nullité chimérique appartient au `ConsolidationResult`, pas aux gains constituants. Le prototype impose cette séparation en conservant explicitement `constituent_gain_ids` et un `TypedZero` de type `CHIMERA_CONSOLIDATION`.

### O-10 — le gain impotent est mieux représenté comme enveloppe que comme arrondi

`ImpotentGainEnvelope` conserve séparément l'entier acquis, le résidu fractionnaire exact et le seuil cible. Aucun arrondi ne transforme le résidu en unité.

### O-11 — le gain négativement positif ne doit posséder aucun total implicite

`NegativePositiveGainProfile` conserve chaque dimension signée et ne fournit aucune propriété `total`. Les valeurs négatives y sont des mesures dimensionnelles, pas un opérateur TEBDLC de soustraction entre gains.

## Anomalies de procédure

### ANOMALY-GAINFORM-001 — branche de validation absente lors de la première écriture

Contexte : préparation d'une PR de validation isolée.
Symptôme : première tentative de créer le marqueur sur `verify-gain-formalization` avant création de la branche; GitHub a répondu `404 Branch not found`.
Impact : aucune modification partielle sur cette branche.
Statut : RESOLVED.
Action : branche ensuite créée explicitement depuis le HEAD connu.

### ANOMALY-GAINFORM-002 — marqueur temporaire créé sur main

Contexte : reprise de la séquence de validation.
Symptôme : un fichier `docs/TEMP2.md` a été créé sur `main` par erreur.
Impact : deux commits traçables, mais aucun état final parasite.
Statut : RESOLVED.
Action : fichier immédiatement supprimé par commit dédié; l'historique n'a pas été réécrit.

### ANOMALY-GAINFORM-003 — première PR de validation en échec

Contexte : PR #2 `Validate gain formalization tranche`, head `459681c...`.
Symptôme : workflow `TEBDLC CI` run `32245381590` terminé `failure` sur Python 3.11, 3.12 et 3.13.
Impact : aucun nouveau gain candidat ne peut être classé `VALIDATED_GAIN` sur la base de cette CI.
Statut : OPEN / R2 REQUIRED.
Limite d'investigation : le connecteur expose le statut des jobs mais les logs détaillés ont retourné 404; `gh` n'est pas installé dans l'environnement disponible. Aucune cause n'est inventée.
Action : finaliser le HEAD courant, créer une validation R2 propre et observer sa CI. L'échec de la PR #2 reste conservé comme trace.

## Gains émergents candidats

### EG-FRAC-001 — exactitude sans sous-flux

Une représentation rationnelle exacte peut conserver une fraction strictement positive à très grande profondeur de multiplication sans la convertir en zéro.

Statut : `EMERGENT_GAIN_CANDIDATE`, VERIFY CI requis.

### EG-FRAC-002 — interdiction opératoire de division

Le type expérimental peut empêcher matériellement l'utilisation de `/` entre gains fractionnaires.

Statut : `EMERGENT_GAIN_CANDIDATE`, VERIFY CI requis.

### EG-FRAC-003 — interdiction opératoire de soustraction

Le type expérimental peut empêcher matériellement `G1-G2` afin d'éviter l'annulation destructive au niveau des primitives.

Statut : `EMERGENT_GAIN_CANDIDATE`, VERIFY CI requis.

### EG-FRAC-004 — provenance compositionnelle déterministe

La multiplication compatible peut unir les références de provenance de manière triée et déterministe.

Statut : `EMERGENT_GAIN_CANDIDATE`, VERIFY CI requis.

### EG-FRAC-005 — composabilité dimension/unité

Le type fractionnaire peut refuser une multiplication lorsque dimension ou unité diffèrent, même si le domaine et le contexte sont identiques.

Statut : `EMERGENT_GAIN_CANDIDATE`, VERIFY CI requis.

### EG-ZERO-001 — zéro fermé machine-readable

Le catalogue des zéros peut être représenté par `ZeroKind` et `TypedZero` avec portée et preuve obligatoires.

Statut : `EMERGENT_GAIN_CANDIDATE`, VERIFY CI requis.

### EG-ZERO-002 — non-propagation inter-zéros

Une nullité de résultat/chimère/activation/etc. peut être empêchée de devenir implicitement une nullité d'existence.

Statut : `EMERGENT_GAIN_CANDIDATE`, VERIFY CI requis.

### EG-SYM-001 — fraction symbolique exacte

Une composition fractionnaire profonde peut être stockée comme facteurs rationnels normalisés et exposants positifs, sans sous-flux et sans expansion obligatoire.

Statut : `EMERGENT_GAIN_CANDIDATE`, VERIFY CI requis.

### EG-SYM-002 — fermeture contre l'unité par exposant nul

L'interdiction de l'exposant zéro empêche une seconde voie de fabrication artificielle de `1`.

Statut : `EMERGENT_GAIN_CANDIDATE`, VERIFY CI requis.

### EG-ONTO-001 — critère anti-pléonasme multi-axes

Deux termes sont distincts seulement s'ils peuvent varier indépendamment ou possèdent une sémantique, une preuve, une temporalité, une arithmétique ou des contre-exemples distincts.

Statut : `EMERGENT_GAIN_CANDIDATE`, validation conceptuelle et tests futurs requis.

### EG-CHIMERA-001 — résultat chimérique non destructif

Une consolidation chimérique peut être représentée comme résultat nul typé tout en conservant tous les gains constituants et les preuves de l'hypothèse réfutée.

Statut : `EMERGENT_GAIN_CANDIDATE`, VERIFY CI requis.

### EG-IMPOTENT-001 — seuil entier sans arrondi

Un entier acquis et un résidu fractionnaire strictement positif peuvent être conservés séparément de façon à démontrer que le seuil entier suivant n'est pas atteint.

Statut : `EMERGENT_GAIN_CANDIDATE`, VERIFY CI requis.

### EG-MULTI-001 — profil multidimensionnel non collapsant

Des effets tels que `(+2 performance, -8 intégrité)` peuvent être représentés exactement sans total inter-dimensions et sans transformer le signe négatif en opérateur de soustraction entre gains.

Statut : `EMERGENT_GAIN_CANDIDATE`, VERIFY CI requis.

## Limites découvertes

- aucune addition typée n'est encore définie;
- aucune partition arithmétique n'est implémentée;
- `FractionContext` ne porte pas encore identité d'entité, fenêtre temporelle ni support explicite;
- la composabilité par stricte égalité de contexte/dimension/unité est volontairement restrictive;
- les prototypes ne sont pas encore exportés depuis l'API racine `tebdlc` afin d'éviter une assimilation prématurée;
- `TypedZero` ne définit volontairement aucune règle d'implication inter-type;
- `SymbolicFractionalGain.evaluate_exact()` peut devenir coûteux si on exige volontairement l'expansion d'un exposant gigantesque; l'avantage réside dans la possibilité de ne pas l'évaluer;
- aucune logique de support/chevauchement machine-readable n'est encore codée;
- aucune revendication de compatibilité directe avec TheEye/SHA777 n'est faite dans cette tranche.

## Règle de non-perte appliquée

Aucun concept existant n'a été supprimé. Les nouveaux fichiers étendent la lignée. Les interdictions opératoires sont ajoutées dans des modules expérimentaux séparés du moteur historique afin de ne pas modifier silencieusement son comportement actuel. Les échecs et erreurs de procédure restent documentés et ne sont pas réécrits hors de l'histoire.

---

**Jonathan Therrien, Marieville, Québec.**
**TEBDLC — Tous droits réservés sauf autorisation explicite du propriétaire.**
