# Jonathan Therrien, Marieville, Québec.

from __future__ import annotations

import argparse
import json
from importlib.metadata import PackageNotFoundError, version

from .core import GainRecord, SourceRef, TEBDLC


def _version() -> str:
    try:
        return version("tebdlc")
    except PackageNotFoundError:
        return "0+uninstalled"


def _self_check_payload() -> dict[str, object]:
    ledger = TEBDLC()
    source = SourceRef(
        source_id="cli-self-check",
        kind="internal-self-check",
        locator="tebdlc://self-check",
    )
    gain = GainRecord.create(
        title="TEBDLC CLI self-check",
        description="Deterministic local ledger construction and retrieval check.",
        sources=(source,),
        domains=("product-readiness",),
    )
    ledger.add(gain)
    recovered = ledger.get(gain.gain_id)
    ok = recovered.canonical() == gain.canonical()
    return {
        "product": "TEBDLC",
        "version": _version(),
        "self_check": "PASS" if ok else "FAIL",
        "gain_id": gain.gain_id,
        "gain_count": len(ledger.gains),
        "network_required": False,
    }


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="tebdlc",
        description="TEBDLC product command line interface.",
    )
    parser.add_argument("--version", action="version", version=f"%(prog)s {_version()}")
    sub = parser.add_subparsers(dest="command")

    info = sub.add_parser("info", help="Print product metadata.")
    info.add_argument("--json", action="store_true", dest="as_json")

    check = sub.add_parser("self-check", help="Run a deterministic local core self-check.")
    check.add_argument("--json", action="store_true", dest="as_json")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    if args.command == "info":
        payload = {
            "product": "TEBDLC",
            "version": _version(),
            "author": "Jonathan Therrien, Marieville, Québec.",
            "network_required": False,
        }
    elif args.command == "self-check":
        payload = _self_check_payload()
        if payload["self_check"] != "PASS":
            return 1
    else:
        build_parser().print_help()
        return 0

    if getattr(args, "as_json", False):
        print(json.dumps(payload, sort_keys=True, ensure_ascii=False))
    else:
        for key, value in payload.items():
            print(f"{key}: {value}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
