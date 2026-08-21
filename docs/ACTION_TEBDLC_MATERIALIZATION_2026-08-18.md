# ACTION / OBSERVATIONS — Matérialisation initiale de TEBDLC

**Jonathan Therrien, Marieville, Québec.**

Date: 2026-08-18
Statut: IMPLEMENTED / VERIFY PENDING
Préparation: `docs/PREPARE_TEBDLC_MATERIALIZATION_2026-08-18.md`

## Actions réalisées
- ajout de `NOTICE.md` avec propriété intellectuelle et tous droits réservés;
- ajout de `README.md` avec principes, cycle de gains et gouvernance;
- création de `pyproject.toml`;
- création du package `src/tebdlc/`;
- implémentation de `TEBDLC`, `GainRecord`, `EvidenceRecord`, `SourceRef`, `AnomalyRecord`, `GainDelta`, réconciliation et états associés;
- historique de révisions de gains et d'anomalies;
- validation avec preuve obligatoire;
- assimilation après validation et blocage sur conflits non résolus;
- supersession explicite d'un gain assimilé sans destruction de l'ancien;
- snapshot/export JSON déterministe;
- delta et garde de non-perte des gains protégés;
- réconciliation `AGREED / ONLY_SOURCE_A / ONLY_SOURCE_B / CONFLICT / UNKNOWN`;
- tests unitaires couvrant les invariants principaux;
- workflow CI Python 3.11/3.12/3.13 avec compilation et tests.

## Anomalies
### ANOMALY-TEBDLC-001 — création de pyproject initialement bloquée
Contexte: initialisation du package Python TEBDLC.
Symptôme: première écriture de `pyproject.toml` bloquée par le contrôle de sécurité de l'outil.
Impact observé: retard local, aucune modification partielle de ce fichier lors de la tentative bloquée.
Statut: RESOLVED.
Action réalisée: reprise avec un manifeste minimal; création réussie ensuite.

### ANOMALY-TEBDLC-002 — CI non encore observée au moment de cette mise à jour
Contexte: workflow CI créé sur `main`.
Symptôme: le fichier de workflow existe, mais aucun résultat de run n'a encore été vérifié dans ce cycle au moment d'écrire cette observation.
Impact: impossible de déclarer les tests distants PASS avant observation réelle.
Statut: OPEN / VERIFY REQUIRED.
Action prévue: vérifier l'état CI ou, si indisponible, enregistrer explicitement cette limite dans le VERIFY final.

## Gains émergents observés
### EMERGENT_GAIN_CANDIDATE — provenance structurée multi-source
`SourceRef` matérialise une provenance structurée et déterministe. Statut candidat jusqu'à validation par tests.

### EMERGENT_GAIN_CANDIDATE — anomalies révisionnées
Les anomalies possèdent maintenant leur propre chaîne de révisions et `parent_revision_id`, ce qui étend la règle de non-effacement aux anomalies elles-mêmes.

### EMERGENT_GAIN_CANDIDATE — supersession explicite
Un gain assimilé ne peut pas être rejeté silencieusement; une nouvelle proposition peut le superséder tout en conservant l'ancien gain assimilé dans l'historique.

### EMERGENT_GAIN_CANDIDATE — réconciliation multi-source
Deux TEBDLC peuvent être comparés sans arbitrage automatique, avec états explicites `AGREED`, `ONLY_SOURCE_A`, `ONLY_SOURCE_B`, `CONFLICT`, `UNKNOWN`.

Aucun de ces candidats n'est déclaré assimilé avant VERIFY réel.
