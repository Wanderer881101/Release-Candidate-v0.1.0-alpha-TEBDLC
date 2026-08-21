# Jonathan Therrien, Marieville, Québec.

from fractions import Fraction

import pytest

from tebdlc.multidimensional import DimensionalEffect, NegativePositiveGainProfile


def test_negative_positive_profile_preserves_each_dimension_exactly():
    performance = DimensionalEffect.create(
        dimension="performance",
        numerator=2,
        unit="points",
        reference="baseline-A",
        context="scenario-A",
        provenance=("measurement:perf",),
    )
    integrity = DimensionalEffect.create(
        dimension="integrity",
        numerator=-8,
        unit="points",
        reference="baseline-A",
        context="scenario-A",
        provenance=("measurement:integrity",),
    )
    profile = NegativePositiveGainProfile((integrity, performance))
    assert profile.positive_effects[0].value == Fraction(2, 1)
    assert profile.negative_effects[0].value == Fraction(-8, 1)
    assert {effect.dimension for effect in profile.effects} == {"performance", "integrity"}
    assert not hasattr(profile, "total")


def test_profile_rejects_single_sign_only():
    a = DimensionalEffect.create(
        dimension="performance",
        numerator=2,
        unit="points",
        reference="baseline-A",
        context="scenario-A",
    )
    b = DimensionalEffect.create(
        dimension="coverage",
        numerator=8,
        unit="points",
        reference="baseline-A",
        context="scenario-A",
    )
    with pytest.raises(ValueError, match="negative effect"):
        NegativePositiveGainProfile((a, b))


def test_profile_rejects_duplicate_dimension_to_avoid_silent_collapse():
    a = DimensionalEffect.create(
        dimension="performance",
        numerator=2,
        unit="points",
        reference="baseline-A",
        context="scenario-A",
    )
    b = DimensionalEffect.create(
        dimension="performance",
        numerator=-1,
        unit="points",
        reference="baseline-A",
        context="scenario-A",
    )
    with pytest.raises(ValueError, match="at most once"):
        NegativePositiveGainProfile((a, b))
