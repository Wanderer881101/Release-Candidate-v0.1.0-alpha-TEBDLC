# Jonathan Therrien, Marieville, Québec.

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Iterable


class ZeroKind(str, Enum):
    EXISTENCE = "ZERO_EXISTENCE"
    QUANTITY = "ZERO_QUANTITY"
    VARIATION = "ZERO_VARIATION"
    COVERAGE = "ZERO_COVERAGE"
    EXPRESSION = "ZERO_EXPRESSION"
    ACTIVATION = "ZERO_ACTIVATION"
    ADMISSIBILITY = "ZERO_ADMISSIBILITY"
    DEBT = "ZERO_DEBT"
    CONFLICT = "ZERO_CONFLICT"
    CHIMERA_CONSOLIDATION = "ZERO_CHIMERA_CONSOLIDATION"
    RESULT = "ZERO_RESULT"
    RESIDUAL = "ZERO_RESIDUAL"
    PROLIFERATION_OBSERVED = "ZERO_PROLIFERATION_OBSERVED"
    OCCURRENCE = "ZERO_OCCURRENCE"


@dataclass(frozen=True)
class TypedZero:
    """Experimental closed, typed zero for TEBDLC.

    A zero is invalid unless its semantic kind, scope and evidence are explicit.
    It never propagates automatically to another ZeroKind.
    """

    kind: ZeroKind
    domain: str
    reference: str
    context: str
    evidence: tuple[str, ...]
    subject: str | None = None

    def __post_init__(self) -> None:
        if not isinstance(self.kind, ZeroKind):
            raise TypeError("kind must be a ZeroKind")
        for field_name, value in (
            ("domain", self.domain),
            ("reference", self.reference),
            ("context", self.context),
        ):
            if not value.strip():
                raise ValueError(f"{field_name} must be non-empty")
        if not self.evidence:
            raise ValueError("typed zero requires at least one evidence reference")
        if any(not item.strip() for item in self.evidence):
            raise ValueError("evidence references must be non-empty")

    @classmethod
    def create(
        cls,
        kind: ZeroKind,
        *,
        domain: str,
        reference: str,
        context: str,
        evidence: Iterable[str],
        subject: str | None = None,
    ) -> "TypedZero":
        return cls(
            kind=kind,
            domain=domain,
            reference=reference,
            context=context,
            evidence=tuple(sorted(set(evidence))),
            subject=subject,
        )

    def same_scope(self, other: "TypedZero") -> bool:
        return (
            self.domain == other.domain
            and self.reference == other.reference
            and self.context == other.context
            and self.subject == other.subject
        )

    def implies(self, other_kind: ZeroKind) -> bool:
        """No cross-kind implication is allowed without an explicit future rule."""
        return self.kind is other_kind

    def canonical(self) -> dict[str, object]:
        return {
            "kind": self.kind.value,
            "domain": self.domain,
            "reference": self.reference,
            "context": self.context,
            "subject": self.subject,
            "evidence": list(self.evidence),
        }
