# TEBDLC Controlled Distribution — Threat Model v0.1

Status: PRE-RELEASE SECURITY MODEL

## Assets

Protected assets include the controlled TEBDLC package, its source provenance, licence/policy bindings, recipient authorization state, falsification privileges, release hashes, and audit history.

## Security objectives

1. A RESTRICTED recipient must not receive the controlled package through the reference delivery path.
2. A NEUTRAL recipient may receive authorized source-use rights but must not obtain the formal TEBDLC falsification right.
3. A package different from the authorized immutable package hash must not be delivered.
4. Licence/policy/release substitutions must fail closed.
5. Authentication failure, ambiguous territory, malformed state, or implementation error must not silently become ALLOW.
6. Historical distribution records must make tampering detectable.
7. Raw credentials and authentication secrets must not be written to the audit record.

## Adversary capabilities considered

The reference model assumes an adversary may:

- present an incorrect or stolen credential;
- attempt credential replay after revocation/expiry;
- alter declared territorial data in an account registry;
- attempt to use a NEUTRAL acceptance as PRIVILEGED;
- substitute another recipient's acceptance record;
- alter the release identifier;
- alter licence/policy hashes;
- modify the package after manifest generation;
- corrupt a copied package;
- attempt to append to a previously tampered audit chain;
- inject forbidden secret-bearing fields into audit events;
- request an unknown or unauthorized action;
- exploit unresolved geographic data to seek permissive fallback.

## Fail-closed boundaries

The system must DENY when it cannot establish all required bindings:

`identity -> territorial state -> requested right -> licence acceptance -> release manifest -> package hash`

Unknown data does not imply neutrality or privilege.

## Out of scope for the reference implementation

The current reference implementation is not itself a production perimeter. The following require deployment-specific controls:

- compromise of the host operating the distributor;
- administrator/root compromise;
- theft of the private package from storage outside the distributor;
- recipient redistribution after legitimate delivery;
- physical compromise of recipient or distribution hardware;
- supply-chain compromise below the language/runtime/OS layer;
- legal identity verification beyond the configured authorization identity;
- trustworthy real-world territorial attestation;
- denial-of-service resistance and network edge protections;
- hardware-backed credential storage;
- remote attestation;
- cryptographic signing keys and HSM/KMS lifecycle;
- disaster recovery and multi-party administrative control.

## Required production hardening

Before operating a live controlled distributor, prefer:

- isolated private package storage inaccessible from the public web root;
- short-lived credentials or signed challenges instead of reusable shared secrets;
- MFA for administrative operations;
- encrypted transport;
- least-privilege service identity;
- filesystem/storage ACLs;
- immutable/off-host copies of audit heads or signed audit checkpoints;
- rate limiting and brute-force detection;
- administrative separation between policy editing and package delivery;
- independent backup and recovery verification;
- monitoring for repeated denied territorial/credential attempts;
- release/package signing in addition to hashing;
- deterministic build/release manifests and clean-room verification.

## Residual truth

The reference controls reduce and expose defined bypass classes; they do not create an absolute guarantee that controlled source cannot be copied after an authorized recipient receives it. Territorial control is therefore a combination of licence rights, authorization, controlled initial delivery, provenance, auditability, and operational security.
