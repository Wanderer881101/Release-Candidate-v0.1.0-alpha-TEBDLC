# Jonathan Therrien, Marieville, Québec.

from fractions import Fraction

import pytest

from tebdlc.fractional import ExactFractionalGain
from tebdlc.impotent import ImpotentGainEnvelope


def residual(numerator: int, denominator: int = 361) -> ExactFractionalGain:
    return ExactFractionalGain.create(
        numerator,
        denominator,
        domain="integrity",
        dimension="integrity_fraction",
        unit="ratio",
        reference="integration-basis-361",
        context="impotent-test",
        provenance=("test",),
    )


def test_impotent_mass_can_exceed_one_without_creating_next_unit():
    gains = (residual(300), residual(300))
    envelope = ImpotentGainEnvelope(45, gains, 46, integration_denominator=361)
    assert envelope.arithmetic_mass == Fraction(600, 361)
    assert envelope.arithmetic_mass > 1
    assert not envelope.unitary_attained
    assert envelope.tebdlc_precedence == "45>_TEBDLC46"


def test_impotent_gains_remain_positive_and_preserved_individually():
    gains = (residual(180), residual(180), residual(1))
    envelope = ImpotentGainEnvelope(45, gains, 46, integration_denominator=361)
    assert envelope.all_gains_positive
    assert len(envelope.impotent_gains) == 3
    assert envelope.arithmetic_mass == 1
    assert not envelope.unitary_attained


def test_arithmetic_mass_equal_to_one_is_not_unitary_proof():
    gains = (residual(180), residual(181))
    envelope = ImpotentGainEnvelope(45, gains, 46, integration_denominator=361)
    assert envelope.arithmetic_mass == 1
    assert not envelope.unitary_attained


def test_reference_uses_ample_contextual_denominator_not_fixed_tenths():
    gain = residual(1, 361)
    envelope = ImpotentGainEnvelope(45, (gain,), 46, integration_denominator=361)
    assert gain.denominator == 361
    assert envelope.integration_denominator == 361


def test_incompatible_impotent_gains_cannot_be_grouped_as_one_envelope():
    a = residual(1)
    b = ExactFractionalGain.create(
        1,
        361,
        domain="integrity",
        dimension="other-dimension",
        unit="ratio",
        reference="integration-basis-361",
        context="impotent-test",
        provenance=("test",),
    )
    with pytest.raises(ValueError, match="dimension"):
        ImpotentGainEnvelope(45, (a, b), 46, integration_denominator=361)


def test_candidate_at_or_below_acquired_integer_is_invalid():
    with pytest.raises(ValueError, match="above the acquired integer"):
        ImpotentGainEnvelope(45, (residual(1),), 45, integration_denominator=361)
