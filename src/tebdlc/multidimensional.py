# Jonathan Therrien, Marieville, Québec.

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from typing import Iterable


@dataclass(frozen=True, order=True)
class DimensionalEffect:
    dimension: str
    value: Fraction
    unit: str
    reference: str
    context: str
    provenance: tuple[str, ...] = ()

    def __post_init__(self) -> None:
        for field_name, field_value in (
            ("dimension", self.dimension),
            ("unit", self.unit),
            ("reference", self.reference),
            ("context", self.context),
        ):
            if not field_value.strip():
                raise ValueError(f"{field_name} must be non-empty")
        if not isinstance(self.value, Fraction):
            raise TypeError("value must be fractions.Fraction")

    @classmethod
    def create(
        cls,
        *,
        dimension: str,
        numerator: int,
        denominator: int = 1,
        unit: str,
        reference: str,
        context: str,
        provenance: Iterable[str] = (),
    ) -> "DimensionalEffect":
        if denominator == 0:
            raise ValueError("denominator cannot be zero")
        return cls(
            dimension=dimension,
            value=Fraction(numerator, denominator),
            unit=unit,
            reference=reference,
            context=context,
            provenance=tuple(sorted(set(provenance))),
        )

    def canonical(self) -> dict[str, object]:
        return {
            "dimension": self.dimension,
            "numerator": self.value.numerator,
            "denominator": self.value.denominator,
            "unit": self.unit,
            "reference": self.reference,
            "context": self.context,
            "provenance": list(self.provenance),
        }


@dataclass(frozen=True)
class NegativePositiveGainProfile:
    """Stores positive and negative dimensional effects without collapsing them.

    The profile deliberately exposes no aggregate total. Signed values describe
    measurements on their own dimensions; they are not TEBDLC subtraction
    operators between gains.
    """

    effects: tuple[DimensionalEffect, ...]

    def __post_init__(self) -> None:
        if len(self.effects) < 2:
            raise ValueError("negative-positive profile requires multiple dimensions")
        dimensions = [effect.dimension for effect in self.effects]
        if len(set(dimensions)) != len(dimensions):
            raise ValueError("each dimension must occur at most once in a profile")
        if not any(effect.value > 0 for effect in self.effects):
            raise ValueError("profile requires at least one positive effect")
        if not any(effect.value < 0 for effect in self.effects):
            raise ValueError("profile requires at least one negative effect")
        object.__setattr__(self, "effects", tuple(sorted(self.effects, key=lambda item: item.dimension)))

    @property
    def positive_effects(self) -> tuple[DimensionalEffect, ...]:
        return tuple(effect for effect in self.effects if effect.value > 0)

    @property
    def negative_effects(self) -> tuple[DimensionalEffect, ...]:
        return tuple(effect for effect in self.effects if effect.value < 0)

    def canonical(self) -> dict[str, object]:
        return {"effects": [effect.canonical() for effect in self.effects]}
