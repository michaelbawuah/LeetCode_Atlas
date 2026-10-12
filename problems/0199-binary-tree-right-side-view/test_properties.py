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


FOLDER = "0199-binary-tree-right-side-view"


def breadth_first_right_edges(tree):
    if tree is None:
        return []
    level, result = [tree], []
    while level:
        result.append(level[-1][0])
        level = [child for node in level for child in (node[1], node[2]) if child is not None]
    return result


@given(TREES)
def test_right_first_dfs_matches_last_bfs_node_per_level(tree):
    assert evaluate(FOLDER, args=[encode(tree)]) == breadth_first_right_edges(tree)
