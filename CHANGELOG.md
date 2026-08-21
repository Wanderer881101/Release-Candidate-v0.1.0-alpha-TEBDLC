# Changelog

**Jonathan Therrien, Marieville, Québec.**

Ce journal résume les changements produit. La généalogie scientifique détaillée reste dans `docs/` et `evidence/`.

## 0.1.0 — préparation de première release

### Produit

- packaging Python `tebdlc` pour Python >= 3.11;
- CLI `tebdlc info` et `tebdlc self-check`;
- exécution possible via `python -m tebdlc`;
- `Makefile` unifiant build, tests, vérification, sanitizers et audit de readiness.

### Noyau et validation

- core fractionnaire borné C;
- miroir R8/R9 multi-précision avec GMP;
- gain impotent;
- stagnation, compression, décompression, réactivation et revalidation;
- recontextualisation exo-sapienne;
- assimilation comportementale;
- factorisation/productivité des répétitions;
- `ΩSt` candidat et Phase 2 structurelle/historique;
- oracles Python indépendants et jalons matériels associés.

### Documentation / reproductibilité

- thèse cumulative jusqu'à R10;
- règle de continuité matérielle;
- bundles de preuve, vecteurs, journaux, empreintes et manifestes;
- README orienté produit;
- contrat `docs/BUILD_AND_VERIFY.md`;
- état `docs/RELEASE_READINESS_0.1.0_PRE_GITIGNORE_2026-08-20.md`.

### CI

- séparation validation locale / GitHub Actions;
- matrice Python 3.11/3.12/3.13;
- job C avec dépendances natives, oracles et sanitizers;
- exécution automatique évitée sur dépôt privé afin de ne pas consommer involontairement des minutes hébergées; exécution manuelle disponible.

### Encore requis avant publication publique

- décision et création du `.gitignore` après audit explicite;
- audit historique de secrets dédié;
- décision de licence/permissions publiques;
- dernier parcours depuis checkout propre;
- tag/release, signatures et sommes de contrôle selon la politique retenue.
