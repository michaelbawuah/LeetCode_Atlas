"""Identity, witness, ownership and parity-discovery regressions for milestone300."""

import importlib.util
import json
import math
import random
from pathlib import Path
from types import SimpleNamespace

import pytest

import atlas.runtime as runtime
from atlas.runtime import (
    TreeNode,
    build_list_array,
    build_tree,
    check_result,
    list_to_json,
    resolve_tree_ref,
)

ROOT = Path(__file__).resolve().parents[1]


def test_list_array_builds_separate_borrowed_lists_and_preserves_empty_entries():
    source = [[], [1, 4, 5], [1, 3, 4]]
    lists = build_list_array(source)
    assert lists[0] is None
    assert lists[1] is not lists[2]
    assert [list_to_json(head) for head in lists] == source
    lists[1].val = 9
    assert lists[2].val == 1
    assert source == [[], [1, 4, 5], [1, 3, 4]]
    assert build_list_array([]) == []


@pytest.mark.parametrize("source", [None, {}, [None], [[True]], [[1.0]], [["1"]], ["1"]])
def test_list_array_shape_and_integer_values_are_required(source):
    with pytest.raises(ValueError, match="outer array"):
        build_list_array(source)


def test_tree_references_resolve_to_unique_existing_node_identities():
    root = build_tree([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5])
    assert resolve_tree_ref(root, 2) is root.left
    assert resolve_tree_ref(root, 5) is root.left.right.right
    for value in [None, True, 2.0, "2"]:
        with pytest.raises(ValueError, match="integers"):
            resolve_tree_ref(root, value)
    with pytest.raises(ValueError, match="exactly one"):
        resolve_tree_ref(root, 10)
    with pytest.raises(ValueError, match="exactly one"):
        resolve_tree_ref(build_tree([1, 2, 2]), 2)
    root.left.left = root
    with pytest.raises(ValueError, match="cycle"):
        resolve_tree_ref(root, 6)


def _reference_eval(monkeypatch, solution):
    meta = {
        "kind": "method",
        "method": "lowestCommonAncestor",
        "args_types": ["treenode", "tree_ref", "tree_ref"],
        "return_type": "tree_ref",
    }
    monkeypatch.setattr(runtime, "metadata", lambda folder: meta)
    monkeypatch.setattr(runtime, "load_module", lambda folder: SimpleNamespace(Solution=solution))


def test_reference_evaluation_passes_original_nodes_and_preserves_fixture_input(monkeypatch):
    class ExistingAncestor:
        def lowestCommonAncestor(self, root, first, second):
            assert first is root.left
            assert second is root.right
            return root

    _reference_eval(monkeypatch, ExistingAncestor)
    args = [[2, 1, 3], 1, 3]
    assert runtime.evaluate("synthetic", args=args) == 2
    assert args == [[2, 1, 3], 1, 3]


def test_reference_result_rejects_a_fresh_node_with_the_same_value(monkeypatch):
    class CounterfeitAncestor:
        def lowestCommonAncestor(self, root, first, second):
            return TreeNode(root.val)

    _reference_eval(monkeypatch, CounterfeitAncestor)
    with pytest.raises(ValueError, match="belong to the original tree"):
        runtime.evaluate("synthetic", args=[[2, 1, 3], 1, 3])


def test_reference_result_rejects_a_wrong_original_node_with_rewritten_ancestor_label(monkeypatch):
    class RewrittenAncestor:
        def lowestCommonAncestor(self, root, first, second):
            first.val = root.val
            return first

    _reference_eval(monkeypatch, RewrittenAncestor)
    with pytest.raises(ValueError, match="changed its original value"):
        runtime.evaluate("synthetic", args=[[2, 1, 3], 1, 3])


def test_peak_checker_accepts_any_strict_peak_and_rejects_boolean_or_nonpeak_indices():
    meta = {"checker": "peak_index"}
    args = [[1, 3, 2, 4, 1]]
    assert check_result(meta, 1, 3, args=args)
    assert check_result(meta, 3, 1, args=args)
    for actual in [0, 2, 4, -1, 5, True, 1.0]:
        assert not check_result(meta, actual, 1, args=args)
    assert check_result(meta, 0, 0, args=[[10]])
    assert check_result(meta, 0, 0, args=[[2, 1]])
    assert check_result(meta, 1, 1, args=[[1, 2]])
    # Checker robustness beyond the unequal-adjacent-value input contract.
    assert not check_result(meta, 0, 0, args=[[2, 2]])


