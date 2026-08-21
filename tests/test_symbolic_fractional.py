# Jonathan Therrien, Marieville, Québec.

from fractions import Fraction

import pytest

from tebdlc.fractional import ExactFractionalGain
from tebdlc.symbolic_fractional import SymbolicFractionalGain


def base(*, dimension: str = "integrity_fraction", unit: str = "ratio") -> SymbolicFractionalGain:
    exact = ExactFractionalGain.create(
        3,
        10,
        domain="integrity",
        dimension=dimension,
        unit=unit,
        reference="baseline-A",
        context="session",
        provenance=("source-A",),
    )
    return SymbolicFractionalGain.from_exact(exact)


def test_symbolic_power_preserves_strict_positivity_without_expansion():
    symbolic = base().pow(1_000_000)
    assert symbolic.is_strictly_positive
    assert not symbolic.is_unit
    assert len(symbolic.factors) == 1
    assert symbolic.factors[0].exponent == 1_000_000


def test_symbolic_normalization_merges_equal_factors():
    symbolic = base() * base()
    assert len(symbolic.factors) == 1
    assert symbolic.factors[0].numerator == 3
    assert symbolic.factors[0].denominator == 10
    assert symbolic.factors[0].exponent == 2


def test_symbolic_and_exact_agree_at_reasonable_depth():
    symbolic = base().pow(25)
    assert symbolic.evaluate_exact() == Fraction(3, 10) ** 25


def test_symbolic_division_subtraction_and_addition_are_not_primitives():
    symbolic = base()
    with pytest.raises(TypeError, match="division"):
        _ = symbolic / symbolic
    with pytest.raises(TypeError, match="subtraction"):
        _ = symbolic - symbolic
    with pytest.raises(TypeError, match="addition"):
        _ = symbolic + symbolic


def test_zero_exponent_is_not_allowed_because_it_would_fabricate_unit():
    with pytest.raises(ValueError, match="positive integer"):
        _ = base().pow(0)


def test_symbolic_dimension_mismatch_blocks_composition():
    a = base(dimension="integrity_fraction")
    b = base(dimension="coverage_fraction")
    assert not a.composable_with(b)
    with pytest.raises(ValueError, match="not composition-compatible"):
        _ = a * b


def test_symbolic_unit_mismatch_blocks_composition():
    a = base(unit="ratio")
    b = base(unit="normalized_score")
    assert not a.composable_with(b)
