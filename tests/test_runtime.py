"""Adapter regressions that would otherwise conceal solution failures."""

from copy import deepcopy

import pytest

from atlas.runtime import (
    ListNode,
    TreeNode,
    build_tree,
    check_result,
    evaluate,
    list_to_json,
    load_module,
    tree_to_json,
)


def test_sparse_tree_uses_queue_based_level_order():
    values = [1, None, 2, 3]
    root = build_tree(values)
    assert root.left is None
    assert root.right.val == 2
    assert root.right.left.val == 3
    assert tree_to_json(root) == values
    assert evaluate("0102-binary-tree-level-order-traversal", args=[values]) == [[1], [2], [3]]


def test_empty_tree_serializes_canonically():
    assert tree_to_json(build_tree([])) == []
    assert tree_to_json(build_tree([None, None])) == []


def test_unreachable_tree_values_are_rejected():
    with pytest.raises(ValueError, match="unreachable"):
        build_tree([1, None, None, 9])
    with pytest.raises(ValueError, match="absent root"):
        build_tree([None, 9])


def test_input_mutation_cannot_change_shared_fixtures():
    args = [[["1", "1"], ["0", "1"]]]
    original = deepcopy(args)
    assert evaluate("0200-number-of-islands", args=args) == 1
    assert args == original
    assert evaluate("0200-number-of-islands", args=args) == 1


def test_rewired_linked_result_is_serialized_without_changing_input():
    args = [[1, 2, 3]]
    assert evaluate("0206-reverse-linked-list", args=args) == [3, 2, 1]
    assert args == [[1, 2, 3]]


def test_list_cycle_fails_instead_of_hanging():
    first, second = ListNode(1), ListNode(2)
    first.next, second.next = second, first
    with pytest.raises(ValueError, match="cycle"):
        list_to_json(first)


def test_tree_shared_children_are_rejected():
    shared = TreeNode(2)
    root = TreeNode(1, shared, shared)
    with pytest.raises(ValueError, match="shared child"):
        tree_to_json(root)


def test_solution_namespace_is_fresh_for_each_load():
    first = load_module("0001-two-sum")
    first.external_marker = "should not leak"
    second = load_module("0001-two-sum")
    assert first is not second
    assert not hasattr(second, "external_marker")


def test_design_sequence_constructs_and_emits_one_result_per_operation():
    operations = ["MinStack", "push", "push", "getMin", "pop", "top", "getMin"]
    arguments = [[], [4], [-2], [], [], [], []]
    original = deepcopy(arguments)
    assert evaluate("0155-min-stack", operations=operations, arguments=arguments) == [
        None,
        None,
        None,
        -2,
        None,
        4,
        4,
    ]
    assert arguments == original


@pytest.mark.parametrize(
    "operations,arguments",
    [([], []), (["MinStack", "push"], [[]]), (["push"], [[]]), (["MinStack"], [1])],
)
def test_invalid_design_sequences_fail_before_execution(operations, arguments):
    with pytest.raises(ValueError):
        evaluate("0155-min-stack", operations=operations, arguments=arguments)


def test_method_argument_count_must_match_metadata():
    with pytest.raises(ValueError, match="Argument count"):
        evaluate("0001-two-sum", args=[[1, 2]])


def test_ordered_output_checker_cannot_hide_permutations_or_scalar_type_errors():
    exact = {"checker": "exact"}
    assert not check_result(exact, [[2, 1], [3]], [[1, 2], [3]])
    assert not check_result(exact, [[3], [1, 2]], [[1, 2], [3]])
    assert not check_result(exact, 1, True)


def test_unordered_checkers_preserve_multiplicity_and_only_declared_order_freedom():
    flat = {"checker": "unordered"}
    assert check_result(flat, [2, 1, 1], [1, 2, 1])
    assert not check_result(flat, [2, 1], [1, 2, 1])
    rows = {"checker": "unordered_rows"}
    assert check_result(rows, [[1, 2], [3]], [[3], [1, 2]])
    assert not check_result(rows, [[2, 1], [3]], [[3], [1, 2]])
    groups = {"checker": "unordered_groups"}
    assert check_result(groups, [["b", "a"], ["x"]], [["x"], ["a", "b"]])
    assert not check_result(groups, [["a", "a"]], [["a"]])


def test_flat_checker_rejects_nested_output():
    with pytest.raises(ValueError, match="flat"):
        check_result({"checker": "unordered"}, [[1, 2]], [[2, 1]])
