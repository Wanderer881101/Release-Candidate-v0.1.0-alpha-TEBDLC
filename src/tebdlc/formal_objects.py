# Jonathan Therrien, Marieville, Québec.

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Iterable

from .core import stable_id
from .zero import TypedZero, ZeroKind


@dataclass(frozen=True)
class ProofRef:
    ref: str
    kind: str
    provenance: str

    def __post_init__(self) -> None:
        if not self.ref.strip():
            raise ValueError("proof ref must be non-empty")
        if not self.kind.strip():
            raise ValueError("proof kind must be non-empty")
        if not self.provenance.strip():
            raise ValueError("proof provenance must be non-empty")

    def canonical(self) -> dict[str, str]:
        return {
            "ref": self.ref,
            "kind": self.kind,
            "provenance": self.provenance,
        }


class RelationKind(str, Enum):
    SAME_ENTITY = "SAME_ENTITY"
    DISTINCT_ENTITY = "DISTINCT_ENTITY"
    DEPENDS_ON = "DEPENDS_ON"
    DERIVED_FROM = "DERIVED_FROM"
    VARIANT_OF = "VARIANT_OF"
    CONFLICTS_WITH = "CONFLICTS_WITH"
    COMPATIBLE_WITH = "COMPATIBLE_WITH"
    SAME_CONTEXT = "SAME_CONTEXT"
    DISTINCT_CONTEXT = "DISTINCT_CONTEXT"
    OCCURS_BEFORE = "OCCURS_BEFORE"
    OCCURS_AFTER = "OCCURS_AFTER"
    PROLIFERATES_TO = "PROLIFERATES_TO"
    REFUNDS = "REFUNDS"


@dataclass(frozen=True)
class GainRelation:
    relation_id: str
    kind: RelationKind
    left_gain_id: str
    right_gain_id: str
    evidence: tuple[ProofRef, ...]
    context: str

    @classmethod
    def create(
        cls,
        kind: RelationKind,
        *,
        left_gain_id: str,
        right_gain_id: str,
        evidence: Iterable[ProofRef],
        context: str,
    ) -> "GainRelation":
        records = tuple(sorted(evidence, key=lambda item: (item.ref, item.kind, item.provenance)))
        if not records:
            raise ValueError("relation requires evidence")
        if not left_gain_id.strip() or not right_gain_id.strip():
            raise ValueError("relation gain ids must be non-empty")
        if not context.strip():
            raise ValueError("relation context must be non-empty")
        identity = {
            "kind": kind.value,
            "left_gain_id": left_gain_id,
            "right_gain_id": right_gain_id,
            "evidence": [item.canonical() for item in records],
            "context": context,
        }
        return cls(
            relation_id=stable_id("rel", identity),
            kind=kind,
            left_gain_id=left_gain_id,
            right_gain_id=right_gain_id,
            evidence=records,
            context=context,
        )

    def canonical(self) -> dict[str, object]:
        return {
            "relation_id": self.relation_id,
            "kind": self.kind.value,
            "left_gain_id": self.left_gain_id,
            "right_gain_id": self.right_gain_id,
            "evidence": [item.canonical() for item in self.evidence],
            "context": self.context,
        }


class ConsolidationStatus(str, Enum):
    COHERENT = "COHERENT"
    CHIMERA = "CHIMERA"
    UNKNOWN = "UNKNOWN"


@dataclass(frozen=True)
class ConsolidationResult:
    result_id: str
    constituent_gain_ids: tuple[str, ...]
    hypothesis: str
    status: ConsolidationStatus
    evidence: tuple[ProofRef, ...]
    zero: TypedZero | None = None

    @classmethod
    def create(
        cls,
        *,
        constituent_gain_ids: Iterable[str],
        hypothesis: str,
        status: ConsolidationStatus,
        evidence: Iterable[ProofRef],
        zero: TypedZero | None = None,
    ) -> "ConsolidationResult":
        constituents = tuple(sorted(set(constituent_gain_ids)))
        proofs = tuple(sorted(evidence, key=lambda item: (item.ref, item.kind, item.provenance)))
        if len(constituents) < 2:
            raise ValueError("consolidation requires at least two constituent gains")
        if not hypothesis.strip():
            raise ValueError("consolidation hypothesis must be non-empty")
        if not proofs:
            raise ValueError("consolidation result requires evidence")
        if status is ConsolidationStatus.CHIMERA:
            if zero is None or zero.kind is not ZeroKind.CHIMERA_CONSOLIDATION:
                raise ValueError("chimera consolidation requires ZERO_CHIMERA_CONSOLIDATION")
        elif zero is not None:
            raise ValueError("only a CHIMERA result may carry a chimera zero")
        identity = {
            "constituent_gain_ids": constituents,
            "hypothesis": hypothesis,
            "status": status.value,
            "evidence": [item.canonical() for item in proofs],
            "zero": None if zero is None else zero.canonical(),
        }
        return cls(
            result_id=stable_id("result", identity),
            constituent_gain_ids=constituents,
            hypothesis=hypothesis,
            status=status,
            evidence=proofs,
            zero=zero,
        )

    @property
    def preserves_constituents(self) -> bool:
        return bool(self.constituent_gain_ids)

    def canonical(self) -> dict[str, object]:
        return {
            "result_id": self.result_id,
            "constituent_gain_ids": list(self.constituent_gain_ids),
            "hypothesis": self.hypothesis,
            "status": self.status.value,
            "evidence": [item.canonical() for item in self.evidence],
            "zero": None if self.zero is None else self.zero.canonical(),
        }
