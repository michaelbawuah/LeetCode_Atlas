from collections import deque

from hypothesis import given
from hypothesis import strategies as st

from atlas.runtime import evaluate

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


FOLDER = "0112-path-sum"


def all_paths(tree):
    if tree is None:
        return []
    if tree[1] is None and tree[2] is None:
        return [[tree[0]]]
    return [[tree[0]] + path for child in (tree[1], tree[2]) for path in all_paths(child)]


@given(TREES, st.integers(-1000, 1000))
def test_frontier_sum_matches_enumerated_complete_paths(tree, target):
    assert evaluate(FOLDER, args=[encode(tree), target]) == any(
        sum(path) == target for path in all_paths(tree)
    )


def test_deep_zero_chain_has_a_complete_zero_path():
    chain = [0] + [item for _ in range(3999) for item in (None, 0)]
    assert evaluate(FOLDER, args=[chain, 0]) is True
