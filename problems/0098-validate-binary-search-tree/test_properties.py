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


FOLDER = "0098-validate-binary-search-tree"
NONEMPTY = TREES.filter(lambda tree: tree is not None)


def bounded_reference(tree, lower=None, upper=None):
    if tree is None:
        return True
    value, left, right = tree
    return (
        (lower is None or value > lower)
        and (upper is None or value < upper)
        and bounded_reference(left, lower, value)
        and bounded_reference(right, value, upper)
    )


@given(NONEMPTY)
def test_inorder_check_matches_ancestor_bounds(tree):
    assert evaluate(FOLDER, args=[encode(tree)]) == bounded_reference(tree)


def test_deep_valid_chain_uses_an_explicit_stack():
    chain = [0] + [value for index in range(1, 2500) for value in (None, index)]
    assert evaluate(FOLDER, args=[chain]) is True
