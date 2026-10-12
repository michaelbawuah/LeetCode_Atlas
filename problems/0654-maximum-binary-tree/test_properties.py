from hypothesis import given
from hypothesis import strategies as st

from atlas.runtime import evaluate

FOLDER = "0654-maximum-binary-tree"


def direct_maximum_ranges(values):
    if not values:
        return None
    index = values.index(max(values))
    return (
        values[index],
        direct_maximum_ranges(values[:index]),
        direct_maximum_ranges(values[index + 1 :]),
    )


def encode(tree):
    if tree is None:
        return []
    pending, values = [tree], []
    for node in pending:
        if node is None:
            values.append(None)
        else:
            values.append(node[0])
            pending.extend((node[1], node[2]))
    while values and values[-1] is None:
        values.pop()
    return values


@given(st.lists(st.integers(0, 1000), min_size=1, max_size=70, unique=True))
def test_monotonic_tree_matches_independent_recursive_maximum_splits(values):
    assert evaluate(FOLDER, args=[values]) == encode(direct_maximum_ranges(values))
