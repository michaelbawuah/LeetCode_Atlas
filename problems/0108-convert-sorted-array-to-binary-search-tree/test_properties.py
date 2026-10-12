from hypothesis import given
from hypothesis import strategies as st

from atlas.runtime import evaluate, load_module

FOLDER = "0108-convert-sorted-array-to-binary-search-tree"


def inorder_and_height(node):
    if node is None:
        return [], 0
    left, left_height = inorder_and_height(node.left)
    right, right_height = inorder_and_height(node.right)
    assert abs(left_height - right_height) <= 1
    return left + [node.val] + right, 1 + max(left_height, right_height)


def ids(node):
    if node is None:
        return set()
    return {id(node)} | ids(node.left) | ids(node.right)


@given(st.lists(st.integers(-10000, 10000), min_size=1, max_size=100, unique=True).map(sorted))
def test_output_is_balanced_has_exact_inorder_and_separate_call_ownership(values):
    before = values.copy()
    solver = load_module(FOLDER).Solution()
    first, second = solver.sortedArrayToBST(values), solver.sortedArrayToBST(values)
    assert inorder_and_height(first)[0] == values
    assert inorder_and_height(second)[0] == values
    assert ids(first).isdisjoint(ids(second))
    assert values == before
    assert evaluate(FOLDER, args=[values])
