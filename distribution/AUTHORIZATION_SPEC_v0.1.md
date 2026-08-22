# TEBDLC Controlled Distribution — Authorization Specification v0.1

**Jonathan Therrien, Marieville, Québec.**

Status: PRE-IMPLEMENTATION SPECIFICATION
Applies to: controlled TEBDLC source distribution

## 1. Objective

This specification defines the minimum deterministic authorization contract that must exist before the complete controlled TEBDLC source package is distributed outside the canonical private development environment.

The public GitHub repository is not the controlled delivery endpoint.

## 2. Inputs

Every authorization decision must bind at minimum:

- recipient authorization identity;
- recipient-declared territory/jurisdiction;
- territorial-policy version;
- resulting territorial state: `PRIVILEGED`, `NEUTRAL`, or `RESTRICTED`;
- TEBDLC licence version;
- requested TEBDLC release/version;
- exact controlled-package content hash;
- requested rights/action;
- licence acceptance record identifier;
- decision timestamp.

IP address or geolocation may be used as a risk signal but must not, by itself, establish authorization.

## 3. Decision semantics

`RESTRICTED` -> controlled package delivery denied.

`NEUTRAL` -> source-use rights granted by licence v0.1 except the formal TEBDLC falsification right.

`PRIVILEGED` -> source-use rights granted by licence v0.1 including the formal TEBDLC falsification right.

The authorization engine must not silently promote `NEUTRAL` to `PRIVILEGED` and must not infer a falsification right from ordinary testing or benchmarking rights.

## 4. Explicit-rule precedence

When a broad geographic class overlaps a narrower explicit territorial rule, the narrower explicit rule governs according to the versioned territorial policy.

No runtime implementation may invent an unlisted territorial classification. Ambiguous geographic classes must be resolved through versioned enumerated annexes before automated enforcement.

## 5. Licence acceptance record

Before an authorized package is delivered, the system must persist an immutable or append-only acceptance record containing at minimum:

- `acceptance_id`;
- authorization identity;
- licence version and licence hash;
- territorial-policy version and policy hash;
- territorial state;
- TEBDLC release identifier;
- package hash;
- acceptance timestamp;
- acceptance mechanism/version.

Acceptance of one package/hash must not silently authorize a different package/hash or later licence version.

## 6. Distribution-event record

Every attempted controlled delivery must generate an auditable event, including denials.

Minimum fields:

- `event_id`;
- `acceptance_id` when applicable;
- authorization identity;
- declared territory;
- resolved territorial state;
- policy version/hash;
- licence version/hash;
- TEBDLC release/version;
- package hash;
- requested action;
- decision: `ALLOW` or `DENY`;
- machine-readable reason code;
- timestamp;
- authorization-engine version.

Records must not contain secrets, credentials, raw authentication tokens, or unnecessary personal data.

## 7. Recommended reason codes

- `ALLOW_PRIVILEGED`
- `ALLOW_NEUTRAL`
- `DENY_RESTRICTED_TERRITORY`
- `DENY_UNRESOLVED_TERRITORY`
- `DENY_NO_LICENCE_ACCEPTANCE`
- `DENY_LICENCE_VERSION_MISMATCH`
- `DENY_PACKAGE_HASH_MISMATCH`
- `DENY_RIGHT_NOT_GRANTED`
- `DENY_AUTHENTICATION_FAILURE`
- `DENY_POLICY_INTEGRITY_FAILURE`

## 8. Package integrity

Authorization must apply to an immutable package identity. Before delivery, the package hash must equal the hash recorded in the release manifest. A mismatch is a hard denial and must be logged.

The release manifest should itself bind:

- release identifier;
- source commit(s);
- package hash;
- build/assembly procedure version;
- licence version/hash;
- territorial-policy version/hash;
- verification-record hash.

## 9. User responsibility boundary

Authorization to receive TEBDLC is not authorization by the TEBDLC author(s) for a recipient's later conduct. Recipient conduct and assumption of risk remain governed by the active licence.

The authorization system records access decisions; it does not certify that a recipient's intended or later use is safe, lawful, appropriate, or endorsed.

## 10. Fail-closed requirements

The controlled distributor must deny delivery when:

- territorial state cannot be resolved deterministically;
- policy or licence integrity verification fails;
- package hash differs from the authorized manifest;
- required licence acceptance is absent;
- requested right is not granted for the resolved territorial state;
- authentication/authorization identity cannot be established.

A software error must not default to `ALLOW`.

## 11. Required tests before activation

At minimum test:

- PRIVILEGED allow path;
- NEUTRAL allow path without falsification right;
- RESTRICTED deny path;
- explicit narrower-rule precedence;
- missing/ambiguous territory;
- altered territorial policy;
- altered licence;
- altered package;
- stale acceptance against newer package/licence;
- falsification request from NEUTRAL;
- authentication failure;
- duplicate/replayed delivery event;
- audit-log integrity and deterministic reproduction of a historical decision.

## 12. Non-retroactivity

Historical authorization/distribution records must retain the policy, licence, package, and engine versions that governed the event. A later policy change may govern later requests but must not rewrite the historical decision context.
