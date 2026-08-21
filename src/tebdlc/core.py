# Jonathan Therrien, Marieville, Québec.

from __future__ import annotations

from dataclasses import dataclass, field, replace
from enum import Enum
import hashlib
import json
from typing import Any, Iterable, Mapping


class GainStatus(str, Enum):
    EMERGENT = "EMERGENT_GAIN"
    VALIDATED = "VALIDATED_GAIN"
    ASSIMILATED = "ASSIMILATED_GAIN"
    UNKNOWN = "UNKNOWN_GAIN"
    REJECTED = "REJECTED_GAIN"


class AnomalyStatus(str, Enum):
    OPEN = "OPEN"
    RESOLVED = "RESOLVED"
    UNKNOWN = "UNKNOWN"
    BLOCKED = "BLOCKED"


class ReconciliationStatus(str, Enum):
    AGREED = "AGREED"
    ONLY_SOURCE_A = "ONLY_SOURCE_A"
    ONLY_SOURCE_B = "ONLY_SOURCE_B"
    CONFLICT = "CONFLICT"
    UNKNOWN = "UNKNOWN"


def canonical_json(value: Any) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def stable_id(prefix: str, value: Any) -> str:
    digest = hashlib.sha256(canonical_json(value).encode("utf-8")).hexdigest()
    return f"{prefix}_{digest[:24]}"


@dataclass(frozen=True)
class SourceRef:
    source_id: str
    kind: str
    locator: str
    metadata: Mapping[str, Any] = field(default_factory=dict)

    def canonical(self) -> dict[str, Any]:
        return {
            "source_id": self.source_id,
            "kind": self.kind,
            "locator": self.locator,
            "metadata": dict(self.metadata),
        }


@dataclass(frozen=True)
class EvidenceRecord:
    ref: str
    kind: str = "evidence"
    metadata: Mapping[str, Any] = field(default_factory=dict)

    def canonical(self) -> dict[str, Any]:
        return {"ref": self.ref, "kind": self.kind, "metadata": dict(self.metadata)}


@dataclass(frozen=True)
class GainRecord:
    gain_id: str
    title: str
    description: str
    status: GainStatus = GainStatus.EMERGENT
    sources: tuple[SourceRef, ...] = ()
    domains: tuple[str, ...] = ()
    dependencies: tuple[str, ...] = ()
    conflicts: tuple[str, ...] = ()
    evidence: tuple[EvidenceRecord, ...] = ()
    revision: int = 0
    parent_revision_id: str | None = None
    supersedes: tuple[str, ...] = ()
    semantic_claims: tuple[str, ...] = ()
    metadata: Mapping[str, Any] = field(default_factory=dict)

    @classmethod
    def create(
        cls,
        *,
        title: str,
        description: str,
        sources: Iterable[SourceRef] = (),
        domains: Iterable[str] = (),
        dependencies: Iterable[str] = (),
        conflicts: Iterable[str] = (),
        semantic_claims: Iterable[str] = (),
        metadata: Mapping[str, Any] | None = None,
        status: GainStatus = GainStatus.EMERGENT,
    ) -> "GainRecord":
        normalized_sources = tuple(sorted(sources, key=lambda item: item.source_id))
        identity = {
            "title": title.strip(),
            "description": description.strip(),
            "sources": [item.canonical() for item in normalized_sources],
            "domains": sorted(set(domains)),
        }
        return cls(
            gain_id=stable_id("gain", identity),
            title=identity["title"],
            description=identity["description"],
            status=status,
            sources=normalized_sources,
            domains=tuple(identity["domains"]),
            dependencies=tuple(sorted(set(dependencies))),
            conflicts=tuple(sorted(set(conflicts))),
            semantic_claims=tuple(sorted(set(semantic_claims))),
            metadata=dict(metadata or {}),
        )

    def canonical(self) -> dict[str, Any]:
        return {
            "gain_id": self.gain_id,
            "title": self.title,
            "description": self.description,
            "status": self.status.value,
            "sources": [item.canonical() for item in self.sources],
            "domains": list(self.domains),
            "dependencies": list(self.dependencies),
            "conflicts": list(self.conflicts),
            "evidence": [item.canonical() for item in self.evidence],
            "revision": self.revision,
            "parent_revision_id": self.parent_revision_id,
            "supersedes": list(self.supersedes),
            "semantic_claims": list(self.semantic_claims),
            "metadata": dict(self.metadata),
        }

    @property
    def revision_id(self) -> str:
        return stable_id("rev", self.canonical())


