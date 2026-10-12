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


FOLDER = "0110-balanced-binary-tree"


def height(tree):
    return 0 if tree is None else 1 + max(height(tree[1]), height(tree[2]))


def direct_balance(tree):
    return tree is None or (
        abs(height(tree[1]) - height(tree[2])) <= 1
        and direct_balance(tree[1])
        and direct_balance(tree[2])
    )


@given(TREES)
def test_cached_postorder_matches_separate_height_checks(tree):
    assert evaluate(FOLDER, args=[encode(tree)]) == direct_balance(tree)


def test_deep_chain_does_not_overflow_python_call_stack():
    chain = [1] + [value for _ in range(2499) for value in (None, 1)]
    assert evaluate(FOLDER, args=[chain]) is False
