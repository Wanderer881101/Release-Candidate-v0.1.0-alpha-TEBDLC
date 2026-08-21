# Jonathan Therrien, Marieville, Québec.

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction

from .fractional import ExactFractionalGain, FractionContext


@dataclass(frozen=True, order=True)
class FractionFactor:
    numerator: int
    denominator: int
    exponent: int = 1

    def __post_init__(self) -> None:
        fraction = Fraction(self.numerator, self.denominator)
        if not (Fraction(0, 1) < fraction < Fraction(1, 1)):
            raise ValueError("symbolic factor must satisfy 0 < factor < 1")
        if self.exponent < 1:
            raise ValueError("exponent must be a positive integer")
        object.__setattr__(self, "numerator", fraction.numerator)
        object.__setattr__(self, "denominator", fraction.denominator)


@dataclass(frozen=True)
class SymbolicFractionalGain:
    """Exact symbolic product of strict positive fractions.

    It stores factors and exponents instead of eagerly expanding huge integer
    numerators/denominators. Addition, division and subtraction are not exposed
    as TEBDLC primitives.
    """

    factors: tuple[FractionFactor, ...]
    typing: FractionContext

    def __post_init__(self) -> None:
        if not self.factors:
            raise ValueError("at least one strict fractional factor is required")
        normalized = self._normalize(self.factors)
        object.__setattr__(self, "factors", normalized)

    @staticmethod
    def _normalize(factors: tuple[FractionFactor, ...]) -> tuple[FractionFactor, ...]:
        exponents: dict[tuple[int, int], int] = {}
        for factor in factors:
            key = (factor.numerator, factor.denominator)
            exponents[key] = exponents.get(key, 0) + factor.exponent
        return tuple(
            FractionFactor(num, den, exponent)
            for (num, den), exponent in sorted(exponents.items())
        )

    @classmethod
    def from_exact(cls, gain: ExactFractionalGain) -> "SymbolicFractionalGain":
        return cls(
            factors=(FractionFactor(gain.numerator, gain.denominator),),
            typing=gain.typing,
        )

    @property
    def is_strictly_positive(self) -> bool:
        return True

    @property
    def is_unit(self) -> bool:
        return False

    def composable_with(self, other: "SymbolicFractionalGain") -> bool:
        return (
            self.typing.domain == other.typing.domain
            and self.typing.dimension == other.typing.dimension
            and self.typing.unit == other.typing.unit
            and self.typing.reference == other.typing.reference
            and self.typing.context == other.typing.context
        )

    def multiply(self, other: "SymbolicFractionalGain") -> "SymbolicFractionalGain":
        if not self.composable_with(other):
            raise ValueError("symbolic fractional gains are not composition-compatible")
        provenance = tuple(sorted(set(self.typing.provenance + other.typing.provenance)))
        return SymbolicFractionalGain(
            factors=self.factors + other.factors,
            typing=FractionContext(
                domain=self.typing.domain,
                dimension=self.typing.dimension,
                unit=self.typing.unit,
                reference=self.typing.reference,
                context=self.typing.context,
                provenance=provenance,
            ),
        )

    def pow(self, exponent: int) -> "SymbolicFractionalGain":
        if exponent < 1:
            raise ValueError("exponent must be a positive integer")
        return SymbolicFractionalGain(
            factors=tuple(
                FractionFactor(f.numerator, f.denominator, f.exponent * exponent)
                for f in self.factors
            ),
            typing=self.typing,
        )

    def __mul__(self, other: object) -> "SymbolicFractionalGain":
        if not isinstance(other, SymbolicFractionalGain):
            return NotImplemented
        return self.multiply(other)

    def __add__(self, other: object) -> "SymbolicFractionalGain":
        raise TypeError("addition is not yet a TEBDLC symbolic gain primitive")

    def __sub__(self, other: object) -> "SymbolicFractionalGain":
        raise TypeError("subtraction is not yet a TEBDLC symbolic gain primitive")

    def __truediv__(self, other: object) -> "SymbolicFractionalGain":
        raise TypeError("division is not a TEBDLC symbolic gain primitive")

    def evaluate_exact(self) -> Fraction:
        result = Fraction(1, 1)
        for factor in self.factors:
            result *= Fraction(factor.numerator, factor.denominator) ** factor.exponent
        return result

    def canonical(self) -> dict[str, object]:
        return {
            "factors": [
                {
                    "numerator": f.numerator,
                    "denominator": f.denominator,
                    "exponent": f.exponent,
                }
                for f in self.factors
            ],
            "domain": self.typing.domain,
            "dimension": self.typing.dimension,
            "unit": self.typing.unit,
            "reference": self.typing.reference,
            "context": self.typing.context,
            "provenance": list(self.typing.provenance),
        }