@dataclass(frozen=True)
class AnomalyRecord:
    anomaly_id: str
    context: str
    symptom: str
    impact: str
    status: AnomalyStatus
    action: str
    revision: int = 0
    parent_revision_id: str | None = None
    metadata: Mapping[str, Any] = field(default_factory=dict)

    @classmethod
    def create(
        cls,
        *,
        context: str,
        symptom: str,
        impact: str,
        status: AnomalyStatus,
        action: str,
        metadata: Mapping[str, Any] | None = None,
    ) -> "AnomalyRecord":
        identity = {"context": context, "symptom": symptom}
        return cls(
            anomaly_id=stable_id("anom", identity),
            context=context,
            symptom=symptom,
            impact=impact,
            status=status,
            action=action,
            metadata=dict(metadata or {}),
        )

    def canonical(self) -> dict[str, Any]:
        return {
            "anomaly_id": self.anomaly_id,
            "context": self.context,
            "symptom": self.symptom,
            "impact": self.impact,
            "status": self.status.value,
            "action": self.action,
            "revision": self.revision,
            "parent_revision_id": self.parent_revision_id,
            "metadata": dict(self.metadata),
        }

    @property
    def revision_id(self) -> str:
        return stable_id("arev", self.canonical())


@dataclass(frozen=True)
class GainDelta:
    added: tuple[str, ...]
    removed: tuple[str, ...]
    changed: tuple[str, ...]

    @property
    def has_loss(self) -> bool:
        return bool(self.removed)


@dataclass(frozen=True)
class ReconciliationResult:
    status: ReconciliationStatus
    gain_id: str
    left_revision_id: str | None
    right_revision_id: str | None
    reason: str


