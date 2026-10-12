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


FOLDER = "0230-kth-smallest-element-in-a-bst"


def insert(tree, value):
    if tree is None:
        return (value, None, None)
    root, left, right = tree
    if value < root:
        return (root, insert(left, value), right)
    return (root, left, insert(right, value))


@given(st.lists(st.integers(0, 10000), min_size=1, max_size=60, unique=True), st.data())
def test_rank_matches_sorted_inserted_values(values, data):
    tree = None
    for value in values:
        tree = insert(tree, value)
    k = data.draw(st.integers(1, len(values)))
    assert evaluate(FOLDER, args=[encode(tree), k]) == sorted(values)[k - 1]


def test_deep_bst_can_return_final_rank():
    size = 2500
    chain = [0] + [value for index in range(1, size) for value in (None, index)]
    assert evaluate(FOLDER, args=[chain, size]) == size - 1
