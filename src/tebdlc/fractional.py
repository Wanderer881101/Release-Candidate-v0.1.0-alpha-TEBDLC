# Jonathan Therrien, Marieville, Québec.

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from typing import Iterable


@dataclass(frozen=True)
class FractionContext:
    """Typed context required to interpret an exact fractional quantity."""

    domain: str
    dimension: str
    unit: str
    reference: str
    context: str
    provenance: tuple[str, ...] = ()

    def __post_init__(self) -> None:
        for field_name, value in (
            ("domain", self.domain),
            ("dimension", self.dimension),
            ("unit", self.unit),
            ("reference", self.reference),
            ("context", self.context),
        ):
            if not value.strip():
                raise ValueError(f"{field_name} must be non-empty")


@dataclass(frozen=True)
class ExactFractionalGain:
    """Experimental exact positive fraction for TEBDLC gain arithmetic.

    This object deliberately exposes multiplication but not subtraction or
    division. A numerator/denominator pair is a representation of an exact
    rational quantity; it does not authorize division between gain objects.
    """

    value: Fraction
    typing: FractionContext

    def __post_init__(self) -> None:
        if not isinstance(self.value, Fraction):
            raise TypeError("value must be fractions.Fraction")
        if not (Fraction(0, 1) < self.value < Fraction(1, 1)):
            raise ValueError("fractional gain must satisfy 0 < value < 1")

    @classmethod
    def create(
        cls,
        numerator: int,
        denominator: int,
        *,
        domain: str,
        dimension: str,
        unit: str,
        reference: str,
        context: str,
        provenance: Iterable[str] = (),
    ) -> "ExactFractionalGain":
        if denominator == 0:
            raise ValueError("denominator cannot be zero")
        return cls(
            Fraction(numerator, denominator),
            FractionContext(
                domain=domain,
                dimension=dimension,
                unit=unit,
                reference=reference,
                context=context,
                provenance=tuple(sorted(set(provenance))),
            ),
        )

    @property
    def numerator(self) -> int:
        return self.value.numerator

    @property
    def denominator(self) -> int:
        return self.value.denominator

    @property
    def is_strictly_positive(self) -> bool:
        return self.value > 0

    @property
    def is_unit(self) -> bool:
        return self.value == 1

    def composable_with(self, other: "ExactFractionalGain") -> bool:
        return (
            self.typing.domain == other.typing.domain
            and self.typing.dimension == other.typing.dimension
            and self.typing.unit == other.typing.unit
            and self.typing.reference == other.typing.reference
            and self.typing.context == other.typing.context
        )

    def multiply(self, other: "ExactFractionalGain") -> "ExactFractionalGain":
        if not self.composable_with(other):
            raise ValueError("fractional gains are not composition-compatible")
        combined_provenance = tuple(
            sorted(set(self.typing.provenance + other.typing.provenance))
        )
        result = self.value * other.value
        return ExactFractionalGain(
            result,
            FractionContext(
                domain=self.typing.domain,
                dimension=self.typing.dimension,
                unit=self.typing.unit,
                reference=self.typing.reference,
                context=self.typing.context,
                provenance=combined_provenance,
            ),
        )

    def __mul__(self, other: object) -> "ExactFractionalGain":
        if not isinstance(other, ExactFractionalGain):
            return NotImplemented
        return self.multiply(other)

    def __add__(self, other: object) -> "ExactFractionalGain":
        raise TypeError("addition is not yet a TEBDLC fractional gain primitive")

    def __sub__(self, other: object) -> "ExactFractionalGain":
        raise TypeError("subtraction is not a TEBDLC fractional gain primitive")

    def __truediv__(self, other: object) -> "ExactFractionalGain":
        raise TypeError("division is not a TEBDLC fractional gain primitive")

    def canonical(self) -> dict[str, object]:
        return {
            "numerator": self.numerator,
            "denominator": self.denominator,
            "domain": self.typing.domain,
            "dimension": self.typing.dimension,
            "unit": self.typing.unit,
            "reference": self.typing.reference,
            "context": self.typing.context,
            "provenance": list(self.typing.provenance),
        }