class TEBDLC:
    """Append-conscious gain ledger with explicit revisions, provenance and anomaly history."""

    SNAPSHOT_FORMAT = "tebdlc.snapshot.v1"

    def __init__(self) -> None:
        self._current: dict[str, GainRecord] = {}
        self._history: dict[str, list[GainRecord]] = {}
        self._anomalies: dict[str, AnomalyRecord] = {}
        self._anomaly_history: dict[str, list[AnomalyRecord]] = {}

    @property
    def gains(self) -> tuple[GainRecord, ...]:
        return tuple(self._current[key] for key in sorted(self._current))

    @property
    def anomalies(self) -> tuple[AnomalyRecord, ...]:
        return tuple(self._anomalies[key] for key in sorted(self._anomalies))

    def add(self, gain: GainRecord) -> GainRecord:
        existing = self._current.get(gain.gain_id)
        if existing is not None:
            if existing.canonical() == gain.canonical():
                return existing
            raise ValueError(f"gain {gain.gain_id} already exists; use revise()")
        self._current[gain.gain_id] = gain
        self._history[gain.gain_id] = [gain]
        return gain

    def get(self, gain_id: str) -> GainRecord:
        if gain_id not in self._current:
            raise KeyError(f"unknown gain: {gain_id}")
        return self._current[gain_id]

    def history(self, gain_id: str) -> tuple[GainRecord, ...]:
        if gain_id not in self._history:
            raise KeyError(f"unknown gain: {gain_id}")
        return tuple(self._history[gain_id])

    def revise(self, gain_id: str, **changes: Any) -> GainRecord:
        current = self.get(gain_id)
        forbidden = {"gain_id", "revision", "parent_revision_id", "status", "evidence"}
        illegal = forbidden.intersection(changes)
        if illegal:
            raise ValueError(f"managed fields cannot be revised directly: {sorted(illegal)}")
        revised = replace(current, **changes, revision=current.revision + 1, parent_revision_id=current.revision_id)
        self._current[gain_id] = revised
        self._history[gain_id].append(revised)
        return revised

    def validate(self, gain_id: str, *, evidence: Iterable[str | EvidenceRecord]) -> GainRecord:
        current = self.get(gain_id)
        if current.status not in {GainStatus.EMERGENT, GainStatus.UNKNOWN}:
            raise ValueError(f"cannot validate from status {current.status.value}")
        records = tuple(item if isinstance(item, EvidenceRecord) else EvidenceRecord(ref=item) for item in evidence)
        if not records:
            raise ValueError("validation requires at least one evidence record")
        updated = replace(
            current,
            status=GainStatus.VALIDATED,
            evidence=current.evidence + records,
            revision=current.revision + 1,
            parent_revision_id=current.revision_id,
        )
        self._current[gain_id] = updated
        self._history[gain_id].append(updated)
        return updated

    def assimilate(self, gain_id: str) -> GainRecord:
        current = self.get(gain_id)
        if current.status is not GainStatus.VALIDATED:
            raise ValueError("only VALIDATED_GAIN can be assimilated")
        unresolved = [ref for ref in current.conflicts if ref in self._current and self._current[ref].status is not GainStatus.REJECTED]
        if unresolved:
            raise ValueError(f"unresolved conflicts block assimilation: {unresolved}")
        updated = replace(current, status=GainStatus.ASSIMILATED, revision=current.revision + 1, parent_revision_id=current.revision_id)
        self._current[gain_id] = updated
        self._history[gain_id].append(updated)
        return updated

    def reject(self, gain_id: str, *, evidence: Iterable[str | EvidenceRecord] = ()) -> GainRecord:
        current = self.get(gain_id)
        if current.status is GainStatus.ASSIMILATED:
            raise ValueError("assimilated gain cannot be silently rejected; supersede it explicitly")
        records = tuple(item if isinstance(item, EvidenceRecord) else EvidenceRecord(ref=item) for item in evidence)
        updated = replace(
            current,
            status=GainStatus.REJECTED,
            evidence=current.evidence + records,
            revision=current.revision + 1,
            parent_revision_id=current.revision_id,
        )
        self._current[gain_id] = updated
        self._history[gain_id].append(updated)
        return updated

    def supersede(self, old_gain_id: str, new_gain: GainRecord, *, evidence: Iterable[str | EvidenceRecord]) -> GainRecord:
        old = self.get(old_gain_id)
        if old.status is not GainStatus.ASSIMILATED:
            raise ValueError("only an ASSIMILATED_GAIN requires explicit supersession")
        candidate = replace(new_gain, supersedes=tuple(sorted(set(new_gain.supersedes + (old_gain_id,)))))
        self.add(candidate)
        return self.validate(candidate.gain_id, evidence=evidence)

    def mark_unknown(self, gain_id: str) -> GainRecord:
        current = self.get(gain_id)
        if current.status is GainStatus.ASSIMILATED:
            raise ValueError("assimilated gain cannot regress silently to UNKNOWN")
        updated = replace(current, status=GainStatus.UNKNOWN, revision=current.revision + 1, parent_revision_id=current.revision_id)
        self._current[gain_id] = updated
        self._history[gain_id].append(updated)
        return updated

    def record_anomaly(self, anomaly: AnomalyRecord) -> AnomalyRecord:
        existing = self._anomalies.get(anomaly.anomaly_id)
        if existing is None:
            self._anomalies[anomaly.anomaly_id] = anomaly
            self._anomaly_history[anomaly.anomaly_id] = [anomaly]
            return anomaly
        if existing.canonical() == anomaly.canonical():
            return existing
        raise ValueError("anomaly already exists; use revise_anomaly()")

    def revise_anomaly(self, anomaly_id: str, **changes: Any) -> AnomalyRecord:
        if anomaly_id not in self._anomalies:
            raise KeyError(f"unknown anomaly: {anomaly_id}")
        current = self._anomalies[anomaly_id]
        forbidden = {"anomaly_id", "revision", "parent_revision_id"}
        illegal = forbidden.intersection(changes)
        if illegal:
            raise ValueError(f"managed fields cannot be revised directly: {sorted(illegal)}")
        revised = replace(current, **changes, revision=current.revision + 1, parent_revision_id=current.revision_id)
        self._anomalies[anomaly_id] = revised
        self._anomaly_history[anomaly_id].append(revised)
        return revised

    def snapshot(self) -> dict[str, Any]:
        return {
            "format": self.SNAPSHOT_FORMAT,
            "gains": [gain.canonical() for gain in self.gains],
            "history": {gain_id: [rev.canonical() for rev in revs] for gain_id, revs in sorted(self._history.items())},
            "anomalies": [anomaly.canonical() for anomaly in self.anomalies],
            "anomaly_history": {aid: [rev.canonical() for rev in revs] for aid, revs in sorted(self._anomaly_history.items())},
        }

    def export_json(self) -> str:
        return canonical_json(self.snapshot())

    def delta(self, previous: "TEBDLC") -> GainDelta:
        before = {gain.gain_id: gain for gain in previous.gains}
        after = {gain.gain_id: gain for gain in self.gains}
        return GainDelta(
            added=tuple(sorted(after.keys() - before.keys())),
            removed=tuple(sorted(before.keys() - after.keys())),
            changed=tuple(sorted(key for key in before.keys() & after.keys() if before[key].canonical() != after[key].canonical())),
        )

    def assert_no_loss_against(self, previous: "TEBDLC") -> None:
        delta = self.delta(previous)
        protected = {gain.gain_id for gain in previous.gains if gain.status in {GainStatus.VALIDATED, GainStatus.ASSIMILATED}}
        lost = protected.intersection(delta.removed)
        if lost:
            raise AssertionError(f"validated/assimilated gains lost: {sorted(lost)}")

    def reconcile(self, other: "TEBDLC") -> tuple[ReconciliationResult, ...]:
        left = {gain.gain_id: gain for gain in self.gains}
        right = {gain.gain_id: gain for gain in other.gains}
        results: list[ReconciliationResult] = []
        for gain_id in sorted(left.keys() | right.keys()):
            a = left.get(gain_id)
            b = right.get(gain_id)
            if a is None:
                results.append(ReconciliationResult(ReconciliationStatus.ONLY_SOURCE_B, gain_id, None, b.revision_id, "gain absent from source A"))
            elif b is None:
                results.append(ReconciliationResult(ReconciliationStatus.ONLY_SOURCE_A, gain_id, a.revision_id, None, "gain absent from source B"))
            elif a.canonical() == b.canonical():
                results.append(ReconciliationResult(ReconciliationStatus.AGREED, gain_id, a.revision_id, b.revision_id, "canonical records match"))
            elif a.revision == b.revision and a.parent_revision_id == b.parent_revision_id:
                results.append(ReconciliationResult(ReconciliationStatus.CONFLICT, gain_id, a.revision_id, b.revision_id, "same lineage position diverged"))
            else:
                results.append(ReconciliationResult(ReconciliationStatus.UNKNOWN, gain_id, a.revision_id, b.revision_id, "different lineage positions require explicit review"))
        return tuple(results)
