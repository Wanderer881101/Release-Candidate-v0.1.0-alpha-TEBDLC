# Jonathan Therrien, Marieville, Québec.

import pytest

from tebdlc.zero import TypedZero, ZeroKind


def make_zero(kind: ZeroKind) -> TypedZero:
    return TypedZero.create(
        kind,
        domain="integrity",
        reference="baseline-A",
        context="session",
        evidence=("proof:1",),
        subject="subject-A",
    )


def test_typed_zero_requires_evidence():
    with pytest.raises(ValueError, match="requires at least one evidence"):
        TypedZero.create(
            ZeroKind.RESULT,
            domain="integrity",
            reference="baseline-A",
            context="session",
            evidence=(),
        )


def test_zero_kind_does_not_propagate_to_other_kind():
    result_zero = make_zero(ZeroKind.RESULT)
    assert result_zero.implies(ZeroKind.RESULT)
    assert not result_zero.implies(ZeroKind.EXISTENCE)
    assert not result_zero.implies(ZeroKind.COVERAGE)


def test_chimera_zero_does_not_imply_constituent_existence_zero():
    chimera = make_zero(ZeroKind.CHIMERA_CONSOLIDATION)
    assert chimera.kind is ZeroKind.CHIMERA_CONSOLIDATION
    assert not chimera.implies(ZeroKind.EXISTENCE)


def test_zero_scope_is_explicit():
    a = make_zero(ZeroKind.RESULT)
    b = TypedZero.create(
        ZeroKind.RESULT,
        domain="integrity",
        reference="baseline-A",
        context="other-session",
        evidence=("proof:2",),
        subject="subject-A",
    )
    assert not a.same_scope(b)


def test_evidence_is_deterministically_deduplicated():
    zero = TypedZero.create(
        ZeroKind.OCCURRENCE,
        domain="event",
        reference="window-A",
        context="audit",
        evidence=("z", "a", "z"),
    )
    assert zero.evidence == ("a", "z")
