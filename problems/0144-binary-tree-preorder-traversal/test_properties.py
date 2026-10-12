from collections import deque

from hypothesis import given
from hypothesis import strategies as st

from atlas.runtime import evaluate

TREES = st.recursive(
    st.none(),
    lambda children: st.tuples(st.integers(-100, 100), children, children),
    max_leaves=25,
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


FOLDER = "0144-binary-tree-preorder-traversal"


def recursive_preorder(tree):
    if tree is None:
        return []
    return [tree[0]] + recursive_preorder(tree[1]) + recursive_preorder(tree[2])


@given(TREES)
def test_stack_order_matches_recursive_definition(tree):
    assert evaluate(FOLDER, args=[encode(tree)]) == recursive_preorder(tree)
