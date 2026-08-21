# VERIFY / RESULTS / CONFIRM — Matérialisation initiale de TEBDLC

**Jonathan Therrien, Marieville, Québec.**

Date: 2026-08-18
Statut: PASS WITH RECORDED LIMITS
Préparation: `docs/PREPARE_TEBDLC_MATERIALIZATION_2026-08-18.md`
Action: `docs/ACTION_TEBDLC_MATERIALIZATION_2026-08-18.md`
Validation PR: #1 `Validate initial TEBDLC materialization`

## Résultats observés
La matérialisation initiale existe réellement dans `Wanderer881101/TEBDLC` et comprend:
- propriété intellectuelle déclarée dans `NOTICE.md`;
- README et gouvernance fondamentale;
- package Python `tebdlc`;
- moteur `TEBDLC`;
- gains, preuves, provenance structurée, anomalies, deltas et réconciliation;
- historique de révisions avec parenté;
- validation avec preuve obligatoire;
- assimilation après validation;
- conflits non résolus bloquant l'assimilation;
- refus de rejet/rétrogradation silencieuse d'un gain assimilé;
- supersession explicite sans destruction de l'ancien gain assimilé;
- snapshot JSON canonique et déterministe;
- garde de non-perte pour gains validés/assimilés;
- tests unitaires;
- workflow CI multi-version.

## CI réellement observée
Le workflow `TEBDLC CI`, run `32167676668`, a terminé avec conclusion `success`.

Jobs observés:
- Python 3.11: SUCCESS — Install, Compile, Test;
- Python 3.12: SUCCESS — Install, Compile, Test;
- Python 3.13: SUCCESS — Install, Compile, Test.

La CI a été déclenchée par une PR de validation isolée ne modifiant pas le runtime.

## Anomalies
### ANOMALY-TEBDLC-001 — première création de pyproject bloquée
Statut: RESOLVED.
La tentative bloquée a été inscrite dans l'ACTION; une reprise minimale a ensuite créé `pyproject.toml` avec succès.

### ANOMALY-TEBDLC-002 — CI non encore observée pendant l'implémentation
Statut: RESOLVED.
Une branche de validation et la PR #1 ont été créées uniquement pour observer une CI réelle. Les trois versions Python configurées ont réussi.

### ANOMALY-TEBDLC-003 — dépôt prototype historique `GainLedger`
Contexte: une première matérialisation a été réalisée sous un nom déjà utilisé ailleurs avant l'adoption de TEBDLC.
Impact: risque de confusion nominale, mais les gains techniques restent utiles.
Statut: RESOLVED AT LINEAGE LEVEL.
Action: TEBDLC devient la lignée canonique; le prototype historique reste une source de provenance et ne doit pas être effacé pour falsifier l'historique.

## Gains émergents validés par cette tranche
Les comportements suivants sont désormais démontrés par les tests et la CI de cette matérialisation:
- provenance structurée multi-source déterministe;
- anomalies révisionnées avec parenté;
- supersession explicite d'un gain assimilé;
- réconciliation multi-source avec états explicites;
- compatibilité Python 3.11, 3.12 et 3.13 pour la tranche actuelle.

Ils sont donc classifiables comme `VALIDATED_GAIN` dans le domaine couvert par les tests actuels. Ils ne sont pas automatiquement revendiqués comme universels hors de ce domaine.

## Gains encore candidats
- validation de schéma externe/JSON Schema formel;
- persistance durable sur disque/base de données avec transactions;
- signatures/attestations cryptographiques;
- réconciliation N-sources et résolution assistée;
- intégration directe avec TheEye et les autres dépôts;
- Semantic Checksum plus riche;
- intégration éventuelle avec SHA777, sans dépendance cryptographique non démontrée.

## Limites
- TEBDLC 0.1.0 est une première matérialisation, pas un produit final.
- La garde de non-perte détecte actuellement surtout la disparition d'identifiants protégés; des notions plus riches de perte sémantique devront être ajoutées.
- La réconciliation signale les conflits; elle ne les résout pas arbitrairement.
- Aucune garantie cryptographique générale n'est revendiquée.

## CONFIRM
La matérialisation initiale de TEBDLC est confirmée comme fonctionnelle dans son périmètre testé. Le cycle PREPARE -> ACTION/OBSERVATIONS -> ANOMALIES/GAINS -> VERIFY/RESULTS -> CONFIRM a été respecté et les anomalies rencontrées sont conservées dans la trace.
