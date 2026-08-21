# Jonathan Therrien, Marieville, Québec.

import pytest

from tebdlc import (
    AnomalyRecord,
    AnomalyStatus,
    GainRecord,
    GainStatus,
    ReconciliationStatus,
    SourceRef,
    TEBDLC,
)


def test_same_canonical_gain_has_same_id():
    s1 = SourceRef("s1", "conversation", "turn:1")
    s2 = SourceRef("s2", "repository", "repo:path")
    a = GainRecord.create(title="A", description="B", sources=(s2, s1), domains=("d",))
    b = GainRecord.create(title="A", description="B", sources=(s1, s2), domains=("d",))
    assert a.gain_id == b.gain_id


def test_duplicate_identical_add_is_idempotent():
    ledger = TEBDLC()
    gain = GainRecord.create(title="A", description="B")
    assert ledger.add(gain) == gain
    assert ledger.add(gain) == gain
    assert len(ledger.gains) == 1


def test_revision_preserves_history_and_parent():
    ledger = TEBDLC()
    gain = ledger.add(GainRecord.create(title="A", description="B"))
    revised = ledger.revise(gain.gain_id, description="B2")
    assert len(ledger.history(gain.gain_id)) == 2
    assert revised.parent_revision_id == gain.revision_id
    assert revised.revision == 1


def test_validation_requires_evidence():
    ledger = TEBDLC()
    gain = ledger.add(GainRecord.create(title="A", description="B"))
    with pytest.raises(ValueError):
        ledger.validate(gain.gain_id, evidence=())


def test_emergent_to_validated_to_assimilated():
    ledger = TEBDLC()
    gain = ledger.add(GainRecord.create(title="A", description="B"))
    validated = ledger.validate(gain.gain_id, evidence=("test:proof",))
    assert validated.status is GainStatus.VALIDATED
    assimilated = ledger.assimilate(gain.gain_id)
    assert assimilated.status is GainStatus.ASSIMILATED
    assert len(ledger.history(gain.gain_id)) == 3


def test_assimilated_gain_cannot_be_silently_rejected_or_unknown():
    ledger = TEBDLC()
    gain = ledger.add(GainRecord.create(title="A", description="B"))
    ledger.validate(gain.gain_id, evidence=("proof",))
    ledger.assimilate(gain.gain_id)
    with pytest.raises(ValueError):
        ledger.reject(gain.gain_id)
    with pytest.raises(ValueError):
        ledger.mark_unknown(gain.gain_id)


def test_assimilation_blocked_by_unresolved_conflict():
    ledger = TEBDLC()
    b = GainRecord.create(title="B", description="B")
    a0 = GainRecord.create(title="A", description="A")
    a = GainRecord(
        gain_id=a0.gain_id,
        title=a0.title,
        description=a0.description,
        conflicts=(b.gain_id,),
    )
    ledger.add(a)
    ledger.add(b)
    ledger.validate(a.gain_id, evidence=("proof",))
    with pytest.raises(ValueError):
        ledger.assimilate(a.gain_id)
    ledger.reject(b.gain_id, evidence=("resolution",))
    assert ledger.assimilate(a.gain_id).status is GainStatus.ASSIMILATED


def test_supersession_preserves_old_assimilated_gain():
    ledger = TEBDLC()
    old = ledger.add(GainRecord.create(title="Old", description="old"))
    ledger.validate(old.gain_id, evidence=("proof-old",))
    ledger.assimilate(old.gain_id)
    new = GainRecord.create(title="New", description="new")
    validated_new = ledger.supersede(old.gain_id, new, evidence=("proof-new",))
    assert old.gain_id in validated_new.supersedes
    assert ledger.get(old.gain_id).status is GainStatus.ASSIMILATED
    assert validated_new.status is GainStatus.VALIDATED


def test_anomaly_revision_is_traced():
    ledger = TEBDLC()
    anomaly = ledger.record_anomaly(
        AnomalyRecord.create(
            context="ci",
            symptom="blocked",
            impact="validation paused",
            status=AnomalyStatus.BLOCKED,
            action="retry",
        )
    )
    resolved = ledger.revise_anomaly(anomaly.anomaly_id, status=AnomalyStatus.RESOLVED, action="retry passed")
    assert resolved.revision == 1
    assert resolved.parent_revision_id == anomaly.revision_id


def test_export_is_deterministic():
    a = TEBDLC()
    b = TEBDLC()
    for ledger in (a, b):
        gain = ledger.add(GainRecord.create(title="A", description="B"))
        ledger.validate(gain.gain_id, evidence=("proof",))
    assert a.export_json() == b.export_json()


def test_no_loss_guard_rejects_missing_validated_gain():
    before = TEBDLC()
    gain = before.add(GainRecord.create(title="A", description="B"))
    before.validate(gain.gain_id, evidence=("proof",))
    after = TEBDLC()
    with pytest.raises(AssertionError):
        after.assert_no_loss_against(before)


def test_reconciliation_agreed_only_and_conflict():
    left = TEBDLC()
    right = TEBDLC()
    shared = GainRecord.create(title="Shared", description="same")
    only_left = GainRecord.create(title="L", description="left")
    left.add(shared)
    right.add(shared)
    left.add(only_left)
    results = {item.gain_id: item for item in left.reconcile(right)}
    assert results[shared.gain_id].status is ReconciliationStatus.AGREED
    assert results[only_left.gain_id].status is ReconciliationStatus.ONLY_SOURCE_A

    left.revise(shared.gain_id, description="left divergence")
    right.revise(shared.gain_id, description="right divergence")
    results = {item.gain_id: item for item in left.reconcile(right)}
    assert results[shared.gain_id].status is ReconciliationStatus.CONFLICT
