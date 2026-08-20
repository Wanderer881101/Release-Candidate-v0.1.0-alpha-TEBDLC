# TEBDLC — Sovereign Territorial Distribution Policy v0.1

Status: DRAFT POLICY / PRE-RELEASE
Policy version: 0.1
Applies to: TEBDLC source-available distribution

> This document records the project's intended distribution policy. It is not legal advice and does not by itself replace a reviewed software licence, applicable export-control law, sanctions law, or other mandatory law.

## 1. Distribution model
TEBDLC is intended to use a **source-available sovereign/territorial** distribution model rather than an OSI open-source licence. Complete controlled source is not intended for indiscriminate publication through the public GitHub repository.

## 2. Territorial states
- **PRIVILEGED** — explicitly favored.
- **NEUTRAL** — neither privileged nor restricted by TEBDLC territorial policy; mandatory law and licence terms still apply.
- **RESTRICTED** — explicitly restricted or restricted by the default rule.

Neutral must never be interpreted as privilege, endorsement, or restriction.

## 3. Privileged territories — v0.1
1. Québec, Canada.
2. France.
3. Switzerland.
4. Belgium.
5. Florida, United States — sole privileged U.S. state under v0.1.

## 4. Neutral territories — v0.1
**The Caribbean in its entirety is NEUTRAL:** no territorial privilege and no territorial restriction merely by Caribbean membership. A future machine-readable annex will enumerate its geographic scope. Florida remains governed by its explicit privileged rule.

## 5. Explicit restrictions and default rule
**Ottawa, Ontario, Canada is explicitly RESTRICTED.**

**The Middle East in its entirety is explicitly RESTRICTED.** Automated enforcement must use an enumerated annex rather than infer membership from an ambiguous regional label.

In addition, following the project's supplied reference image, the following named countries/territories are explicitly RESTRICTED regardless of whether a particular geographic convention classifies them as Middle Eastern:

- Türkiye (Turkey)
- Cyprus
- Lebanon
- Syria
- Israel
- Jordan
- Iraq
- Iran
- Afghanistan
- Kuwait
- Bahrain
- Saudi Arabia
- Qatar
- United Arab Emirates
- Oman
- Yemen
- Egypt
- Sudan
- Eritrea
- Ethiopia
- Djibouti
- Turkmenistan

Geographic water-body labels appearing in the reference image (Caspian Sea, Red Sea, Gulf of Aden) are not territorial distribution subjects and therefore are not encoded as countries.

The remainder of the United States is RESTRICTED unless changed by explicit revision; Florida is the current privileged exception. Territories neither explicitly PRIVILEGED nor explicitly NEUTRAL are RESTRICTED by default under v0.1.

Where classifications overlap, an explicit narrower territorial rule prevails over a broader geographic class until a later policy revision expressly changes it. Geographic classification never changes attribution, provenance, authorship, falsification records, or intellectual-property notices.

## 6. Distribution controls
IP geolocation alone must not constitute sufficient authorization. Production distribution should require applicable licence acceptance, declared jurisdiction/territory, authenticated authorization identity, evaluation against the versioned territorial policy, logging of policy/licence/TEBDLC versions and commit, auditable grant/revocation events, and compliance with mandatory law. VPN, proxy, roaming, hosting location, or transient IP must not silently redefine a recipient's declared/legal territory.

## 7. Intellectual property and falsification
Territorial classification does not erase or transfer authorship. TEBDLC-originated IP retains provenance and attribution. Falsifiers/contributors retain attribution and versioned provenance for their own submissions under `FALSIFICATION_POLICY.md` and the isolated `falsification-registry` branch. Incorporation into later TEBDLC versions must not erase historical falsification records or authorship chains.

## 8. Public repository boundary
Until the territorial licence and controlled distribution mechanism are ready, the public Release Candidate repository must **not** be treated as the distribution endpoint for the complete territorially controlled source package. Material on public `main` must be presumed globally readable and deliberately approved for global publication.

## 9. Versioning and non-retroactivity
Every policy change must receive a new policy version and preserve prior versions in repository history. Distribution records should retain policy version, TEBDLC version, TEBDLC commit/hash, territorial classification and authorization decision, declared territory, timestamp, and applicable licence version.

## 10. Pre-release blockers
Before controlled source distribution begins:
- obtain legal review of the custom source-available licence and territorial classifications;
- create exhaustive Caribbean geographic annex while preserving NEUTRAL status;
- create exhaustive Middle East geographic annex for deterministic RESTRICTED classification;
- define recipient authorization model and licence rights;
- implement/test controlled distribution and revocation;
- verify applicable sanctions/export-control and other mandatory legal obligations.

Until these are resolved, this is a **versioned technical/governance specification**, not a representation that territorial enforcement is legally complete.
