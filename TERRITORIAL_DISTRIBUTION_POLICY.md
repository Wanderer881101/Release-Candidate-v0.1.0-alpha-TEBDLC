# TEBDLC — Sovereign Territorial Distribution Policy v0.1

Status: DRAFT POLICY / PRE-RELEASE
Policy version: 0.1
Applies to: TEBDLC source-available distribution

> This document records the project's intended distribution policy. It is not legal advice and does not by itself replace a reviewed software licence, applicable export-control law, sanctions law, or other mandatory law.

## 1. Distribution model

TEBDLC is intended to use a **source-available sovereign/territorial** distribution model rather than an OSI open-source licence.

The complete restricted source distribution is not intended to be published indiscriminately through the public GitHub repository. The public repository may contain public-facing documentation, governance material, release metadata, verification information, and other material deliberately designated public.

## 2. Territorial states

Policy v0.1 distinguishes three territorial states:

- **PRIVILEGED** — explicitly favored under the TEBDLC distribution policy.
- **NEUTRAL** — neither privileged nor restricted by TEBDLC territorial policy; access remains subject to the applicable licence, distribution controls, and mandatory law.
- **RESTRICTED** — explicitly restricted or restricted by the default rule.

A neutral classification must never be interpreted as a privilege, preference, endorsement, or restriction.

## 3. Privileged territories — v0.1

The initial privileged territorial classes are:

1. **Québec, Canada** — PRIVILEGED.
2. **France** — PRIVILEGED.
3. **Switzerland** — PRIVILEGED.
4. **Belgium** — PRIVILEGED.
5. **Florida, United States of America** — PRIVILEGED as the sole privileged U.S. state under policy v0.1.

## 4. Neutral territories — v0.1

**The Caribbean in its entirety is NEUTRAL.**

For avoidance of doubt:

- the Caribbean receives **no TEBDLC territorial privilege**;
- the Caribbean receives **no TEBDLC territorial restriction** merely by belonging to the Caribbean;
- neutral status is distinct from privileged and restricted status;
- a future machine-readable geographic annex should enumerate the geographic scope used for deterministic implementation without changing this neutral status by implication.

Florida is governed by its explicit PRIVILEGED U.S. subdivision rule and is not made privileged merely by any Caribbean geographic classification.

## 5. Explicit restrictions and default rule

1. **Ottawa, Ontario, Canada is explicitly RESTRICTED.**
2. **The Middle East in its entirety is explicitly RESTRICTED.** Because "Middle East" has no single universally standardized geographic boundary, automated enforcement must use a future versioned enumerated annex rather than infer membership from a vague regional label.
3. The remainder of the United States is RESTRICTED unless subsequently changed by an explicit policy revision; Florida is the current privileged exception.
4. Territories that are neither explicitly PRIVILEGED nor explicitly NEUTRAL are RESTRICTED by default under policy v0.1.

Where classifications overlap, an explicit narrower territorial rule prevails over a broader geographic class until a later policy revision expressly changes it.

No geographic classification changes attribution, provenance, authorship records, falsification records, or intellectual-property notices.

## 6. Distribution controls

IP geolocation alone must not constitute sufficient authorization for access to the complete controlled source package.

A production distribution mechanism should support, at minimum:

- explicit acceptance of the applicable TEBDLC licence;
- declared jurisdiction/territory;
- authenticated account or equivalent authorization identity;
- territorial eligibility evaluation against a versioned policy;
- recording of the policy version used for the decision;
- provenance of the distributed TEBDLC version and commit;
- auditable grant/revocation events;
- compliance with mandatory applicable law.

VPN, proxy, roaming, hosting location, or a transient IP address must not silently redefine the legal or declared territory of an authorized recipient.

## 7. Intellectual property and falsification

Territorial classification does not erase or transfer authorship.

TEBDLC-originated intellectual property must retain its provenance and attribution. A falsifier or contributor must retain attribution and versioned provenance for their own submitted contribution according to `FALSIFICATION_POLICY.md` and the isolated `falsification-registry` branch.

A falsification must identify the TEBDLC version/commit it addresses and the falsifier/contributor version. Incorporation of a valid falsification into a later TEBDLC version must not erase the historical falsification record or its authorship chain.

## 8. Public repository boundary

Until the territorial licence and controlled distribution mechanism are ready, the public Release Candidate repository must **not** be treated as the distribution endpoint for the complete territorially controlled TEBDLC source package.

Material placed on the public `main` branch must be presumed globally readable. Only material deliberately approved for global publication should be committed there.

## 9. Versioning and non-retroactivity

Every change to this policy must receive a new policy version and preserve prior versions in repository history.

A later territorial policy must not silently rewrite which policy governed an earlier distribution event. Distribution records should therefore retain at least:

- policy version;
- TEBDLC release/version;
- TEBDLC commit/hash;
- territorial classification and authorization decision;
- declared territory;
- timestamp;
- applicable licence version.

## 10. Pre-release blockers

Before controlled source distribution begins:

- obtain legal review of the custom source-available licence and territorial classifications;
- create the exhaustive Caribbean geographic annex for deterministic classification while preserving NEUTRAL status;
- create an exhaustive Middle East geographic annex for deterministic RESTRICTED classification;
- define the recipient authorization model;
- define applicable licence rights (view, compile, execute, test, modify, falsify, redistribute, commercialize, etc.);
- implement and test the controlled distribution mechanism;
- define revocation and policy-update handling;
- verify applicable sanctions/export-control and other mandatory legal obligations.

Until these items are resolved, this document is a **versioned technical/governance specification**, not a representation that territorial enforcement is legally complete.
