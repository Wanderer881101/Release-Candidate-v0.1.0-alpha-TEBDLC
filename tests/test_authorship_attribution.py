# Jonathan Therrien, Marieville, Québec.

from pathlib import Path


REQUIRED_ATTRIBUTION = "Jonathan Therrien, Marieville, Québec."
TEXT_SUFFIXES = {".md", ".py", ".toml", ".yml", ".yaml"}


def test_all_tebdlc_text_files_carry_required_attribution():
    root = Path(__file__).resolve().parents[1]
    missing = []
    for path in sorted(root.rglob("*")):
        if not path.is_file() or path.suffix.lower() not in TEXT_SUFFIXES:
            continue
        if any(part in {".git", ".pytest_cache", "__pycache__"} for part in path.parts):
            continue
        text = path.read_text(encoding="utf-8")
        if REQUIRED_ATTRIBUTION not in text:
            missing.append(str(path.relative_to(root)))
    assert not missing, f"missing required attribution: {missing}"
