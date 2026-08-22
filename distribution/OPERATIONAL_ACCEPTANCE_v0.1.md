# TEBDLC v0.1.0-alpha — Operational Acceptance Gate

**Jonathan Therrien, Marieville, Québec.**

This document is additive to `RELEASE_GATE_v0.1.0-alpha.md`, `DEPLOYMENT_SPEC_v0.1.md`, `THREAT_MODEL_v0.1.md`, `AUTHORIZATION_SPEC_v0.1.md`, and `CONTROLLED_DELIVERY_v0.1.md`.

It defines the minimum material evidence required before a controlled TEBDLC package may be treated as operationally ready. A checkbox may be marked complete only from persisted evidence; intent, configuration text, or synthetic-only results are not substitutes.

## A. Immutable candidate identity

- [x] Candidate release identifier: `v0.1.0-alpha`.
- [x] Private source commit: `677a28d87164379cb2a268e55cfc30302ebc44ab`.
- [x] Private source root-tree SHA-1: `63658d334ae8c3d280e9ef2c29845fffce2747e6`.
- [x] Real canonical package SHA-256 persisted: `dd15a49e30a2419d504d315c29aa4f25d6c6590202bedbce8f78dc632f426ba3`.
- [x] Real package size and tracked-file count persisted: `162053` bytes / `139` tracked files.
- [x] Final manifest SHA-256 persisted: `ee8cff12529b190b7f9fcf7028a61a32af50f68dc3bfa6c39b24411f85521826`.
- [x] Active licence SHA-256 persisted in the final manifest: `86fddddedbd112c2c8b420d4b31802147a3bce702ff68db3683b816b39e69ac1`.
- [x] Active territorial-policy SHA-256 persisted in the final manifest: `1e0a639c10ae2d124f4d535536788b19912903f310c9e494d57e6fbcba9b6090`.

Evidence: private branch `release-evidence-v0.1.0-alpha`, `PACKAGE_PROOF.json`, `RELEASE_MANIFEST.json`, `SHA256SUMS`.

## B. Package construction and clean-room proof

- [x] Authenticated Git-object assembler implemented fail-closed.
- [x] Every fetched blob must match its Git blob SHA-1.
- [x] Rebuilt root tree must match the bound source root tree before packaging.
- [x] Canonical package rebuild must be byte-identical before acceptance.
- [x] Clean-room verifier binds archive contents back to the expected Git root tree.
- [x] Real package assembled from the bound private Git objects.
- [x] Real package passes clean-room verification.
- [x] `CLEAN_ROOM_PASS` record persisted with package/tree/licence/policy hashes.

Evidence: `CLEAN_ROOM_RECORD.json`, `CLEAN_ROOM_STDOUT.txt`, package SHA-256 and source-tree identity above.

## C. Controlled store and transport

- [x] Verified package stored outside globally public GitHub source exposure, as a private GitHub Actions artifact associated with the private `TEBDLC` repository.
- [x] Package store defaults to deny and exposes no anonymous listing/download path. Material probes deny anonymous access.
- [x] The current material transport path is GitHub private Actions artifact delivery over HTTPS; authenticated HTTPS readback of the exact package passed. This does **not** claim certification of a future external TEBDLC production endpoint.
- [x] Current transport workflow uses least privilege: `actions: read`, `contents: read`; a repository-write negative probe was denied with HTTP `403`.
- [x] Package-at-rest access is constrained by the private repository / GitHub Actions artifact access boundary and authenticated service identity; anonymous readback is materially denied.
- [x] Persisted release/store/adversarial/provenance evidence contains no raw presented secret, and material evidence workflows explicitly scan for runtime-secret leakage.
- [x] Credential rotation and revocation behavior is materially tested: rotation revokes the old credential, the new credential authenticates, explicit revocation of the new credential is enforced, and revoked credentials are denied.
- [x] Abuse-boundary evidence exists for the **current GitHub transport**: GitHub API rate-limit headers are present and the observed limit is `5000`. A future public TEBDLC HTTP API is explicitly `NOT_APPLICABLE_NO_PUBLIC_TEBDLC_HTTP_API` until such an endpoint exists.

Controlled-store evidence: run `32436626437`, artifact `9430960453`, `CONTROLLED_STORE_RECORD.json`; pre-store and post-readback package SHA-256 are identical and byte-for-byte readback is true.
Operational provenance evidence: run `32439124525`, `OPERATIONAL_PROVENANCE_RECORD.json`, `OPERATIONAL_PROVENANCE_SUMMARY.json`.
Transport-boundary evidence: run `32442687045`, `TRANSPORT_BOUNDARY_RECORD.json`, `HTTPS_READBACK_SHA256SUMS`.

## D. Recipient decision and delivery proof

For each real delivery attempt, persist a non-secret record binding:

- recipient/account identifier;
- credential/key identifier (never the raw secret);
- resolved territory and policy version;
- authorization decision and reason;
- accepted licence version/hash;
- requested release identifier;
- expected package SHA-256;
- pre-delivery package SHA-256;
- post-delivery/destination SHA-256 when delivery occurs;
- audit event/checkpoint identifier;
- timestamp in UTC.

