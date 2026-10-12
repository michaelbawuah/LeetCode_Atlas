from collections import deque

from hypothesis import given, settings
from hypothesis import strategies as st

from atlas.runtime import build_tree, evaluate

FOLDER = "0337-house-robber-iii"


def oracle(encoded):
    root = build_tree(encoded)
    values, edges, pending = [], [], [(root, None)]
    while pending:
        node, parent = pending.pop()
        index = len(values)
        values.append(node.val)
        if parent is not None:
            edges.append((parent, index))
        if node.left is not None:
            pending.append((node.left, index))
        if node.right is not None:
            pending.append((node.right, index))
    return max(
        sum(value for index, value in enumerate(values) if mask & (1 << index))
        for mask in range(1 << len(values))
        if all(not (mask & (1 << first) and mask & (1 << second)) for first, second in edges)
    )


def small_trees():
    return st.recursive(
        st.none(), lambda children: st.tuples(st.integers(0, 20), children, children), max_leaves=8
    ).filter(lambda tree: tree is not None)


def encode(tree):
    queue, values = deque([tree]), []
    while queue:
        node = queue.popleft()
        if node is None:
            values.append(None)
        else:
            values.append(node[0])
            queue.extend((node[1], node[2]))
    while values[-1] is None:
        values.pop()
    return values


@settings(max_examples=60, deadline=None)
@given(small_trees().map(lambda tree: (encode(tree),)))
def test_optimized_matches_independent_small_or_model_oracle(args):
    assert evaluate(FOLDER, args=list(args)) == oracle(*args)


def test_official_maximum_skewed_tree_avoids_recursion_limit():
    size = 10000
    chain = [1] + [item for _ in range(size - 1) for item in (None, 1)]
    assert evaluate(FOLDER, args=[chain]) == 5000
