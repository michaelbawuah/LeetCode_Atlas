"""Check the platform semantics required by in-place and witness problems."""

import pytest

from atlas.runtime import check_result, evaluate, metadata


def test_any_valid_topological_order_is_accepted():
    meta = {"checker": "topological_order"}
    args = [4, [[2, 0], [2, 1], [3, 2]]]
    expected = [0, 1, 2, 3]
    assert check_result(meta, [1, 0, 2, 3], expected, args=args)
    assert not check_result(meta, [0, 2, 1, 3], expected, args=args)
    assert not check_result(meta, [0, 1, 2, 2], expected, args=args)
    assert not check_result(meta, [False, 1, 2, 3], expected, args=args)
    assert not check_result(meta, [], expected, args=args)
    with pytest.raises(ValueError, match="requires course count"):
        check_result(meta, expected, expected)


def test_cycle_fixture_requires_no_order():
    meta = {"checker": "topological_order"}
    args = [2, [[0, 1], [1, 0]]]
    assert check_result(meta, [], [], args=args)
    assert not check_result(meta, [0, 1], [], args=args)
    assert not check_result(meta, False, [], args=args)


def test_in_place_array_result_keeps_shared_fixture_unchanged():
    args = [[0, 1, 0, 3, 12]]
    assert evaluate("0283-move-zeroes", args=args) == [1, 3, 12, 0, 0]
    assert args == [[0, 1, 0, 3, 12]]
    assert evaluate("0283-move-zeroes", args=args) == [1, 3, 12, 0, 0]


def test_in_place_list_rewiring_is_serialized():
    args = [[1, 2, 3, 4, 5]]
    assert evaluate("0143-reorder-list", args=args) == [1, 5, 2, 4, 3]
    assert args == [[1, 2, 3, 4, 5]]


def test_merged_intervals_allow_outer_order_without_reversing_endpoints():
    meta = metadata("0056-merge-intervals")
    expected = [[1, 6], [8, 10]]
    assert check_result(meta, [[8, 10], [1, 6]], expected)
    assert not check_result(meta, [[10, 8], [1, 6]], expected)
    assert not check_result(meta, [[1, 6], [8, 10], [8, 10]], expected)
