"""Regressions for graph identity, cyclic lists, numeric and witness semantics."""

import importlib.util
import json
import math
from collections import deque
from pathlib import Path

import pytest

from atlas.runtime import (
    GraphNode,
    build_graph,
    build_list_cycle,
    check_result,
    graph_to_json,
    list_to_json,
    load_module,
)


def test_graph_cycle_preserves_shared_neighbor_identities_and_canonical_labels():
    root = build_graph([[4, 2], [3, 1], [4, 2], [1, 3]])
    assert root.neighbors[0].neighbors[0] is root
    assert root.neighbors[1].neighbors[1] is root
    assert graph_to_json(root) == [[2, 4], [1, 3], [2, 4], [1, 3]]
    assert graph_to_json(build_graph([])) == []
    assert graph_to_json(build_graph([[]])) == [[]]


def test_graph_serialization_uses_only_root_reachable_nodes():
    assert graph_to_json(build_graph([[], [3], [2]])) == [[]]
    assert graph_to_json(build_graph([[3], [], [1]])) == [[3], [], [1]]


@pytest.mark.parametrize(
    "adjacency",
    [None, {}, [None], [1], [[0]], [[2]], [[True]], [[1.0]], [["1"]]],
)
def test_graph_fixture_shape_and_neighbor_ranges_are_validated(adjacency):
    with pytest.raises(ValueError):
        build_graph(adjacency)


def test_graph_serializer_rejects_invalid_labels_neighbors_and_label_collisions():
    for value in [0, -1, True, 1.5]:
        with pytest.raises(ValueError, match="labels"):
            graph_to_json(GraphNode(value))
    root = GraphNode(1)
    root.neighbors = [None]
    with pytest.raises(ValueError, match="graph nodes"):
        graph_to_json(root)
    root.neighbors = (GraphNode(2),)
    with pytest.raises(ValueError, match="must be a list"):
        graph_to_json(root)
    root.neighbors = [GraphNode(2), GraphNode(2)]
    with pytest.raises(ValueError, match="share a label"):
        graph_to_json(root)


def test_graph_checker_ignores_neighbor_order_but_preserves_rows_and_multiplicity():
    meta = {"checker": "graph_adjacency"}
    assert check_result(meta, [[3, 2], [1], [1]], [[2, 3], [1], [1]])
    assert not check_result(meta, [[2, 2], [1]], [[2], [1]])
    assert not check_result(meta, [[2], [1, 3], [2]], [[2, 3], [1], [1]])
    with pytest.raises(ValueError, match="1-based"):
        check_result(meta, [[False]], [[1]])


def test_solution_modules_get_public_graph_node_aliases():
    module = load_module("0001-two-sum")
    assert module.Node is GraphNode
    assert module.GraphNode is GraphNode
    first, second = GraphNode(), GraphNode()
    first.neighbors.append(second)
    assert second.neighbors == []


def test_cyclic_list_fixture_links_to_the_original_target_node():
    head = build_list_cycle({"values": [3, 2, 0, -4], "pos": 1})
    second, third, fourth = head.next, head.next.next, head.next.next.next
    assert fourth.next is second
    assert third.next is fourth
    with pytest.raises(ValueError, match="cycle"):
        list_to_json(head)
    assert list_to_json(build_list_cycle({"values": [1, 2], "pos": -1})) == [1, 2]
    assert build_list_cycle({"values": [], "pos": -1}) is None
    singleton = build_list_cycle({"values": [7], "pos": 0})
    assert singleton.next is singleton


@pytest.mark.parametrize(
    "value",
    [
        None,
        {},
        {"values": [], "pos": 0},
        {"values": [1], "pos": 1},
        {"values": [1], "pos": -2},
        {"values": [1], "pos": False},
        {"values": [1.0], "pos": -1},
        {"values": [True], "pos": -1},
        {"values": "1", "pos": -1},
        {"values": [1], "pos": -1, "extra": 3},
    ],
)
def test_cyclic_list_fixture_errors_are_rejected(value):
    with pytest.raises(ValueError):
        build_list_cycle(value)


def test_approx_checker_uses_explicit_tolerances_and_rejects_boolean_nonfinite_values():
    meta = {"checker": "approx"}
    assert check_result(meta, 1.0 + 5e-10, 1)
    assert check_result(meta, 5e-13, 0.0)
    assert not check_result(meta, 1.0 + 5e-8, 1)
    assert not check_result(meta, 5e-11, 0.0)
    for actual, expected in [(True, 1), (1, True), (math.inf, math.inf), (math.nan, 0), ("1", 1)]:
        assert not check_result(meta, actual, expected)


