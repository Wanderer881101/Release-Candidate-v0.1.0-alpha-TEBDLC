# TEBDLC — Sovereign Territorial Distribution Policy v0.1

Status: DRAFT POLICY / PRE-RELEASE
Policy version: 0.1
Applies to: TEBDLC source-available distribution

> This document records the project's intended distribution policy. It is not legal advice and does not by itself replace a reviewed software licence, applicable export-control law, sanctions law, or other mandatory law.

## 1. Distribution model

TEBDLC is intended to use a **source-available sovereign/territorial** distribution model rather than an OSI open-source licence.

The complete restricted source distribution is not intended to be published indiscriminately through the public GitHub repository. The public repository may contain public-facing documentation, governance material, release metadata, verification information, and other material deliberately designated public.

## 2. Default rule — allowlist

Distribution authorization is positive rather than inferred:

`AUTHORIZED(T) iff T is explicitly present in the privileged territorial allowlist and no explicit exclusion applies.`

A territory absent from the allowlist is **restricted by default** for distribution of the complete controlled source package.

No geographic restriction changes attribution, provenance, authorship records, falsification records, or intellectual-property notices.

## 3. Privileged territories — v0.1

The initial privileged territorial classes are:

1. **Québec, Canada** — privileged.
2. **France** — privileged.
3. **Switzerland** — privileged.
4. **Belgium** — privileged.
5. **The Caribbean in its entirety** — privileged, subject to the explicit Florida rule below and to a future enumerated geographic annex for deterministic implementation.
6. **Florida, United States of America** — privileged as the sole privileged U.S. state under policy v0.1.

## 4. Explicit restrictions and precedence

1. **Ottawa, Ontario, Canada is explicitly restricted.**
2. The remainder of the United States is restricted unless subsequently added by an explicit policy revision; Florida is the current exception.
3. All other territories not expressly included in the privileged allowlist are restricted by default.

Where a broad future geographic authorization and a narrower explicit restriction conflict, the **narrower explicit restriction prevails** until a later policy revision expressly removes it.

## 5. Caribbean scope

The policy intent is to privilege **all Caribbean territories**.

Before automated territorial enforcement is activated, the project must publish a versioned machine-readable annex enumerating the countries, dependencies, overseas territories, islands, and other geographic units treated as Caribbean for TEBDLC distribution purposes. This avoids relying on ambiguous geographic interpretation at runtime.

Florida remains governed by its explicit U.S. exception and must not be inferred solely from the Caribbean annex.

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

Territorial authorization does not erase or transfer authorship.

TEBDLC-originated intellectual property must retain its provenance and attribution. A falsifier or contributor must retain attribution and versioned provenance for their own submitted contribution according to `FALSIFICATION_POLICY.md` and the isolated `falsification-registry` branch.

A falsification must identify the TEBDLC version/commit it addresses and the falsifier/contributor version. Incorporation of a valid falsification into a later TEBDLC version must not erase the historical falsification record or its authorship chain.

## 8. Public repository boundary

Until the territorial licence and controlled distribution mechanism are ready, the public Release Candidate repository must **not** be treated as the distribution endpoint for the complete territorially restricted TEBDLC source package.

Material placed on the public `main` branch must be presumed globally readable. Only material deliberately approved for global publication should be committed there.

## 9. Versioning and non-retroactivity

Every change to this policy must receive a new policy version and preserve prior versions in repository history.

A later territorial policy must not silently rewrite which policy governed an earlier distribution event. Distribution records should therefore retain at least:

- policy version;
- TEBDLC release/version;
- TEBDLC commit/hash;
- authorization decision;
- declared territory;
- timestamp;
- applicable licence version.

## 10. Pre-release blockers

Before controlled source distribution begins:

- obtain legal review of the custom source-available licence and territorial restrictions;
- create the exhaustive Caribbean territorial annex;
- define the recipient authorization model;
- define applicable licence rights (view, compile, execute, test, modify, falsify, redistribute, commercialize, etc.);
- implement and test the controlled distribution mechanism;
- define revocation and policy-update handling;
- verify applicable sanctions/export-control and other mandatory legal obligations.

Until these items are resolved, this document is a **versioned technical/governance specification**, not a representation that territorial enforcement is legally complete.
