# Jonathan Therrien, Marieville, Québec.

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction

from .fractional import ExactFractionalGain


@dataclass(frozen=True)
class ImpotentGainEnvelope:
    """Experimental TEBDLC model of gains that remain non-unitizable by themselves.

    Impotence is NOT defined by ``sum(fractions) < 1``. A collection of valid
    impotent gains may carry an arithmetic mass greater than one while still
    failing to constitute the next unit because the required integration is
    incomplete or incoherent.

    ``acquired_integer`` is the last completely integrated unitary state.
    ``candidate_integer`` is the next unit whose existence is NOT granted by
    the mere arithmetic mass of ``impotent_gains``.

    The notation ``45 >_TEBDLC 46`` is therefore a semantic precedence
    relation: the demonstrated state 45 has authority over an unintegrated
    candidate 46. It is not the ordinary numeric proposition 45 > 46.

    Impotent gains are preserved individually. They may later participate in
    an explicitly proven, associably coherent alternative consolidation with
    other gains. No such general addition/consolidation operator is introduced
    here.
    """

    acquired_integer: int
    impotent_gains: tuple[ExactFractionalGain, ...]
    candidate_integer: int
    integration_denominator: int

    def __post_init__(self) -> None:
        if self.candidate_integer <= self.acquired_integer:
            raise ValueError("candidate integer must be above the acquired integer")
        if not self.impotent_gains:
            raise ValueError("at least one impotent gain is required")
        if self.integration_denominator <= 1:
            raise ValueError("integration denominator must be an ample positive basis")

        first = self.impotent_gains[0]
        for gain in self.impotent_gains:
            if gain.typing.domain != first.typing.domain:
                raise ValueError("impotent gains must share a domain")
            if gain.typing.dimension != first.typing.dimension:
                raise ValueError("impotent gains must share a dimension")
            if gain.typing.unit != first.typing.unit:
                raise ValueError("impotent gains must share a unit")
            if gain.typing.reference != first.typing.reference:
                raise ValueError("impotent gains must share a reference")
            if gain.typing.context != first.typing.context:
                raise ValueError("impotent gains must share a context")

    @property
    def arithmetic_mass(self) -> Fraction:
        """Non-authoritative arithmetic sum used only to inspect magnitude.

        This value MUST NOT be interpreted as a unit count and cannot promote
        the candidate integer. It is intentionally separated from unitary
        integration semantics.
        """

        return sum((gain.value for gain in self.impotent_gains), Fraction(0, 1))

    @property
    def unitary_attained(self) -> bool:
        """Impotent-only consolidation never self-promotes to a unit."""

        return False

    @property
    def tebdlc_precedence(self) -> str:
        return f"{self.acquired_integer}>_TEBDLC{self.candidate_integer}"

    @property
    def all_gains_positive(self) -> bool:
        return all(gain.value > 0 for gain in self.impotent_gains)

    def canonical(self) -> dict[str, object]:
        return {
            "acquired_integer": self.acquired_integer,
            "candidate_integer": self.candidate_integer,
            "integration_denominator": self.integration_denominator,
            "impotent_gains": [gain.canonical() for gain in self.impotent_gains],
            "arithmetic_mass": {
                "numerator": self.arithmetic_mass.numerator,
                "denominator": self.arithmetic_mass.denominator,
                "authoritative_for_unitarity": False,
            },
            "unitary_attained": self.unitary_attained,
            "tebdlc_precedence": self.tebdlc_precedence,
        }
