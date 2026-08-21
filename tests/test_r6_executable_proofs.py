# Jonathan Therrien, Marieville, Québec.

from fractions import Fraction

import pytest

from tebdlc.fractional import ExactFractionalGain
from tebdlc.impotent import ImpotentGainEnvelope


def fg(n: int, d: int, *, provenance=()):
    return ExactFractionalGain.create(
        n,
        d,
        domain="integrity",
        dimension="coverage",
        unit="ratio",
        reference="R6-proof",
        context="proof-context",
        provenance=provenance,
    )


def test_pf_exhaustive_small_fraction_space_stays_strictly_between_zero_and_one():
    """Executable evidence for PF-1..PF-7 over a finite exhaustive domain."""
    fractions = [Fraction(n, d) for d in range(2, 41) for n in range(1, d)]
    for a in fractions:
        ga = fg(a.numerator, a.denominator)
        assert ga.is_strictly_positive
        assert not ga.is_unit
        for b in fractions:
            gb = fg(b.numerator, b.denominator)
            product = ga * gb
            assert Fraction(0, 1) < product.value < Fraction(1, 1)
            assert product.value < ga.value
            assert product.value < gb.value
            assert not product.is_unit


def test_division_addition_and_subtraction_are_not_gain_primitives():
    a = fg(3, 10)
    b = fg(3, 10)
    with pytest.raises(TypeError):
        _ = a / b
    with pytest.raises(TypeError):
        _ = a + b
    with pytest.raises(TypeError):
        _ = a - b


def test_fractional_gain_cannot_be_constructed_as_zero_or_unit():
    with pytest.raises(ValueError):
        fg(0, 361)
    with pytest.raises(ValueError):
        fg(361, 361)
    with pytest.raises(ValueError):
        fg(362, 361)


def test_context_dimension_unit_reference_and_domain_are_composition_boundaries():
    base = fg(3, 10)
    variants = [
        ExactFractionalGain.create(3, 10, domain="other", dimension="coverage", unit="ratio", reference="R6-proof", context="proof-context"),
        ExactFractionalGain.create(3, 10, domain="integrity", dimension="other", unit="ratio", reference="R6-proof", context="proof-context"),
        ExactFractionalGain.create(3, 10, domain="integrity", dimension="coverage", unit="other", reference="R6-proof", context="proof-context"),
        ExactFractionalGain.create(3, 10, domain="integrity", dimension="coverage", unit="ratio", reference="other", context="proof-context"),
        ExactFractionalGain.create(3, 10, domain="integrity", dimension="coverage", unit="ratio", reference="R6-proof", context="other"),
    ]
    for other in variants:
        assert not base.composable_with(other)
        with pytest.raises(ValueError):
            _ = base * other


def test_provenance_survives_fractional_composition_without_duplication():
    a = fg(3, 10, provenance=("A", "shared"))
    b = fg(2, 5, provenance=("B", "shared"))
    product = a * b
    assert product.typing.provenance == ("A", "B", "shared")
    assert product.value == Fraction(3, 25)


def test_deep_finite_fractional_chain_never_reaches_zero_or_one():
    g = fg(3, 10)
    result = g
    for _ in range(999):
        result = result * g
    assert result.value == Fraction(3**1000, 10**1000)
    assert result.value > 0
    assert result.value < 1
    assert not result.is_unit


def test_impotent_mass_can_exceed_one_without_unit_promotion_600_over_361():
    p1 = fg(300, 361, provenance=("p1",))
    p2 = fg(300, 361, provenance=("p2",))
    envelope = ImpotentGainEnvelope(
        acquired_integer=45,
        impotent_gains=(p1, p2),
        candidate_integer=46,
        integration_denominator=361,
    )
    assert envelope.arithmetic_mass == Fraction(600, 361)
    assert envelope.arithmetic_mass > 1
    assert envelope.all_gains_positive
    assert envelope.unitary_attained is False
    assert envelope.tebdlc_precedence == "45>_TEBDLC46"


def test_impotent_mass_equal_one_still_does_not_create_unit():
    p1 = fg(180, 361)
    p2 = fg(181, 361)
    envelope = ImpotentGainEnvelope(45, (p1, p2), 46, 361)
    assert envelope.arithmetic_mass == 1
    assert envelope.unitary_attained is False


def test_impotent_mass_below_one_still_preserves_positive_constituents():
    p1 = fg(1, 361)
    p2 = fg(1, 361)
    envelope = ImpotentGainEnvelope(45, (p1, p2), 46, 361)
    assert Fraction(0, 1) < envelope.arithmetic_mass < 1
    assert envelope.all_gains_positive
    assert envelope.unitary_attained is False


def test_impotent_envelope_rejects_cross_context_consolidation():
    a = fg(300, 361)
    b = ExactFractionalGain.create(
        300,
        361,
        domain="integrity",
        dimension="coverage",
        unit="ratio",
        reference="R6-proof",
        context="different-context",
    )
    with pytest.raises(ValueError):
        ImpotentGainEnvelope(45, (a, b), 46, 361)
