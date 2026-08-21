# VERIFY / RESULTS — Formalisation approfondie des gains TEBDLC

**Jonathan Therrien, Marieville, Québec.**

Horodatage : 2026-08-19 07:08 America/Montreal
Statut : BLOCKED / NOT CONFIRMED
Préparation : `docs/PREPARE_GAIN_FORMALIZATION_2026-08-19.md`
Action : `docs/ACTION_GAIN_FORMALIZATION_2026-08-19.md`
Validation R1 : PR #2 — fermée, non fusionnée, échec conservé
Validation R2 : PR #3 — head `3a6cafe69db07c2c6e480ec9ad8cf25dfd404d09`
Base R2 : `main` `e8303599ebc36d8b56f3f55bed3e72ff2a01dc79`

## 1. Résultat CI R2 observé

Workflow : `TEBDLC CI`
Run : `32246045162`
Événement : `pull_request`
Statut : `completed`
Conclusion : `failure`
Début observé : `2026-08-19T11:07:32Z`
Fin observée : `2026-08-19T11:07:36Z`

Jobs observés :

- Python 3.11 : FAILURE;
- Python 3.12 : FAILURE;
- Python 3.13 : FAILURE.

Le connecteur retourne `steps: []` pour les trois jobs. La tentative de lecture des logs du job Python 3.11 retourne `BlobNotFound`/404. L'environnement d'exécution disponible ici ne possède pas `gh`, donc les logs GitHub Actions complets ne peuvent pas être récupérés par le chemin de secours prévu.

Aucune cause racine n'est donc déclarée sans preuve.

## 2. Ce qui est réellement matérialisé dans main

La tranche contient actuellement, sans export dans l'API racine :

- `ExactFractionalGain` et `FractionContext`;
- exactitude rationnelle stricte `0 < F < 1`;
- contexte de fraction comprenant domaine, dimension, unité, référentiel, contexte et provenance;
- multiplication conditionnée par composabilité;
- addition générale, soustraction et division explicitement non disponibles comme primitives fractionnaires;
- `TypedZero` / `ZeroKind` avec preuve et portée obligatoires;
- non-propagation implicite entre types de zéro;
- `SymbolicFractionalGain` et facteurs/exposants positifs;
- exposant zéro interdit pour éviter `f^0 = 1`;
- `ProofRef`, `GainRelation`, `ConsolidationResult`;
- `ZERO_CHIMERA_CONSOLIDATION` séparé des gains constituants;
- `ImpotentGainEnvelope`;
- `DimensionalEffect` / `NegativePositiveGainProfile` sans total inter-dimensions;
- corpus de contre-exemples;
- catalogue fermé des zéros;
- ontologie multi-axes;
- formalisation de familles de gains.

## 3. Résultats qui NE SONT PAS revendiqués

La tranche ne reçoit aucun `VALIDATED_GAIN` ni `ASSIMILATED_GAIN` supplémentaire sur la seule base de la CI actuelle.

Sont notamment encore non confirmés par CI :

- compatibilité Python 3.11/3.12/3.13 des nouveaux modules;
- non-régression de l'intégralité de la suite historique après ajout des prototypes;
- règle d'attribution sur le HEAD final;
- exactitude symbolique dans la suite canonique complète;
- zéro typé dans la suite canonique complète;
- gain chimère, impotent et multidimensionnel dans la suite canonique complète.

## 4. Analyse limitée mais utile

Les deux validations R1 et R2 ont échoué sur les trois matrices. La R2 s'est terminée en environ quatre secondes et les jobs ne présentent aucun step via le connecteur. Ce signal est compatible avec un échec très précoce du workflow ou de l'environnement, mais il ne permet pas de conclure à une cause précise.

Une reproduction ciblée hors checkout GitHub a permis de vérifier les propriétés arithmétiques principales des primitives fractionnaires et symboliques, mais cette reproduction n'est pas considérée comme substitut à la CI canonique et n'est donc pas utilisée pour promouvoir les gains candidats.

## 5. Anomalie

### ANOMALY-GAINFORM-004 — CI R2 échoue sans logs accessibles

Contexte : validation isolée du HEAD final de formalisation.
Symptôme : run `32246045162` en failure sur 3.11/3.12/3.13, durée très courte, aucune étape retournée, logs blob indisponibles.
Impact : impossibilité de CONFIRM la tranche par GitHub Actions malgré la présence des tests.
Statut : OPEN / BLOCKED.
Action requise : obtenir un log de job exploitable ou exécuter la suite canonique depuis un checkout exact du HEAD; corriger seulement après cause démontrée.

## 6. Non-perte

Aucun module expérimental n'est exporté depuis `tebdlc.__init__`. Le moteur historique reste donc découplé de ces nouvelles primitives tant que la validation est bloquée.

Les PR R1/R2, anomalies, échecs et hypothèses restent dans l'historique. Aucun échec n'est transformé artificiellement en PASS et aucun concept documenté n'est supprimé pour simplifier la validation.

## 7. CONFIRM

**CONFIRM NON ACCORDÉ.**

La tranche est matériellement développée et documentée, mais son statut reste `BLOCKED / NOT CONFIRMED` jusqu'à une preuve d'exécution canonique satisfaisante.

---

**Jonathan Therrien, Marieville, Québec.**
**TEBDLC — Tous droits réservés sauf autorisation explicite du propriétaire.**