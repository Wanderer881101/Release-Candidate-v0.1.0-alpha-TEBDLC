# ONTOLOGIE MULTI-AXES DES GAINS — TEBDLC

**Jonathan Therrien, Marieville, Québec.**

Horodatage : 2026-08-19 06:55:50 America/Montreal
Statut : FORMALISATION CANDIDATE / À APPROFONDIR

## 1. Principe

Les sortes de gains ne doivent pas être empilées dans une liste plate si elles décrivent des aspects différents. Un même gain peut simultanément être fractionnaire, variant, événementiel, proliférable, litigieux et validé sans contradiction.

TEBDLC doit donc préférer une ontologie multi-axes à un enum exclusif unique.

## 2. Axe E — État épistémique

Décrit ce qui est démontré au sujet du gain :

    EMERGENT
    UNKNOWN
    VALIDATED
    ASSIMILATED
    REJECTED

Cet axe ne décrit ni sa quantité ni sa provenance.

## 3. Axe Q — Quantification

Décrit la forme quantitative disponible :

    UNQUANTIFIED
    EXACT_INTEGER
    EXACT_FRACTIONAL
    MEASURED_WITH_UNCERTAINTY
    SYMBOLIC_EXACT

`UNQUANTIFIED` n'est jamais zéro.

## 4. Axe M — Morphologie

Décrit la forme structurelle du gain :

    ATOMIC
    PARTIAL
    FRACTIONAL
    VARIANT
    COMPOSITE
    MULTIPLE_OUTPUT
    LATENT
    IMPOTENT_RELATIVE_TO_THRESHOLD

Ces valeurs pourront être raffinées. Elles ne doivent pas être utilisées comme preuve d'état épistémique.

## 5. Axe D — Dynamique

Décrit le comportement dans le temps ou la descendance :

    STABLE
    EVENT_BOUND
    CONDITIONAL
    DORMANT
    PROLIFERABLE
    PROLIFERATED
    SPONTANEOUSLY_OBSERVED
    EXPIRING_CANDIDATE

`PROLIFERABLE` décrit une capacité; `PROLIFERATED` décrit un fait observé. Ils ne sont donc pas pléonastiques.

## 6. Axe P — Provenance

Décrit d'où vient le gain ou ses preuves :

    OBSERVATION
    TEST
    CI
    REPOSITORY
    CONVERSATION
    AGENT
    HUMAN
    SIMULATION
    HARDWARE
    EXTERNAL_SOURCE
    COMPOSITE_PROVENANCE

La provenance n'accorde aucune autorité implicite.

## 7. Axe A — Admissibilité / légitimité

Décrit la possibilité d'utiliser ou d'assimiler le gain sans falsifier sa réalité fonctionnelle :

    ADMISSIBLE
    UNKNOWN_ADMISSIBILITY
    LICENSED
    LITIGIOUS
    CONTAMINATED
    STOLEN
    ILLEGAL
    QUARANTINED

Un gain peut être fonctionnellement réel tout en ayant une admissibilité nulle ou inconnue.

## 8. Axe T — Temporalité

Décrit la position temporelle :

    observed_at
    valid_from
    valid_until
    event_window
    persistence_window
    lineage_position

La temporalité doit rester donnée structurée plutôt qu'un simple adjectif lorsque possible.

## 9. Axe I — Identité

Décrit le sujet réel auquel le gain est attribué :

    subject_id
    entity_kind
    identity_evidence
    identity_confidence_or_unknown
    continuity_claim

Cet axe est central pour prévenir les gains chimères. Une identité partagée techniquement n'est pas automatiquement une identité réelle unique.

## 10. Axe R — Relations

Les relations ne sont pas des types de gain. Elles relient des gains sans les modifier :

    VARIANT_OF
    DEPENDS_ON
    DERIVED_FROM
    PART_OF
    COMPOSES_WITH
    PROLIFERATES_TO
    REFUNDS
    CONFLICTS_WITH
    COMPATIBLE_WITH
    SAME_ENTITY
    DISTINCT_ENTITY
    SAME_CONTEXT
    DISTINCT_CONTEXT
    OCCURS_BEFORE
    OCCURS_AFTER

Une relation doit posséder sa propre provenance/preuve si elle influence un résultat.

## 11. Axe Z — Zéro typé

Le zéro n'est pas un état général du gain. Il appartient à un type de propriété ou de résultat défini dans le catalogue fermé :

    ZERO_EXISTENCE
    ZERO_QUANTITY
    ZERO_VARIATION
    ZERO_COVERAGE
    ZERO_EXPRESSION
    ZERO_ACTIVATION
    ZERO_ADMISSIBILITY
    ZERO_DEBT
    ZERO_CONFLICT
    ZERO_CHIMERA_CONSOLIDATION
    ZERO_RESULT
    ZERO_RESIDUAL
    ZERO_PROLIFERATION_OBSERVED
    ZERO_OCCURRENCE

Aucun de ces zéros ne se propage automatiquement vers un autre.

## 12. Axe C — Composabilité

Deux gains ne sont opérables ensemble que si une règle dédiée le permet. La composabilité doit examiner au minimum :

    domain
    reference
    context
    dimension/unit
    identity compatibility
    temporal compatibility
    provenance constraints
    relation evidence

La simple égalité numérique n'est jamais une preuve de composabilité.

## 13. Axe S — Support / couverture

Pour les gains représentant une couverture d'éléments, la fraction seule est insuffisante. Il faut pouvoir identifier le support :

    support(G) = ensemble ou description canonique des éléments couverts

Deux gains `3/10` peuvent avoir :

    support identique
    support disjoint
    support partiellement chevauchant
    support inconnu

Aucune addition de couverture n'est admise sans cette information.

## 14. Représentation candidate d'un gain

Une représentation future pourrait prendre la forme conceptuelle :

    Gain = {
      identity,
      epistemic_state,
      quantification,
      morphology,
      dynamics,
      provenance,
      admissibility,
      temporality,
      support,
      context,
      evidence,
      relations
    }

Cette structure n'est pas encore une API canonique. Elle décrit les dimensions qui doivent rester séparables pour éviter perte de sens et pléonasmes.

## 15. Critère anti-pléonasme

Deux termes de gain sont considérés non pléonastiques s'ils peuvent varier indépendamment l'un de l'autre sur au moins un exemple valide.

Exemple :

    PROLIFERABLE = true
    PROLIFERATED = false

est possible; les deux notions sont donc distinctes.

En revanche, deux termes qui ne peuvent jamais être distingués par état, preuve, temporalité, quantité ou relation doivent être fusionnés ou abandonnés.

## 16. Principe de développement

Avant d'ajouter une nouvelle sorte de gain, TEBDLC doit demander :

1. quel axe décrit-elle ?
2. peut-elle varier indépendamment des termes existants ?
3. possède-t-elle une arithmétique ou une sémantique différente ?
4. quels contre-exemples la distinguent ?
5. peut-elle être testée ?
6. sa création préserve-t-elle tous les gains précédents ?

Si aucune réponse distinctive n'existe, le terme est probablement redondant.

---

**Jonathan Therrien, Marieville, Québec.**
**TEBDLC — Tous droits réservés sauf autorisation explicite du propriétaire.**