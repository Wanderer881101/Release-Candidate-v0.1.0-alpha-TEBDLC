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

## Assumption of risk

TEBDLC is provided for use only by recipients who knowingly accept the risks associated with obtaining, compiling, executing, testing, modifying, integrating, configuring, or otherwise using the technology.

To the maximum extent permitted by applicable law, the recipient assumes the risks arising from their use of TEBDLC, including risks that are known, unknown, foreseeable, unforeseeable, documented, undocumented, emergent, or produced through interaction with other software, hardware, networks, data, configurations, environments, modifications, or systems.

The recipient is responsible for determining whether TEBDLC is appropriate for the environment, purpose, system, data, and circumstances in which the recipient chooses to use it. The recipient is responsible for appropriate isolation, backups, testing, validation, authorization, supervision, operational controls, and recovery measures relevant to that use.

## User conduct and responsibility

The recipient and user remain responsible for their own conduct, decisions, configurations, modifications, integrations, deployments, commands, inputs, outputs, targets, systems, data, and uses of TEBDLC.

Access to, possession of, or authorization to use TEBDLC does not constitute approval, direction, sponsorship, authorization, endorsement, or participation by the TEBDLC author(s) or rightsholder(s) in an act performed by a user.

The user is responsible for obtaining any permission, consent, authority, licence, or other authorization required for the systems, data, networks, devices, services, or environments on which the user chooses to act.

To the maximum extent permitted by applicable law, the TEBDLC author(s), rightsholder(s), and recorded contributor(s) are not responsible merely by reason of authorship, ownership, contribution, publication, or authorized distribution for independent acts, misuse, unauthorized acts, unlawful acts, modifications, combinations, deployments, or decisions made by a recipient or third party.

No provision of this section grants permission to perform an act that is otherwise prohibited by this licence or by applicable law.

## No warranty

To the maximum extent permitted by applicable law, TEBDLC is provided **AS IS** and **AS AVAILABLE**, without warranties or representations, express or implied, including warranties of merchantability, fitness for a particular purpose, non-infringement, uninterrupted operation, absence of defects, correctness of results, security, compatibility, or absence of harmful or unexpected effects.

No documentation, test result, benchmark, proof artifact, validation record, release designation, or successful prior execution constitutes a guarantee that another use, environment, configuration, modification, or future execution will produce the same result or be free of harmful effects.

## Limitation of liability

To the maximum extent permitted by applicable law, the TEBDLC author(s), rightsholder(s), and recorded contributor(s) shall not be liable solely by reason of their authorship, ownership, contribution, publication, or authorized distribution for indirect, incidental, special, consequential, exemplary, or similar damages arising from a recipient's or third party's use, misuse, configuration, modification, integration, deployment, or independent conduct involving TEBDLC.

Nothing in this licence excludes or limits liability that cannot lawfully be excluded or limited under mandatory applicable law.

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
