# TEBDLC v0.1.0-alpha — Controlled Release Gate

This gate prevents accidental publication of the complete territorially controlled source through a globally public GitHub branch.

## Completed governance and reference-implementation prerequisites

- [x] Public Release Candidate repository exists.
- [x] Evidence-safe `.gitignore` policy established.
- [x] Isolated `falsification-registry` branch established.
- [x] Falsification attribution/provenance policy established.
- [x] Territorial policy v0.1 established.
- [x] Caribbean classification corrected to NEUTRAL.
- [x] Explicit restricted territorial entries recorded from the approved policy inputs.
- [x] Sovereign source-available licence activated as project licence v0.1.
- [x] Rights matrix for PRIVILEGED / NEUTRAL / RESTRICTED established.
- [x] PRIVILEGED and NEUTRAL rights made identical except for the formal TEBDLC falsification right.
- [x] NEUTRAL ordinary testing, benchmarking, debugging and private evaluation preserved without granting participation in the formal falsification regime.
- [x] Recipient authorization/decision contract v0.1 specified.
- [x] Licence acceptance record format specified and schema added.
- [x] Distribution-event audit record format specified and schema added.
- [x] Release-manifest format specified and schema added.
- [x] Stdlib-only fail-closed record validator added.
- [x] Validator tests cover privileged allow, neutral allow, neutral falsification denial, restricted denial, malformed hash and manifest inconsistency.
- [x] Deterministic Caribbean geographic annex added with NEUTRAL semantics and Florida override preserved.
- [x] Deterministic Middle East/restricted annex added from explicitly approved restricted territories.
- [x] Deterministic territorial resolver added with narrow-rule precedence and fail-closed default.
- [x] Territorial resolver tests cover Québec, Ottawa, France, Florida, New York, Caribbean neutral states, restricted states and unresolved territories.
- [x] Recipient authentication reference implementation added.
- [x] Authentication registry schema added.
- [x] Credential lifecycle includes ACTIVE/SUSPENDED/REVOKED account handling, credential validity windows, revocation, duplicate-ID rejection and rotation.
- [x] Stored credentials use salted PBKDF2-HMAC-SHA256 verifiers; raw secrets are not intended for repository persistence.
- [x] Integrated authentication + territorial resolution + rights authorization engine added.
- [x] Authentication and integrated authorization test suites added for success, wrong secret, suspended account, revoked/expired/not-yet-valid credential, rotation, neutral rights, restricted denial and fail-closed behavior.
- [x] Controlled-delivery reference primitive added for private/local package sources and authorized output destinations.
- [x] Delivery binds authenticated subject, territorial state, licence acceptance, release identity, licence/policy hashes and exact package SHA-256.
- [x] Delivery performs pre-copy, copied-file and post-copy package-hash verification before atomic destination promotion.
- [x] Controlled-delivery tests added for privileged/neutral allow paths and authentication, territory, identity, policy, release, package and path failure cases.
- [x] Hash-chained append-only audit log reference added.
- [x] Audit append now verifies the entire existing chain before adding a new event.
- [x] Audited delivery wrapper persists both ALLOW and DENY outcomes without persisting the presented raw credential secret.
- [x] Adversarial end-to-end suite added for wrong-secret, restricted-territory, neutral/privileged mismatch, acceptance-identity substitution, release substitution, package tamper, licence/policy substitution, audit tampering and secret-field injection.
- [x] Extended 18-scenario adversarial suite added for source symlinks, source/destination collapse, missing manifest/acceptance fields, duplicate subject records, audit deletion and other bypass/integrity cases.
- [x] Controlled-distribution threat model v0.1 added with explicit in-scope and residual/out-of-scope risks.
- [x] Private deployment specification v0.1 added, separating public governance, authorization, private package vault and delivery trust zones.
- [x] Clean-room verification harness added to bind exact package, active licence and territorial-policy hashes and execute all reference/adversarial suites.

## Verification note

The reference test code and adversarial suites are present and reviewable. A complete clean execution of the current public repository state has not yet been recorded from this assistant's sandbox because direct reconstruction through `raw.githubusercontent.com` was unavailable in the earlier lab environment. This infrastructure limitation is not counted as a TEBDLC test failure. Runtime execution remains part of the final clean-room verification gate.

## Blocking before controlled source distribution

- [ ] Deploy/operate the controlled-delivery reference outside globally public GitHub against a private controlled package store.
- [ ] Execute the complete reference and adversarial suites against that deployed/private-package environment and persist results/hashes; code presence alone is not a PASS.
- [ ] Add production operational controls appropriate to the selected hosting environment (TLS, secret/KMS handling, service isolation, ACLs, rate limiting, monitoring and backup/recovery as applicable).
- [ ] Applicable mandatory-law/export/sanctions review and any required operational adjustment.
- [ ] Assemble the exact controlled `v0.1.0-alpha` package and create its immutable release manifest and package SHA-256.
- [ ] Run `distribution/clean_room_verify.py` against that exact package, active licence and territorial policy and persist a passing verification record.
- [ ] Persist immutable release manifest, verification record, policy/licence hashes and final audit checkpoint for the delivered candidate.

## External legal status

The project licence is active as TEBDLC project policy. No claim is made that it has received governmental, judicial, or specialist legal certification. Mandatory applicable law prevails where required, without silently rewriting historical distribution provenance.

## Hard publication invariant

**DO NOT COPY THE COMPLETE CONTROLLED TEBDLC SOURCE PACKAGE TO PUBLIC `main` WHILE ANY CONTROLLED-DISTRIBUTION BLOCKER ABOVE REMAINS OPEN.**

The public repository may continue to host intentionally global governance, policy, provenance formats, release metadata, and documentation that does not disclose controlled source material.

## Release identity

Candidate: `v0.1.0-alpha`

The final controlled package must receive its own immutable content hash, manifest, licence version, territorial-policy version, build/verification record and audit checkpoint before delivery.
