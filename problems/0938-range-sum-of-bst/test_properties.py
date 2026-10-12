from collections import deque

from hypothesis import given
from hypothesis import strategies as st

from atlas.runtime import build_tree, evaluate, load_module

TREES = st.recursive(
    st.none(),
    lambda child: st.tuples(st.integers(-20, 20), child, child),
    max_leaves=20,
)
NONEMPTY = TREES.filter(lambda tree: tree is not None)


def encode(tree):
    if tree is None:
        return []
    queue, values = deque([tree]), []
    while queue:
        node = queue.popleft()
        if node is None:
            values.append(None)
        else:
            values.append(node[0])
            queue.extend((node[1], node[2]))
    while values and values[-1] is None:
        values.pop()
    return values


def levels(tree):
    result, level = [], [tree] if tree is not None else []
    while level:
        result.append([node[0] for node in level])
        level = [child for node in level for child in (node[1], node[2]) if child is not None]
    return result


def snapshot(root):
    output, pending = {}, [root] if root is not None else []
    while pending:
        node = pending.pop()
        assert id(node) not in output
        output[id(node)] = (node.val, node.left, node.right)
        if node.left is not None:
            pending.append(node.left)
        if node.right is not None:
            pending.append(node.right)
    return output


def bst(values):
    if not values:
        return None
    value = values[0]
    return (
        value,
        bst([other for other in values[1:] if other < value]),
        bst([other for other in values[1:] if other > value]),
    )


FOLDER = "0938-range-sum-of-bst"


@given(
    st.lists(st.integers(1, 100000), min_size=1, max_size=35, unique=True),
    st.integers(1, 100000),
    st.integers(1, 100000),
)
def test_pruned_sum_matches_flat_original_value_filter_and_preserves_links(values, first, second):
    low, high = sorted((first, second))
    tree = bst(values)
    expected = sum(value for value in values if low <= value <= high)
    assert evaluate(FOLDER, args=[encode(tree), low, high]) == expected
    root = build_tree(encode(tree))
    before = snapshot(root)
    assert load_module(FOLDER).Solution().rangeSumBST(root, low, high) == expected
    assert snapshot(root) == before
