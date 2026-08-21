# Jonathan Therrien, Marieville, Québec.

from fractions import Fraction

import pytest

from tebdlc.fractional import ExactFractionalGain


def make(
    value_num: int,
    value_den: int,
    *,
    context: str = "session",
    dimension: str = "integrity_fraction",
    unit: str = "ratio",
) -> ExactFractionalGain:
    return ExactFractionalGain.create(
        value_num,
        value_den,
        domain="integrity",
        dimension=dimension,
        unit=unit,
        reference="baseline-A",
        context=context,
        provenance=("test",),
    )


def test_fraction_is_exact_and_strictly_between_zero_and_one():
    gain = make(3, 10)
    assert gain.value == Fraction(3, 10)
    assert gain.is_strictly_positive
    assert not gain.is_unit


def test_repeated_multiplication_remains_positive_and_below_one():
    gain = make(3, 10)
    result = gain
    for _ in range(100):
        result = result * gain
        assert Fraction(0, 1) < result.value < Fraction(1, 1)


def test_no_underflow_to_zero_after_deep_exact_composition():
    gain = make(3, 10)
    result = gain
    for _ in range(1000):
        result = result * gain
    assert result.value > 0
    assert result.numerator > 0
    assert result.value != 0


def test_fraction_close_to_one_is_not_promoted_to_unit():
    gain = make(10**40 - 1, 10**40)
    assert gain.value < 1
    assert gain.value != 1
    assert not gain.is_unit


def test_division_is_explicitly_forbidden():
    gain = make(3, 10)
    with pytest.raises(TypeError, match="division"):
        _ = gain / gain


def test_subtraction_is_explicitly_forbidden():
    a = make(3, 10)
    b = make(1, 10)
    with pytest.raises(TypeError, match="subtraction"):
        _ = a - b


def test_addition_is_not_yet_a_fractional_gain_primitive():
    a = make(3, 10)
    b = make(1, 10)
    with pytest.raises(TypeError, match="addition"):
        _ = a + b


def test_raw_mathematics_demonstrates_why_division_is_forbidden():
    assert Fraction(3, 10) / Fraction(3, 10) == 1
    assert Fraction(3, 10) / Fraction(1, 10) == 3


def test_incompatible_contexts_cannot_be_multiplied():
    a = make(3, 10, context="session-A")
    b = make(3, 10, context="session-B")
    assert not a.composable_with(b)
    with pytest.raises(ValueError, match="not composition-compatible"):
        _ = a * b


def test_incompatible_dimensions_cannot_be_multiplied():
    a = make(3, 10, dimension="integrity_fraction")
    b = make(3, 10, dimension="coverage_fraction")
    assert not a.composable_with(b)
    with pytest.raises(ValueError, match="not composition-compatible"):
        _ = a * b


def test_incompatible_units_cannot_be_multiplied():
    a = make(3, 10, unit="ratio")
    b = make(3, 10, unit="normalized_score")
    assert not a.composable_with(b)


def test_multiplication_preserves_and_unions_provenance():
    a = ExactFractionalGain.create(
        3,
        10,
        domain="integrity",
        dimension="integrity_fraction",
        unit="ratio",
        reference="baseline-A",
        context="session",
        provenance=("source-A",),
    )
    b = ExactFractionalGain.create(
        2,
        5,
        domain="integrity",
        dimension="integrity_fraction",
        unit="ratio",
        reference="baseline-A",
        context="session",
        provenance=("source-B",),
    )
    result = a * b
    assert result.value == Fraction(3, 25)
    assert result.typing.provenance == ("source-A", "source-B")


def test_zero_and_one_are_not_fractional_gain_values():
    with pytest.raises(ValueError):
        make(0, 10)
    with pytest.raises(ValueError):
        make(10, 10)