def test_longest_palindrome_checker_accepts_ties_and_rejects_invalid_witnesses():
    meta = {"checker": "longest_palindrome"}
    assert check_result(meta, "aba", "bab", args=["babad"])
    assert check_result(meta, "bab", 3, args=["babad"])
    assert not check_result(meta, "bad", "bab", args=["babad"])
    assert not check_result(meta, "aaa", "bab", args=["babad"])
    assert not check_result(meta, "a", "bab", args=["babad"])
    assert not check_result(meta, 3, "bab", args=["babad"])
    with pytest.raises(ValueError, match="original string"):
        check_result(meta, "aba", "bab")


def test_gas_station_checker_simulates_the_original_route_and_handles_impossibility():
    meta = {"checker": "gas_station"}
    args = [[1, 2, 3, 4, 5], [3, 4, 5, 1, 2]]
    assert check_result(meta, 3, 3, args=args)
    assert not check_result(meta, 0, 3, args=args)
    assert not check_result(meta, True, 3, args=args)
    assert not check_result(meta, -1, 3, args=args)
    impossible = [[2, 3, 4], [3, 4, 3]]
    assert check_result(meta, -1, -1, args=impossible)
    assert not check_result(meta, 0, -1, args=impossible)
    assert not check_result(meta, -1, -1, args=[[1], [1]])
    # Checker robustness outside the unique-start problem contract: either start works.
    assert check_result(meta, 1, 0, args=[[2, 2], [1, 1]])
    with pytest.raises(ValueError, match="equal nonempty"):
        check_result(meta, 0, 0, args=[[1, 2], [1]])


def test_graph_clone_identity_sets_are_independent_of_serialized_topology():
    original = build_graph([[2], [1]])
    cloned = load_module("0133-clone-graph").Solution().cloneGraph(original)

    def identities(root):
        seen = set()
        pending = deque([root])
        while pending:
            node = pending.popleft()
            if id(node) in seen:
                continue
            seen.add(id(node))
            pending.extend(node.neighbors)
        return seen

    assert graph_to_json(original) == graph_to_json(cloned)
    assert identities(original).isdisjoint(identities(cloned))
    cloned.neighbors[0].val = 3
    assert original.neighbors[0].val == 2


def _catalog_fixture(tmp_path):
    root = Path(__file__).resolve().parents[1]
    spec = importlib.util.spec_from_file_location("atlas_catalog150", root / "tools/catalog.py")
    catalog = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(catalog)
    source = root / "problems/0001-two-sum"
    folder = tmp_path / "problems/0001-two-sum"
    folder.mkdir(parents=True)
    for name in ("meta.json", "README.md", "cases.json", "solution.py", "test_properties.py"):
        (folder / name).write_text((source / name).read_text())
    return catalog, folder, json.loads((folder / "meta.json").read_text())


def test_catalog_validates_special_checker_adapter_declarations(tmp_path):
    catalog, folder, meta = _catalog_fixture(tmp_path)
    meta.update(checker="graph_adjacency", args_types=["value"], return_type="value")
    (folder / "meta.json").write_text(json.dumps(meta))
    with pytest.raises(ValueError, match="declaration does not match"):
        catalog.collect(tmp_path)
    meta.update(args_types=["graphnode"], return_type="graphnode")
    (folder / "meta.json").write_text(json.dumps(meta))
    (folder / "cases.json").write_text(
        json.dumps([{"name": "graph", "args": [[[2], [1]]], "expected": [[2], [1]]}])
    )
    assert catalog.collect(tmp_path)[0]["checker"] == "graph_adjacency"
    meta.update(checker="exact", args_types=["listnode_cycle"], return_type="value")
    (folder / "meta.json").write_text(json.dumps(meta))
    (folder / "cases.json").write_text(
        json.dumps([{"name": "cycle", "args": [{"values": [1], "pos": 0}], "expected": True}])
    )
    assert catalog.collect(tmp_path)[0]["args_types"] == ["listnode_cycle"]


def test_catalog_rejects_boolean_approximate_reference_values(tmp_path):
    catalog, folder, meta = _catalog_fixture(tmp_path)
    meta.update(checker="approx", args_types=["value", "value"], return_type="value")
    (folder / "meta.json").write_text(json.dumps(meta))
    (folder / "cases.json").write_text(
        json.dumps([{"name": "numeric", "args": [2.0, 3], "expected": True}])
    )
    with pytest.raises(ValueError, match="finite numeric"):
        catalog.collect(tmp_path)
