from collections import deque

from hypothesis import given
from hypothesis import strategies as st

from atlas.runtime import evaluate

FOLDER = "0104-maximum-depth-of-binary-tree"
TREES = st.recursive(
    st.none(),
    lambda children: st.tuples(st.integers(-100, 100), children, children),
    max_leaves=30,
)


def serialize(tree):
    if tree is None:
        return []
    queue, values = deque([tree]), []
    while queue:
        node = queue.popleft()
        if node is None:
            values.append(None)
        else:
            value, left, right = node
            values.append(value)
            queue.extend((left, right))
    while values and values[-1] is None:
        values.pop()
    return values


def recursive_depth(tree):
    return 0 if tree is None else 1 + max(recursive_depth(tree[1]), recursive_depth(tree[2]))


@given(TREES)
def test_iterative_depth_matches_recursive_definition(tree):
    assert evaluate(FOLDER, args=[serialize(tree)]) == recursive_depth(tree)


def test_deep_chain_avoids_recursive_call_limit():
    size = 2000
    encoded = [1] + [value for _ in range(size - 1) for value in (None, 1)]
    assert evaluate(FOLDER, args=[encoded]) == size
