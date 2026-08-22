# TEBDLC v0.1.0-alpha — Active Public Release Model

Status: **CANONICAL / ACTIVE FOR THE FIRST PUBLIC RELEASE**

## Purpose

This document is the canonical architecture for the first public TEBDLC Release Candidate.

## Repository roles

### Private TEBDLC repository

The private `TEBDLC` repository remains the development/master repository. Its complete history, unrelated branches, experiments, secrets, private operational material and material not explicitly selected for the Release Candidate are not made public merely because a Release Candidate exists.

### Public Release Candidate repository

`Release-Candidate-v0.1.0-alpha-TEBDLC` is the public distribution repository for the intentionally selected and frozen `v0.1.0-alpha` product snapshot.

The public Release Candidate is intended to be materially usable and independently verifiable. It therefore includes the source selected for this release and the resources required for build, execution, testing, audit and reconstruction, including as applicable:

- `src/`;
- `c_core/`;
- `tests/`;
- `tools/`;
- `docs/`;
- `evidence/`;
- build/package metadata such as `Makefile` and `pyproject.toml`;
- public licence, notice and release documentation;
- intentionally published provenance needed to reconstruct and verify the release.

## Canonical source lineage

The product material is derived from the frozen TEBDLC `v0.1.0-alpha` source identity:

- source commit: `677a28d87164379cb2a268e55cfc30302ebc44ab`;
- source root tree: `63658d334ae8c3d280e9ef2c29845fffce2747e6`.

Where a shared product subtree is intentionally copied from that snapshot, the public assembly should preserve its Git object identity whenever possible. Public overlays may intentionally differ where needed for licence, notice, release documentation or public-repository governance.

## Public availability versus granted rights

Public readability/downloadability and legal/project permission are distinct.

The Release Candidate may be publicly readable and downloadable while use, modification, redistribution, commercialisation, falsification participation or other project-defined rights remain subject to the active licence, applicable policy and mandatory law.

No policy for territorially controlled *delivery* may be interpreted as making already-public Release Candidate bytes technically inaccessible by territory.

## Historical controlled-distribution work

The previously built controlled-distribution subsystem, territorial delivery engine, private-vault design, authorization records and associated validation evidence are preserved as historical/R&D gains. They are not deleted and may be useful for future private artifacts or controlled services.

They do **not** define the publication boundary of this first public Release Candidate.

Historical documents remain evidence of the decisions and validations that existed when they were created. Statements in them that require the complete `v0.1.0-alpha` usable product to remain outside the public Release Candidate are superseded by this active model.

## Non-loss rule

Correcting the release architecture must not silently erase historical documents, proofs, tests, provenance or validated gains. Superseded material remains traceable and should be identified as historical rather than deleted merely because the active release model changed.

## Secret boundary

Public release approval does not authorize publication of credentials, private keys, authentication secrets, unrelated private repository material or other material not intentionally selected for the Release Candidate.

## Precedence

For the publication architecture of the first public `v0.1.0-alpha` Release Candidate, this document and later explicitly versioned successors take precedence over earlier controlled-distribution statements.

---

**Jonathan Therrien, Marieville, Québec.**
**TEBDLC — Tout est bon dans le cochon. Tous droits réservés sauf permissions explicitement accordées.**