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


FOLDER = "0572-subtree-of-another-tree"
NONEMPTY = TREES.filter(lambda tree: tree is not None)


def reference_contains(tree, needle):
    if tree is None:
        return False
    return (
        tree == needle or reference_contains(tree[1], needle) or reference_contains(tree[2], needle)
    )


@given(NONEMPTY, NONEMPTY)
def test_candidate_search_matches_structural_reference(tree, needle):
    assert evaluate(FOLDER, args=[encode(tree), encode(needle)]) == reference_contains(tree, needle)


@given(NONEMPTY)
def test_whole_tree_is_always_a_subtree(tree):
    assert evaluate(FOLDER, args=[encode(tree), encode(tree)]) is True
