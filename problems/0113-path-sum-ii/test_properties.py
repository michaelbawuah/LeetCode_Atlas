from collections import deque

from hypothesis import given
from hypothesis import strategies as st

from atlas.runtime import build_tree, evaluate, load_module

TREES = st.recursive(
    st.none(),
    lambda child: st.tuples(st.integers(-20, 20), child, child),
    max_leaves=20,
)


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


def identities(root):
    result, stack = set(), [root] if root is not None else []
    while stack:
        node = stack.pop()
        assert id(node) not in result
        result.add(id(node))
        if node.right is not None:
            stack.append(node.right)
        if node.left is not None:
            stack.append(node.left)
    return result


FOLDER = "0113-path-sum-ii"


def all_paths(tree):
    if tree is None:
        return []
    if tree[1] is None and tree[2] is None:
        return [[tree[0]]]
    return [[tree[0]] + path for child in (tree[1], tree[2]) for path in all_paths(child)]


@given(TREES, st.integers(-1000, 1000))
def test_backtracked_results_match_enumerated_path_multiset(tree, target):
    expected = [path for path in all_paths(tree) if sum(path) == target]
    actual = evaluate(FOLDER, args=[encode(tree), target])
    assert sorted(actual) == sorted(expected)


def test_result_rows_do_not_alias_and_tree_links_remain_intact():
    root = build_tree([1, 1, 1])
    original_children = (root.left, root.right)
    result = load_module(FOLDER).Solution().pathSum(root, 2)
    assert result == [[1, 1], [1, 1]]
    assert result[0] is not result[1]
    result[0][0] = 99
    assert result[1] == [1, 1]
    assert (root.left, root.right) == original_children


def test_deep_path_uses_enter_leave_frames():
    size = 3500
    chain = [0] + [item for _ in range(size - 1) for item in (None, 0)]
    assert evaluate(FOLDER, args=[chain, 0]) == [[0] * size]
