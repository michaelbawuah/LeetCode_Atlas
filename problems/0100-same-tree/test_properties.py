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


FOLDER = "0100-same-tree"


@given(TREES, TREES)
def test_paired_traversal_matches_structural_tuple_equality(first, second):
    assert evaluate(FOLDER, args=[encode(first), encode(second)]) == (first == second)


@given(TREES)
def test_identical_serialized_trees_are_equal(tree):
    assert evaluate(FOLDER, args=[encode(tree), encode(tree)]) is True
