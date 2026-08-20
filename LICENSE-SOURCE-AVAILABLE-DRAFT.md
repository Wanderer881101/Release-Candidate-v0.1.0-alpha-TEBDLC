# TEBDLC Sovereign Source-Available Licence — v0.1

Status: **ACTIVE PROJECT LICENCE v0.1**

Copyright and original TEBDLC intellectual property remain with their respective recorded owner(s). Nothing in this licence transfers authorship or ownership by implication.

This is a source-available territorial licence and is not represented as an OSI open-source licence. Mandatory applicable law prevails where it requires otherwise.

## Territorial classification

Access and rights are governed by the versioned `TERRITORIAL_DISTRIBUTION_POLICY.md` and its machine-readable annexes. The territorial policy distinguishes `PRIVILEGED`, `NEUTRAL`, and `RESTRICTED` classifications.

## Rights matrix

Subject to this licence, the applicable territorial policy, attribution/provenance requirements, and mandatory law:

| Right | PRIVILEGED | NEUTRAL | RESTRICTED |
|---|---:|---:|---:|
| Inspect/read authorized source | YES | YES | NO |
| Compile/build | YES | YES | NO |
| Execute | YES | YES | NO |
| Test and benchmark | YES | YES | NO |
| Falsify TEBDLC claims / submit falsification records | YES | **NO** | NO |
| Modify for private evaluation | YES | YES | NO |

**The sole TEBDLC project-right difference between `PRIVILEGED` and `NEUTRAL` under licence v0.1 is falsification:** privileged recipients may perform and submit TEBDLC falsification work under the falsification regime; neutral recipients may not exercise that licence-granted falsification right.

Ordinary testing, benchmarking, debugging, compatibility testing, and private evaluation by a NEUTRAL recipient remain permitted provided they are not represented, submitted, registered, or exercised as a TEBDLC falsification under the project's falsification regime.

## Rights not granted by v0.1

Unless separately authorized in writing, this licence does **not** grant any recipient, including PRIVILEGED recipients, the right to:

- redistribute the controlled TEBDLC source package;
- redistribute controlled TEBDLC binaries as a substitute distribution;
- publish controlled-source modifications;
- sublicense TEBDLC;
- sell, license, or commercialize a derivative or integration incorporating controlled TEBDLC source.

Visibility or possession of source does not create these rights by implication.

## Falsification and attribution

Only a recipient classified `PRIVILEGED` may exercise the TEBDLC licence-granted falsification right.

An authorized falsification must preserve at minimum:

- TEBDLC version and exact commit/hash being tested;
- TEBDLC-originated intellectual-property attribution;
- falsifier/contributor identity or declared attribution;
- falsifier/contribution version;
- provenance of submitted material;
- evidence hashes;
- applicable licence version;
- applicable territorial-policy version.

TEBDLC-originated IP and falsifier/contributor-originated IP must not be silently merged into a single authorship claim. Historical falsification records must remain attributable and versioned even when a later TEBDLC release incorporates a correction or gain derived from them. See `FALSIFICATION_POLICY.md` and the isolated `falsification-registry` branch.

A `NEUTRAL` recipient receives no licence-granted right to register, submit, publish, or participate in TEBDLC falsification as defined by that regime.

## Territorial neutrality

`NEUTRAL` means neither territorially privileged nor territorially restricted. It does not mean unrestricted rights. Neutral recipients receive the same v0.1 source-use rights as privileged recipients **except for the falsification right**, which is reserved to PRIVILEGED recipients.

## Restricted territories

A `RESTRICTED` classification grants no right under this licence to receive or use the controlled complete TEBDLC source package. Public material deliberately published outside the controlled package remains governed by the notices applicable to that public material and by mandatory law.

## Public repository boundary

Material published in the public Release Candidate repository is globally readable and must be deliberately designated for global publication. Publication of governance metadata or documentation does not itself authorize receipt of the controlled complete source package.

The public GitHub repository is not the controlled distribution endpoint for territorially governed TEBDLC source.

## Versioning and provenance

Every controlled distribution should record at minimum the TEBDLC version/commit, licence version, territorial-policy version, territorial classification, authorization event, and timestamp. A later licence or territorial-policy revision must not silently rewrite the recorded terms associated with an earlier distribution event.

## Mandatory-law reservation

This document states the project's active licence policy. It does not claim certification, governmental approval, or a judicial determination of enforceability. Where mandatory applicable law requires a different result, that mandatory law prevails and the project policy may be revised prospectively while preserving historical provenance.
