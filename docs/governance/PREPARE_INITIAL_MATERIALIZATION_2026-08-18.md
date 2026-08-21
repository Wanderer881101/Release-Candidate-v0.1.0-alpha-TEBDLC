# PREPARE — Matérialisation initiale de TEBDLC

**Jonathan Therrien, Marieville, Québec.**

Date: 2026-08-18
Statut: PREPARE avant toute implémentation TEBDLC
Dépôt: Wanderer881101/TEBDLC
Visibilité constatée: privée

## Nom et signification
TEBDLC signifie « Tout est bon dans le cochon ».

Ce nom remplace GainLedger comme identité propre du mécanisme de conservation des gains. Le dépôt GainLedger antérieurement matérialisé reste une trace historique de l'itération précédente et ne doit pas être effacé ou réécrit silencieusement.

## Pourquoi cette matérialisation
Le projet a besoin d'un mécanisme indépendant, machine-readable et auditable qui empêche autant que possible qu'un agent IA, une reprise, une reconstruction, un test ou une évolution perde silencieusement un gain déjà acquis.

TEBDLC doit matérialiser les règles déjà établies:
- non-perte de gains;
- gains émergents pendant tests/examens/validations;
- validation avant assimilation;
- anomalies systématiquement enregistrées;
- révisions `(R-n)` illimitées;
- conversation et dépôts comme sources complémentaires lorsque compatibles;
- `UNKNOWN` plutôt qu'une affirmation non démontrée;
- PREPARE avant action et VERIFY/RESULTS/CONFIRM après action.

## Propriété intellectuelle
Les concepts, spécifications, textes, architectures et implémentations originales déposés ici sont traités comme propriété intellectuelle du propriétaire du dépôt, sous réserve des droits de tiers applicables aux dépendances, standards, citations ou contributions externes. Aucune licence publique n'est accordée implicitement par la simple présence dans ce dépôt privé.

Cette mention n'est pas une opinion juridique ni un substitut à un conseil professionnel en propriété intellectuelle.

## Objectif technique initial
Créer un noyau Python déterministe capable de représenter:
- GainRecord et identifiant stable;
- états EMERGENT / VALIDATED / ASSIMILATED / UNKNOWN / REJECTED;
- EvidenceRecord;
- historique de révisions append-conscious;
- AnomalyRecord avec OPEN / RESOLVED / UNKNOWN / BLOCKED;
- conflits et dépendances;
- snapshots déterministes;
- delta entre deux états;
- garde explicite contre disparition de gains validés/assimilés.

## Exigence de migration depuis l'itération GainLedger
La migration doit être une réimplémentation/portage contrôlé sans perte fonctionnelle connue, tout en remplaçant l'identité publique/interne GainLedger par TEBDLC. Les références historiques à GainLedger peuvent subsister uniquement lorsqu'elles décrivent réellement cette étape historique.

## Règle d'anomalie
Toute anomalie rencontrée pendant cette matérialisation sera inscrite dans le VERIFY final avec contexte, symptôme, impact, statut et action prise/prévue. Un succès global ne l'efface pas.

## Gains émergents
Toute amélioration découverte pendant la matérialisation devient d'abord `EMERGENT_GAIN_CANDIDATE`; elle ne sera déclarée acquise qu'après preuve/test approprié.

## Non-objectifs immédiats
- ne pas prétendre résoudre l'équivalence sémantique générale;
- ne pas intégrer de secrets ou données personnelles brutes;
- ne pas prétendre qu'un hash stable constitue une preuve cryptographique complète;
- ne pas publier le dépôt ni lui appliquer une licence open source sans décision explicite du propriétaire.

## Rollback
Le dépôt est initialement vide. Les commits constituent la trace. En cas d'erreur, corriger par nouvelle révision documentée plutôt que réécrire l'histoire.
