# TEBDLC v0.1.0-alpha — Legal / Mandatory-Rule Operational Checkpoint

Status: **OPERATIONAL LEGAL SCREENING DEFINED — NOT A LEGAL OPINION OR GOVERNMENT CLASSIFICATION**

Review date: 2026-08-20 (America/Toronto)

This checkpoint records mandatory-rule risks and operational blocks for the actual controlled-distribution model. It does not claim legal advice, an export classification ruling, a sanctions permit, or government authorization.

## 1. Canadian export-control classification

Official source reviewed:

- Global Affairs Canada, *A Guide to Canada’s Export Control List — 2026* (in force May 1, 2026): https://www.international.gc.ca/trade-commerce/controls-controles/ecl-lec/index.aspx?lang=eng
- Category 5 — Part 2, “Information Security”: https://www.international.gc.ca/trade-commerce/controls-controles/ecl-lec/export_control_list-guide-liste_exportation_controlee_2026.aspx?lang=eng
- Global Affairs Canada, *Export permits for cryptographic items*: https://www.international.gc.ca/controls-controles/export-exportation/crypto/Crypto_Intro.aspx?lang=eng

Material conclusion for TEBDLC operations:

1. TEBDLC contains security/authentication/integrity functionality and therefore **must be classified against the current Export Control List before an export or transfer from Canada is treated as legally cleared**.
2. This document does **not** assert that TEBDLC is controlled under Category 5 Part 2, nor that an exclusion applies. That classification requires the actual technical facts to be compared with the current control text.
3. Until classification is resolved for the intended transaction, the distribution system must fail closed for exports/transfers outside the scope already legally established by the operator.
4. If TEBDLC is controlled, the applicable individual or general export-permit route must be determined before the transfer. The existence of GEP 45 or GEP 46 is not treated as blanket authorization.

Operational state: `EXPORT_CLASSIFICATION_REQUIRED_BEFORE_EXTERNAL_TRANSFER`.

## 2. General Export Permits for cryptography

Official sources reviewed:

- General Export Permit No. 45 — Cryptography for the Development or Production of a Product: https://laws-lois.justice.gc.ca/eng/regulations/SOR-2012-160/FullText.html
- Global Affairs Canada cryptographic export-permit guidance: https://www.international.gc.ca/controls-controles/export-exportation/crypto/Crypto_Intro.aspx?lang=eng

Important restrictions recorded:

- GEP 45 is conditional and purpose-limited; it is not assumed to authorize ordinary TEBDLC distribution.
- GEP 45 does not authorize destinations excluded by its terms, countries on the Area Control List, destinations subject to relevant SEMA/United Nations Act restrictions, or foreign governments in the circumstances specified by the permit.
- Use of a GEP may carry notification, recordkeeping or other conditions; those conditions must be satisfied before relying on it.

Operational state: `NO_GEP_ASSUMED_WITHOUT_TRANSACTION_SPECIFIC_APPLICABILITY_CHECK`.

## 3. Area Control List and destination controls

Official sources reviewed:

- Justice Laws Website, Area Control List: https://laws-lois.justice.gc.ca/eng/regulations/SOR-81-543/FullText.html
- Global Affairs Canada, military and strategic goods and technology / Area Control List guidance: https://www.international.gc.ca/controls-controles/military-militaires/index.aspx?lang=eng

As reviewed on the checkpoint date, the Area Control List contains the **Democratic People’s Republic of Korea (North Korea)**.

Operational rule:

`ACL_DESTINATION => DENY_EXTERNAL_TRANSFER_UNLESS_LAWFULLY_AUTHORIZED_BY_THE_APPLICABLE_CANADIAN_REGIME`

This rule is external-law gating and is additive to TEBDLC’s own territorial policy; it does not rewrite historical TEBDLC policy records.

## 4. Canadian sanctions screening

Official sources reviewed:

- Global Affairs Canada, Canadian sanctions: https://www.international.gc.ca/world-monde/international_relations-relations_internationales/sanctions/index.aspx?lang=eng
- Consolidated Canadian Autonomous Sanctions List: https://www.international.gc.ca/world-monde/international_relations-relations_internationales/sanctions/consolidated-consolide.aspx?lang=eng

The consolidated list is an administrative aid and **does not itself have force of law**. Relevant regulations must be consulted for the actual recipient/entity/transaction.

Operational rules before a real controlled delivery:

1. screen recipient/account/entity and relevant destination against current Canadian sanctions information;
2. inspect the applicable regulation when a possible match or country restriction exists;
3. fail closed on unresolved identity/sanctions ambiguity;
4. preserve a non-secret screening checkpoint identifier/date/source-set in the delivery provenance;
5. do not silently rewrite historical licence, policy or provenance if external legal rules change later.

Operational state: `SANCTIONS_SCREEN_REQUIRED_PER_REAL_DELIVERY`.

## 5. Québec personal-information obligations

The controlled-delivery design processes recipient/account identifiers, credential identifiers, declared territory, authorization outcomes and audit timestamps. Depending on the real operating context, some or all of these may be personal information.

Official guidance reviewed:

- Commission d’accès à l’information du Québec — private enterprises and organizations: https://www.cai.gouv.qc.ca/protection-renseignements-personnels/information-entreprises-privees
- Scope of the Québec private-sector privacy law: https://www.cai.gouv.qc.ca/protection-renseignements-personnels/information-entreprises-privees/champ-application-loi_entreprises
- Confidentiality incidents and security measures: https://www.cai.gouv.qc.ca/protection-renseignements-personnels/information-entreprises-privees/incidents-confidentialite-mesures-securite-entreprises

Operational controls already aligned with this risk include minimization of persisted secrets, least-privilege access, audit integrity, incident actions and credential revocation. Before processing real third-party recipient data as an operating enterprise, the operator must additionally ensure that collection purposes, required notices/consents where applicable, retention/destruction governance, access limitation, incident handling and other applicable Québec obligations are implemented for the actual business context.

Operational state: `REAL_RECIPIENT_PERSONAL_DATA_REQUIRES_APPLICABLE_PRIVACY_GOVERNANCE`.

## 6. Mandatory-rule precedence and non-rewrite invariant

External mandatory law is an operational constraint on whether a transaction may proceed; it does not retroactively alter historical TEBDLC records.

Required model:

`TEBDLC policy decision + external mandatory-rule checkpoint => final operational delivery eligibility`

Where an external rule blocks or requires authorization for a transaction that TEBDLC’s internal policy would otherwise allow, the operational result must fail closed or wait for the required authorization. The internal historical decision and external adjustment remain separately attributable.

No minus/division semantics are introduced into TEBDLC’s evidence accounting: the external checkpoint is an additional recorded condition/provenance fact, not a subtraction or normalization of an existing gain/evidence element.

## 7. Release consequence

For `v0.1.0-alpha`:

- **Technical freeze readiness:** established by the successful final consolidation/freeze CI gate.
- **External distribution legality:** transaction-dependent and **not automatically certified** by CI or this document.
- **Release may be technically frozen/tagged as an identified candidate/product artifact**, provided the tag/release notes retain the mandatory-rule conditions above and do not represent the release as government-certified or universally authorized for export/distribution.
- **Any real external controlled delivery remains fail-closed until the applicable export classification, destination/sanctions screening and privacy obligations are satisfied for that transaction.**

## 8. Source freshness rule

Because export controls and sanctions can change, the official sources above must be rechecked at the time of each real external distribution decision. A stale checkpoint cannot override newer mandatory law.
