#!/usr/bin/env python3
# Jonathan Therrien, Marieville, Québec.
"""Reference controlled-delivery primitive for TEBDLC v0.1.

This module is intentionally storage/local-path oriented. It does not expose a public
network endpoint. Delivery occurs only after authentication/authorization, licence
acceptance binding, manifest binding, and package SHA-256 verification succeed.
"""
from __future__ import annotations

import hashlib
import json
import os
import shutil
import tempfile
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from audit_log import append_event
from authorize_request import authorize

ENGINE_VERSION = "controlled-delivery/0.1"


def _sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def _deny(reason: str, subject_id: str | None = None, state: str | None = None) -> dict[str, Any]:
    return {
        "decision": "DENY",
        "reason_code": reason,
        "subject_id": subject_id,
        "territorial_state": state,
        "delivery_engine_version": ENGINE_VERSION,
    }


def _required_keys(obj: dict[str, Any], keys: set[str]) -> bool:
    return isinstance(obj, dict) and keys.issubset(obj.keys())


def controlled_deliver(
    *,
    registry: dict[str, Any],
    credential_id: str,
    presented_secret: str,
    package_path: str | os.PathLike[str],
    release_manifest: dict[str, Any],
    licence_acceptance: dict[str, Any],
    output_directory: str | os.PathLike[str],
    now: datetime | None = None,
) -> dict[str, Any]:
    """Authorize and copy exactly one immutable package into an output directory.

    The function fails closed on malformed records, mismatches, unsafe paths,
    package mutation, missing acceptance, restricted/neutral rights failures,
    or any inability to establish identity and package integrity.
    """
    now = (now or datetime.now(timezone.utc)).astimezone(timezone.utc)

    authz = authorize(
        registry,
        credential_id,
        presented_secret,
        "DOWNLOAD_PACKAGE",
        now,
    )
    if authz.get("decision") != "ALLOW":
        return _deny(
            str(authz.get("reason_code", "DENY_AUTHORIZATION_FAILURE")),
            authz.get("subject_id"),
            authz.get("territorial_state"),
        )

    subject_id = authz.get("subject_id")
    state = authz.get("territorial_state")

    manifest_required = {
        "manifest_version", "release_id", "source_commits", "package_sha256",
        "assembly_procedure_version", "licence_version", "licence_sha256",
        "territorial_policy_version", "territorial_policy_sha256",
        "verification_record_sha256", "created_at",
    }
    acceptance_required = {
        "acceptance_id", "authorization_identity", "declared_territory",
        "territorial_state", "licence_version", "licence_sha256",
        "territorial_policy_version", "territorial_policy_sha256",
        "tebdlc_release", "package_sha256", "accepted_at",
        "acceptance_mechanism_version",
    }
    if not _required_keys(release_manifest, manifest_required):
        return _deny("DENY_MANIFEST_INTEGRITY_FAILURE", subject_id, state)
    if not _required_keys(licence_acceptance, acceptance_required):
        return _deny("DENY_NO_LICENCE_ACCEPTANCE", subject_id, state)

    if release_manifest.get("manifest_version") != "0.1":
        return _deny("DENY_MANIFEST_INTEGRITY_FAILURE", subject_id, state)
    if licence_acceptance.get("authorization_identity") != subject_id:
        return _deny("DENY_ACCEPTANCE_IDENTITY_MISMATCH", subject_id, state)
    if licence_acceptance.get("territorial_state") != state:
        return _deny("DENY_ACCEPTANCE_TERRITORY_MISMATCH", subject_id, state)
    if licence_acceptance.get("tebdlc_release") != release_manifest.get("release_id"):
        return _deny("DENY_RELEASE_MISMATCH", subject_id, state)

    for field in (
        "licence_version",
        "licence_sha256",
        "territorial_policy_version",
        "territorial_policy_sha256",
        "package_sha256",
    ):
        if licence_acceptance.get(field) != release_manifest.get(field):
            reason = (
                "DENY_PACKAGE_HASH_MISMATCH"
                if field == "package_sha256"
                else "DENY_LICENCE_VERSION_MISMATCH"
                if field == "licence_version"
                else "DENY_POLICY_INTEGRITY_FAILURE"
                if field.startswith("territorial_policy")
                else "DENY_LICENCE_INTEGRITY_FAILURE"
            )
            return _deny(reason, subject_id, state)

    expected_hash = release_manifest.get("package_sha256")
    if not isinstance(expected_hash, str) or len(expected_hash) != 64:
        return _deny("DENY_MANIFEST_INTEGRITY_FAILURE", subject_id, state)

    source = Path(package_path)
    if not source.is_file() or source.is_symlink():
        return _deny("DENY_PACKAGE_UNAVAILABLE", subject_id, state)

    try:
        source_resolved = source.resolve(strict=True)
        output = Path(output_directory)
        output.mkdir(parents=True, exist_ok=True)
        output_resolved = output.resolve(strict=True)
    except OSError:
        return _deny("DENY_PATH_INTEGRITY_FAILURE", subject_id, state)

    destination = output_resolved / source_resolved.name
    try:
        if destination.resolve(strict=False) == source_resolved:
            return _deny("DENY_PATH_INTEGRITY_FAILURE", subject_id, state)
    except OSError:
        return _deny("DENY_PATH_INTEGRITY_FAILURE", subject_id, state)

    try:
        pre_hash = _sha256_file(source_resolved)
    except OSError:
        return _deny("DENY_PACKAGE_UNAVAILABLE", subject_id, state)
    if pre_hash != expected_hash:
        return _deny("DENY_PACKAGE_HASH_MISMATCH", subject_id, state)

    temp_path: Path | None = None
    try:
        fd, tmp_name = tempfile.mkstemp(prefix=".tebdlc-delivery-", dir=str(output_resolved))
        os.close(fd)
        temp_path = Path(tmp_name)
        shutil.copyfile(source_resolved, temp_path)
        copied_hash = _sha256_file(temp_path)
        post_hash = _sha256_file(source_resolved)
        if copied_hash != expected_hash or post_hash != expected_hash:
            return _deny("DENY_PACKAGE_HASH_MISMATCH", subject_id, state)
        os.replace(temp_path, destination)
        temp_path = None
    except OSError:
        return _deny("DENY_DELIVERY_IO_FAILURE", subject_id, state)
    finally:
        if temp_path is not None:
            try:
                temp_path.unlink(missing_ok=True)
            except OSError:
                pass

    return {
        "decision": "ALLOW",
        "reason_code": authz.get("reason_code"),
        "subject_id": subject_id,
        "credential_id": authz.get("credential_id"),
        "territorial_state": state,
        "acceptance_id": licence_acceptance.get("acceptance_id"),
        "release_id": release_manifest.get("release_id"),
        "package_sha256": expected_hash,
        "delivered_filename": destination.name,
        "delivered_at": now.isoformat(),
        "delivery_engine_version": ENGINE_VERSION,
    }


def audited_controlled_deliver(*, audit_log_path: str | os.PathLike[str], **kwargs: Any) -> dict[str, Any]:
    """Run a delivery attempt and append its result to the hash-chained audit log.

    Both ALLOW and DENY outcomes are persisted. Raw presented secrets are never
    copied into the audit event.
    """
    now = kwargs.get("now")
    result = controlled_deliver(**kwargs)
    audit_event = dict(result)
    audit_event.pop("credential_secret", None)
    stored = append_event(audit_log_path, audit_event, now=now)
    returned = dict(result)
    returned["audit_sequence"] = stored["sequence"]
    returned["audit_entry_hash"] = stored["entry_hash"]
    return returned


def load_json(path: str | os.PathLike[str]) -> dict[str, Any]:
    with Path(path).open("r", encoding="utf-8") as fh:
        obj = json.load(fh)
    if not isinstance(obj, dict):
        raise ValueError("record must be a JSON object")
    return obj