def test_balanced_bst_checks_semantics_instead_of_one_example_shape():
    meta = {"checker": "balanced_bst"}
    original = [-10, -3, 0, 5, 9]
    example = [0, -3, 9, -10, None, 5]
    alternative = [0, -10, 5, None, -3, None, 9]
    assert check_result(meta, alternative, example, args=[original])
    assert not check_result(
        meta, [-10, None, -3, None, 0, None, 5, None, 9], example, args=[original]
    )
    assert not check_result(meta, [0, 9, -3], example, args=[original])
    assert not check_result(meta, [0, None, None, 9], example, args=[original])
    assert not check_result(meta, [True], [1], args=[[1]])
    assert not check_result(meta, [1.0], [1], args=[[1]])
    with pytest.raises(ValueError, match="sorted unique"):
        check_result(meta, [1, 1], [1, 1], args=[[1, 1]])


def test_bst_inorder_accepts_remaining_or_inserted_values_and_rejects_invalid_trees():
    meta = {"checker": "bst_inorder"}
    values = [1, 2, 3, 4]
    assert check_result(meta, [3, 1, 4, None, 2], values)
    assert check_result(meta, [2, 1, 3, None, None, None, 4], values)
    assert check_result(meta, [], [])
    assert not check_result(meta, [2, 3, 1], [1, 2, 3])
    assert not check_result(meta, [2, 1, 2], [1, 2])
    assert not check_result(meta, [], [1])
    assert not check_result(meta, [1, None, None, 2], [1, 2])
    with pytest.raises(ValueError, match="sorted unique"):
        check_result(meta, [1], [True])


def test_approximate_lists_preserve_arity_and_reject_nonfinite_or_boolean_elements():
    meta = {"checker": "approx_list"}
    assert check_result(meta, [1 + 5e-10, 5e-13, -2.0], [1, 0, -2])
    assert check_result(meta, [], [])
    for actual in [[1], [1, True], [1, math.inf], [1, math.nan], [1, "2"], [[1], 2], 1]:
        assert not check_result(meta, actual, [1, 2])
    assert not check_result(meta, [1, 2.1], [1, 2])


def test_absolute_level_average_tolerance_accepts_small_errors_but_rejects_scaled_errors():
    averages = {
        "checker": "approx_list",
        "numeric_tolerance": {"relative": 0, "absolute": 1e-5},
    }
    assert check_result(averages, [1 + 1e-6], [1])
    assert not check_result(averages, [1e9 + 0.5], [1e9])
    ratios = {
        "checker": "approx_list",
        "numeric_tolerance": {"relative": 1e-5, "absolute": 1e-5},
    }
    assert check_result(ratios, [2 + 1e-5], [2])
    assert not check_result(ratios, [2 + 1e-3], [2])
    # Existing scalar policies retain their original relative and absolute defaults.
    assert check_result({"checker": "approx"}, 1 + 5e-10, 1)
    assert check_result({"checker": "approx"}, 1e9 + 0.5, 1e9)


@pytest.mark.parametrize(
    "policy",
    [
        {"relative": -1e-9, "absolute": 1e-5},
        {"relative": 0, "absolute": math.inf},
        {"relative": math.nan, "absolute": 1e-5},
        {"relative": True, "absolute": 1e-5},
        {"relative": 0, "absolute": False},
        {"relative": 0, "absolute": 10**1000},
        {"relative": 0},
        {"relative": 0, "absolute": 1e-5, "extra": 0},
    ],
)
def test_runtime_rejects_unsafe_or_incomplete_numeric_tolerance_policies(policy):
    with pytest.raises(ValueError, match="finite nonnegative"):
        check_result({"checker": "approx_list", "numeric_tolerance": policy}, [1], [1])


