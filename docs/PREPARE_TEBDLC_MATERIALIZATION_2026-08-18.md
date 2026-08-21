# PREPARE — Matérialisation initiale de TEBDLC

Date: 2026-08-18
Repository: Wanderer881101/TEBDLC
Statut: PREPARE — aucune implémentation encore revendiquée

## Origine et intention
TEBDLC signifie « Tout est bon dans le cochon ». Le dépôt matérialise individuellement le mécanisme de conservation, suivi, validation et assimilation des gains issu du travail sur LaGrosseClef / TheEye.

Cette matérialisation doit préserver les gains conceptuels et techniques déjà produits dans le prototype historique nommé `GainLedger`, sans prétendre que ce nom ou ce dépôt historique devient canonique. `GainLedger` reste une trace historique de première matérialisation; TEBDLC devient la nouvelle lignée canonique du composant.

## Propriété intellectuelle
Propriétaire: Jonathan Therrien, Marieville, Québec.
Tous droits réservés sauf mention contraire explicitement ajoutée ultérieurement par le propriétaire.
Aucune licence open source n'est accordée par défaut par ce dépôt privé.

## Objectif
Créer un moteur machine-readable capable de:
- enregistrer un gain avec identité stable;
- distinguer `EMERGENT_GAIN`, `VALIDATED_GAIN`, `ASSIMILATED_GAIN`, `UNKNOWN_GAIN`, `REJECTED_GAIN`;
- préserver un historique de révisions sans écrasement silencieux;
- gérer dépendances, conflits et preuves;
- enregistrer les anomalies systématiquement;
- calculer des deltas de gains;
- détecter les pertes de gains protégés;
- exporter un snapshot canonique déterministe;
- préparer la réconciliation multi-source (conversation, dépôt, tests, agents, futurs systèmes).

## Règles de gouvernance à appliquer
1. PREPARE avant action.
2. ACTION/EXECUTE uniquement après PREPARE.
3. Toute anomalie rencontrée est inscrite systématiquement.
4. Tout gain inattendu devient candidat avant validation.
5. VERIFY / RESULTS / CONFIRM après action réelle.
6. Toute reprise crée une nouvelle révision; la version précédente devient `(R-1)`, puis `(R-2)`, etc., sans limite.
7. La version la plus récente ne porte aucun `(R-n)`.
8. Aucun gain validé/assimilé ne peut disparaître silencieusement.
9. Une amélioration locale ne compense pas une régression non documentée ailleurs.
10. Les traces historiques ne sont jamais réécrites pour leur faire prévoir un résultat ultérieur.

## Baseline de migration depuis le prototype historique
Les gains techniques observés dans le prototype `GainLedger` à conserver au minimum sont:
- IDs stables basés sur représentation canonique;
- `GainRecord`, `EvidenceRecord`, `AnomalyRecord`, `GainDelta`;
- historique de révisions et `parent_revision_id`;
- validation avec preuve obligatoire;
- assimilation seulement après validation;
- blocage en présence de conflits non résolus;
- impossibilité de rejeter ou rétrograder silencieusement un gain assimilé;
- snapshot/export JSON déterministe;
- delta ajouté/supprimé/modifié;
- garde de non-perte pour gains validés/assimilés;
- anomalies persistantes et déterministes;
- tests associés.

## Gains supplémentaires visés pendant la matérialisation
- provenance structurée multi-source;
- statut de confiance de source sans autorité implicite;
- registre des anomalies avec résolution révisionnée;
- mécanisme de supersession explicite pour gains assimilés obsolètes;
- réconciliation `AGREED / ONLY_SOURCE_A / ONLY_SOURCE_B / CONFLICT / UNKNOWN`;
- version de schéma explicite et validation de snapshot;
- séparation entre identité du gain et état courant;
- support d'empreinte sémantique locale comme métadonnée/claim vérifiable.

Ces ajouts commencent comme `EMERGENT_GAIN_CANDIDATE` jusqu'à validation.

## Critères de réussite
- package Python importable;
- tests unitaires couvrant les invariants critiques;
- documentation de gouvernance et propriété intellectuelle;
- aucune perte des gains du prototype historique identifiés ci-dessus;
- anomalies et limites documentées après implémentation;
- aucune affirmation de sécurité cryptographique générale sans preuve.

## Rollback
Le dépôt est initialement vide. Chaque commit constitue une étape traçable. Toute correction future suit la convention `(R-n)` et ne supprime pas arbitrairement les traces antérieures.