- [x] Dedicated material per-attempt provenance record persists all required bindings for one ALLOW, one authentication DENY and one restricted-territory DENY without storing raw secrets.
- [x] Recipient provenance is bound to audit sequence and audit-entry hash for every recorded attempt.

Material tests required:

- [x] At least one permitted delivery completes with pre/post SHA equality against the exact package `dd15a49e30a2419d504d315c29aa4f25d6c6590202bedbce8f78dc632f426ba3`.
- [x] At least one policy-denied request produces no package delivery.
- [x] At least one authentication failure produces no package delivery.
- [x] At least one integrity mismatch/tamper scenario fails closed.
- [x] Audit chain remains valid after ALLOW and DENY outcomes; deliberate audit tampering is detected.

Evidence: `CONTROLLED_DISTRIBUTION_RECORD.json`, `ADVERSARIAL_PRIVATE_ENVIRONMENT_RECORD.json`, `PRIVATE_PACKAGE_ADVERSARIAL_RECORD.json`, `OPERATIONAL_PROVENANCE_RECORD.json`; adversarial run `32438606191`; provenance run `32439124525`.

## E. Falsification and intellectual-property provenance

- [x] Formal falsification is accepted only under the territorial/rights policy in force: a material PRIVILEGED `FALSIFY` request was allowed while restricted conditions were denied.
- [x] NEUTRAL users remain outside the formal falsification regime while retaining permitted ordinary evaluation rights.
- [x] Formal falsification provenance binds the original TEBDLC release identity and the falsifier/contributor identity/version provenance.
- [x] Contributor/falsifier intellectual-property attribution is additive; TEBDLC origin/provenance is preserved and not rewritten.
- [x] Falsification registry isolation is materially tested: candidate HEAD and tree remained unchanged and the validation fixture was not persisted into the product candidate.

Evidence: run `32442926737`, `FALSIFICATION_PROVENANCE_RECORD.json`, `FALSIFICATION_PROVENANCE_SUMMARY.json`; summary `overall_pass=true`.

## F. Operations and resilience

- [x] Monitoring materially detects authorization failures, integrity failures, repeated denied requests and delivery-error counters without recording raw secrets.
- [x] Backup/recovery procedure materially captures package, manifest, licence, policy and audit state.
- [x] Recovery is destructively tested in disposable state and preserves package/manifest/licence/policy hashes plus audit-chain validity.
- [x] Incident actions define package/credential revocation, audit preservation and recipient notification where applicable.
- [x] Current validation deployment boundaries are documented and materially exercised: private GitHub artifact store, ephemeral GitHub-hosted runner, read-only delivery token boundary, separate evidence branch, separate falsification registry and immutable package identity. This does not claim a future external network service has been deployed.

Evidence: run `32439558264`, `OPERATIONAL_RESILIENCE_RECORD.json`, `MONITORING_RECORD.json`; transport-boundary run `32442687045`.

## G. Legal/mandatory-rule checkpoint

- [x] Applicable mandatory-rule domains for the actual controlled-distribution model have been operationally reviewed: Canadian export controls / cryptographic-item classification, Area Control List, Canadian sanctions screening, and applicable Québec private-sector personal-information obligations.
- [x] Required restrictions are recorded as dated, sourced, additive operational adjustments in `LEGAL_MANDATORY_RULE_CHECKPOINT_v0.1.md`: export classification before external transfer, transaction-time destination/sanctions screening, fail-closed ambiguity handling, and applicable privacy governance before real recipient personal-data processing.
- [x] No historical licence/policy/provenance record is silently rewritten after an external legal adjustment; mandatory-law outcomes are recorded as separate additive provenance/checkpoint facts.

This section records an **operational legal-risk checkpoint, not a legal opinion, government export classification, sanctions permit or universal distribution authorization**. Applicability remains transaction-dependent and official sources must be rechecked at the time of real external distribution.

Evidence: `LEGAL_MANDATORY_RULE_CHECKPOINT_v0.1.md`, review date 2026-08-20, official Global Affairs Canada / Justice Laws / Commission d’accès à l’information du Québec sources cited therein.

## H. Final freeze

- [x] Technical consolidation/freeze gate completed successfully on `main` after all required persisted material evidence families were present and no explicit failed result was detected.
- [x] Sections A–G are materially satisfied for **freeze readiness**, with external legal requirements represented as fail-closed transaction-time conditions rather than fabricated CI certification.

Final release binding must include at minimum:

`release_id ↔ source_commit ↔ source_tree_sha1 ↔ package_sha256 ↔ manifest_sha256 ↔ licence_sha256 ↔ territorial_policy_sha256 ↔ clean_room_record ↔ distribution/audit_checkpoint ↔ mandatory-rule checkpoint`

`v0.1.0-alpha` is technically and operationally ready to be frozen/tagged as the identified release candidate/product artifact. Any real external controlled delivery remains subject to the transaction-time mandatory-rule conditions documented in `LEGAL_MANDATORY_RULE_CHECKPOINT_v0.1.md`.
