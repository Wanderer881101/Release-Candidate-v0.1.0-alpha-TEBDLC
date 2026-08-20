# TEBDLC v0.1.0-alpha — Controlled Release Gate

This gate prevents accidental publication of the complete territorially controlled source through a globally public GitHub branch.

## Completed governance prerequisites

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

## Verification note

The authentication/authorization test code is present and reviewable. A direct clean execution from this assistant's sandbox was not recorded because the sandbox could not resolve `raw.githubusercontent.com` to reconstruct the public repository state. This infrastructure limitation is not counted as a TEBDLC test failure. Runtime execution remains part of the final clean-room verification gate.

## Blocking before controlled source distribution

- [ ] Controlled delivery implementation outside globally public GitHub.
- [ ] End-to-end bypass/adversarial testing of territorial decision logic and delivery path.
- [ ] Applicable mandatory-law/export/sanctions review.
- [ ] Final clean-room release verification against the exact controlled package SHA.

## External legal status

The project licence is active as TEBDLC project policy. No claim is made that it has received governmental, judicial, or specialist legal certification. Mandatory applicable law prevails where required, without silently rewriting historical distribution provenance.

## Hard publication invariant

**DO NOT COPY THE COMPLETE CONTROLLED TEBDLC SOURCE PACKAGE TO PUBLIC `main` WHILE ANY CONTROLLED-DISTRIBUTION BLOCKER ABOVE REMAINS OPEN.**

The public repository may continue to host intentionally global governance, policy, provenance formats, release metadata, and documentation that does not disclose controlled source material.

## Release identity

Candidate: `v0.1.0-alpha`

The final controlled package must receive its own immutable content hash, manifest, licence version, territorial-policy version, and build/verification record before delivery.
