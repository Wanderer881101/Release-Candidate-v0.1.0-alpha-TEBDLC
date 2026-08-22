# TEBDLC

**Jonathan Therrien, Marieville, Québec.**

**Tout est bon dans le cochon** — moteur souverain de conservation, validation, réconciliation et assimilation des gains.

TEBDLC matérialise un principe simple : une évolution ne doit pas perdre silencieusement les gains déjà démontrés. Tests, examens, validations, audits, simulations, corrections et révisions peuvent eux-mêmes produire de nouveaux gains, mais ceux-ci restent candidats tant qu'ils ne sont pas validés.

## Statut produit

Version Python déclarée : `0.1.0`.

TEBDLC est un produit de R&D utilisable et vérifiable. Certaines propriétés sont exécutées et reproduites dans les domaines testés; d'autres restent explicitement candidates. Le dépôt ne revendique ni preuve universelle, ni garantie cryptographique générale, ni conformité à un standard externe sans preuve dédiée.

### Premier Release public

Le modèle canonique du premier Release public `v0.1.0-alpha` est défini par `ACTIVE_RELEASE_MODEL_v0.1.0-alpha.md`.

Le dépôt privé `TEBDLC` demeure le dépôt maître de développement. Le présent dépôt public distribue la copie figée intentionnellement sélectionnée du produit `v0.1.0-alpha`, avec les éléments nécessaires à son utilisation et à sa vérification indépendante. Les anciens mécanismes de distribution contrôlée sont conservés comme historique/R&D et ne définissent plus la frontière de publication de ce premier Release public.

## Composants

- `src/tebdlc/` : bibliothèque Python et objets formels;
- `c_core/` : noyaux C expérimentaux et tests de référence;
- `tests/` : tests Python;
- `evidence/` : vecteurs, journaux, empreintes et manifestes de jalons;
- `docs/` : thèse documentaire, rapports et généalogie expérimentale;
- `tools/` : outils de validation et de continuité;
- `Makefile` : contrat de build/test/verify reproductible.

## Prérequis

### Python

- Python 3.11 ou plus récent;
- `pip`;
- `pytest` pour exécuter la suite de tests.

### C

Le build complet C requiert :

- un compilateur C11 (`gcc`, `clang` ou équivalent compatible);
- GMP;
- OpenSSL/libcrypto;
- zlib;
- Clang pour les cibles sanitizer.

Sous Debian/Ubuntu, les paquets correspondants sont généralement :

```bash
sudo apt-get install build-essential clang libgmp-dev libssl-dev zlib1g-dev python3 python3-pip
```

## Installation depuis un checkout

```bash
make setup
```

Cette commande installe le package Python en mode éditable et `pytest` dans l'environnement courant.

Installation Python seule :

```bash
python3 -m pip install -e .
```

## Interface utilisateur

Après installation :

```bash
tebdlc info
tebdlc self-check
tebdlc self-check --json
```

ou sans script console :

```bash
python3 -m tebdlc info
python3 -m tebdlc self-check
```

`self-check` construit et relit localement un gain déterministe dans le ledger. Aucun réseau n'est requis.

## Build et tests

```bash
make build
make test
```

`make test` exécute les tests Python et les huit familles C actuellement intégrées au produit : core borné, R8/R9 multi-précision, gain impotent, stagnation, recontextualisation exo-sapienne, assimilation comportementale, productivité/factorisation et `ΩSt` Phase 2.

Pour confronter les tests C à leurs oracles Python indépendants :

```bash
make verify
```

Pour les vérifications mémoire/comportement indéfini actuellement câblées :

```bash
make sanitize
```

Pour supprimer uniquement les artefacts régénérables :

```bash
make clean
```

Voir `docs/BUILD_AND_VERIFY.md` pour le détail des commandes, dépendances, sorties et limites.

## Cycle fondamental

`OBSERVATION -> EMERGENT_GAIN -> EXPERIMENTATION -> VALIDATION -> ASSIMILATION`

## Gouvernance fondamentale

`PREPARE -> ACTION/EXECUTE -> OBSERVATIONS -> ANOMALIES + EMERGENT_GAINS -> VERIFY/RESULTS -> CONFIRM`

Toute reprise crée une nouvelle révision documentaire. L'historique n'est pas réécrit silencieusement.

## États de gain

- `EMERGENT_GAIN` : découvert mais non validé;
- `VALIDATED_GAIN` : démontré par une ou plusieurs preuves;
- `ASSIMILATED_GAIN` : intégré comme gain durable;
- `UNKNOWN_GAIN` : potentiel ou état insuffisamment démontré;
- `REJECTED_GAIN` : gain candidat rejeté avec traçabilité.

## Principes

- aucune suppression silencieuse d'un gain validé ou assimilé;
- anomalies enregistrées même lorsque l'action globale réussit;
- historique des révisions préservé;
- provenance multi-source explicite;
- conflits visibles et bloquants lorsque nécessaire;
- snapshots déterministes et auditables;
- réconciliation entre sources sans écrasement arbitraire;
- distinction entre identité d'un gain, son état courant et ses preuves;
- stagnation différente de disparition;
- compression différente d'effacement;
- réactivation différente d'auto-validation;
- représentation différente de valeur;
- mesure candidate différente de vérité universelle.

## Validation et preuves

Les validations principales peuvent être exécutées localement avec `make verify` et `make sanitize`. GitHub Actions constitue une contre-validation externe lorsqu'un runner est disponible; l'indisponibilité ou la facturation d'un runner ne doit pas être confondue avec un résultat fonctionnel TEBDLC.

Les jalons solides conservent au minimum :

`code + tests + vecteurs + logs + empreintes + résultats + documentation`.

Les preuves et limites associées sont conservées sous `evidence/milestones/` et `docs/`.

## Propriété intellectuelle et droits d'utilisation

TEBDLC demeure une propriété intellectuelle protégée. La publication du code source ne constitue ni un abandon de droits ni une publication sous licence open source.

Les droits effectivement accordés sont définis par la licence active du Release public. La disponibilité mondiale des fichiers publics et les droits juridiques/projet accordés sur ces fichiers sont deux choses distinctes. Le présent README est descriptif et ne crée aucun droit supplémentaire.

Voir :

- `NOTICE.md` pour la propriété, l'attribution et la réserve des droits;
- `LICENSE-SOURCE-AVAILABLE-v0.1.1.md` pour les permissions et restrictions actives du Release public;
- `TERRITORIAL_RIGHTS_POLICY_v0.2.md` pour la portée actuelle des règles territoriales;
- `ACTIVE_RELEASE_MODEL_v0.1.0-alpha.md` pour l'architecture canonique du premier Release public.

Les anciens `LICENSE-SOURCE-AVAILABLE-DRAFT.md`, `TERRITORIAL_DISTRIBUTION_POLICY.md` et éléments de `distribution/` sont conservés pour la provenance de l'ancien modèle de distribution contrôlée; ils ne remplacent pas les documents actifs ci-dessus pour la frontière de publication de `v0.1.0-alpha`.

## Traçabilité

Voir notamment :

- `docs/PREPARE_TEBDLC_MATERIALIZATION_2026-08-18.md`;
- `docs/THESE_ARITHMETIQUE_DES_GAINS_R10_2026-08-19.md`;
- `docs/CONSOLIDATION_POST_R9_2026-08-19.md`;
- `docs/ADDENDUM_R10_OMEGAST_PHASE2_2026-08-19.md`.
