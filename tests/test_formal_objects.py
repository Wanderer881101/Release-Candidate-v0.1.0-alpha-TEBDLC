# Jonathan Therrien, Marieville, Québec.

import pytest

from tebdlc.formal_objects import (
    ConsolidationResult,
    ConsolidationStatus,
    GainRelation,
    ProofRef,
    RelationKind,
)
from tebdlc.zero import TypedZero, ZeroKind


def proof(ref: str = "proof:1") -> ProofRef:
    return ProofRef(ref=ref, kind="test", provenance="suite")


def chimera_zero() -> TypedZero:
    return TypedZero.create(
        ZeroKind.CHIMERA_CONSOLIDATION,
        domain="identity",
        reference="session-A",
        context="audit",
        evidence=("proof:identity-conflict",),
        subject="consolidation-A",
    )


def test_relation_requires_evidence():
    with pytest.raises(ValueError, match="requires evidence"):
        GainRelation.create(
            RelationKind.DISTINCT_ENTITY,
            left_gain_id="g1",
            right_gain_id="g2",
            evidence=(),
            context="audit",
        )


def test_relation_identity_is_deterministic():
    a = GainRelation.create(
        RelationKind.DISTINCT_ENTITY,
        left_gain_id="g1",
        right_gain_id="g2",
        evidence=(proof("b"), proof("a")),
        context="audit",
    )
    b = GainRelation.create(
        RelationKind.DISTINCT_ENTITY,
        left_gain_id="g1",
        right_gain_id="g2",
        evidence=(proof("a"), proof("b")),
        context="audit",
    )
    assert a.relation_id == b.relation_id


def test_chimera_requires_typed_chimera_zero():
    with pytest.raises(ValueError, match="ZERO_CHIMERA_CONSOLIDATION"):
        ConsolidationResult.create(
            constituent_gain_ids=("g1", "g2"),
            hypothesis="same entity",
            status=ConsolidationStatus.CHIMERA,
            evidence=(proof(),),
            zero=None,
        )


def test_chimera_zero_does_not_remove_constituent_ids():
    result = ConsolidationResult.create(
        constituent_gain_ids=("g2", "g1", "g2"),
        hypothesis="same entity",
        status=ConsolidationStatus.CHIMERA,
        evidence=(proof(),),
        zero=chimera_zero(),
    )
    assert result.status is ConsolidationStatus.CHIMERA
    assert result.constituent_gain_ids == ("g1", "g2")
    assert result.preserves_constituents
    assert result.zero is not None
    assert result.zero.kind is ZeroKind.CHIMERA_CONSOLIDATION


def test_coherent_result_cannot_carry_chimera_zero():
    with pytest.raises(ValueError, match="only a CHIMERA"):
        ConsolidationResult.create(
            constituent_gain_ids=("g1", "g2"),
            hypothesis="same entity",
            status=ConsolidationStatus.COHERENT,
            evidence=(proof(),),
            zero=chimera_zero(),
        )


def test_consolidation_requires_at_least_two_constituents():
    with pytest.raises(ValueError, match="at least two"):
        ConsolidationResult.create(
            constituent_gain_ids=("g1",),
            hypothesis="same entity",
            status=ConsolidationStatus.UNKNOWN,
            evidence=(proof(),),
        )