def _load_file(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_parity_registration_detects_missing_and_unexpected_counterparts():
    parity = _load_file("atlas_parity_tests300", ROOT / "tests/test_cpp_properties.py")
    assert len(parity.LEGACY_FOLDERS) == len(parity.NEW_FOLDERS) == 75
    assert len(parity.ADDED_FOLDERS) == 75
    assert len(parity.PER_PROBLEM_FOLDERS) == 150
    assert len(parity.FOLDERS) == 225
    parity.validate_counterpart_coverage(set(parity.FOLDERS))
    incomplete = set(parity.FOLDERS) - {parity.FOLDERS[0]}
    with pytest.raises(ValueError, match="missing"):
        parity.validate_counterpart_coverage(incomplete)
    with pytest.raises(ValueError, match="unexpected"):
        parity.validate_counterpart_coverage(set(parity.FOLDERS) | {"9999-unregistered"})


@pytest.mark.parametrize(
    "source",
    [
        "generate = 7",
        "def generate(): return []",
        "def generate(rng, other): return []",
        "def generate(*args): return []",
    ],
)
def test_parity_module_requires_one_explicit_rng_parameter(tmp_path, source):
    parity = _load_file("atlas_parity_shape300", ROOT / "tests/test_cpp_properties.py")
    path = tmp_path / "parity.py"
    path.write_text(source)
    with pytest.raises(ValueError, match="generate|RNG"):
        parity.load_parity_generator(path)


def test_parity_payload_validation_handles_designs_json_and_copy_isolation(tmp_path):
    parity = _load_file("atlas_parity_payload300", ROOT / "tests/test_cpp_properties.py")
    path = tmp_path / "parity.py"
    path.write_text("def generate(rng): return [[rng.randint(0, 100)]]\n")
    generator = parity.load_parity_generator(path)
    assert generator(random.Random(123)) == generator(random.Random(123))
    method = {"kind": "method", "args_types": ["value"]}
    source = [[1, 2]]
    copied = parity.validate_generated_payload(method, source)
    copied[0].append(3)
    assert source == [[1, 2]]
    for payload in [None, [], [math.inf], [object()], [(1, 2)], [{1: "bad key"}]]:
        with pytest.raises(ValueError):
            parity.validate_generated_payload(method, payload)
    design = {"kind": "design", "class_name": "Example"}
    assert parity.validate_generated_payload(design, [["Example", "get"], [[], [1]]]) == [
        ["Example", "get"],
        [[], [1]],
    ]
    for payload in [
        [["Example"], []],
        [["get"], [[]]],
        [["Example", "_private"], [[], []]],
        [["Example", "Example"], [[], []]],
        [["Example", False], [[], []]],
    ]:
        with pytest.raises(ValueError):
            parity.validate_generated_payload(design, payload)


def _catalog_fixture(tmp_path, *, cpp=False):
    catalog = _load_file("atlas_catalog300", ROOT / "tools/catalog.py")
    source = ROOT / "problems/0001-two-sum"
    folder = tmp_path / "problems/0001-two-sum"
    folder.mkdir(parents=True)
    names = ["meta.json", "README.md", "cases.json", "solution.py", "test_properties.py"]
    if cpp:
        names.extend(["solution.cpp", "cpp_runner.cpp"])
    for name in names:
        (folder / name).write_text((source / name).read_text())
    return catalog, folder, json.loads((folder / "meta.json").read_text())


def test_catalog_requires_explicit_paired_complexities_for_cpp(tmp_path):
    catalog, folder, meta = _catalog_fixture(tmp_path, cpp=True)
    meta.pop("complexity_cpp")
    (folder / "meta.json").write_text(json.dumps(meta))
    with pytest.raises(ValueError, match="complexity_cpp"):
        catalog.collect(tmp_path)
    meta["complexity_cpp"] = {"time": "TODO", "space": "O(n)"}
    (folder / "meta.json").write_text(json.dumps(meta))
    with pytest.raises(ValueError, match="meaningful"):
        catalog.collect(tmp_path)
    meta["complexity_cpp"] = {"time": "O(n) expected", "space": "O(n)"}
    meta.pop("complexity_language")
    (folder / "meta.json").write_text(json.dumps(meta))
    with pytest.raises(ValueError, match="explicit Python"):
        catalog.collect(tmp_path)


def test_catalog_preserves_legacy_python_scope_and_rejects_bad_tree_reference_declarations(
    tmp_path,
):
    catalog, folder, meta = _catalog_fixture(tmp_path)
    meta.pop("complexity_language")
    (folder / "meta.json").write_text(json.dumps(meta))
    assert catalog.collect(tmp_path)[0]["languages"] == ["Python"]
    meta.update(args_types=["value", "tree_ref", "tree_ref"], return_type="tree_ref")
    (folder / "meta.json").write_text(json.dumps(meta))
    with pytest.raises(ValueError, match="original tree"):
        catalog.collect(tmp_path)


@pytest.mark.parametrize(
    "policy",
    [
        {"relative": -1e-9, "absolute": 1e-5},
        {"relative": 0, "absolute": math.inf},
        {"relative": math.nan, "absolute": 1e-5},
        {"relative": True, "absolute": 1e-5},
        {"relative": 0, "absolute": False},
        {"relative": 0, "absolute": 10**1000},
        {"relative": 0},
    ],
)
def test_catalog_rejects_negative_nonfinite_boolean_or_incomplete_numeric_tolerances(
    tmp_path, policy
):
    catalog, folder, meta = _catalog_fixture(tmp_path)
    meta.update(checker="approx_list", numeric_tolerance=policy)
    (folder / "meta.json").write_text(json.dumps(meta))
    with pytest.raises(ValueError, match="Numeric tolerance"):
        catalog.collect(tmp_path)
