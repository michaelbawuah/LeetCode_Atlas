"""Catalog errors must be caught before the public index can mislead readers."""

import importlib.util
import json
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("catalog", ROOT / "tools/catalog.py")
catalog = importlib.util.module_from_spec(spec)
spec.loader.exec_module(catalog)


def test_generated_catalog_matches_actual_files():
    for path, expected in catalog.render(catalog.collect()).items():
        assert (ROOT / path).read_text() == expected, f"Regenerate {path}"


def test_duplicate_ids_and_unsupported_acceptance_are_rejected(tmp_path):
    source = ROOT / "problems/0001-two-sum"
    target = tmp_path / "problems/0001-two-sum"
    target.mkdir(parents=True)
    for name in ("meta.json", "README.md", "cases.json", "solution.py", "test_properties.py"):
        (target / name).write_text((source / name).read_text())
    meta = json.loads((target / "meta.json").read_text())
    meta["judge_status"] = "accepted"
    (target / "meta.json").write_text(json.dumps(meta))
    with pytest.raises(ValueError, match="requires dated submission evidence"):
        catalog.collect(tmp_path)
    meta["judge_status"] = "not_recorded"
    (target / "meta.json").write_text(json.dumps(meta))
    second = tmp_path / "problems/0001-another-two-sum"
    second.mkdir()
    for name in ("README.md", "cases.json", "solution.py", "test_properties.py"):
        (second / name).write_text((source / name).read_text())
    meta["slug"] = "another-two-sum"
    (second / "meta.json").write_text(json.dumps(meta))
    with pytest.raises(ValueError, match="Duplicate problem ID"):
        catalog.collect(tmp_path)
