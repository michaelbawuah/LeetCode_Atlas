from collections import deque

from hypothesis import given
from hypothesis import strategies as st

from atlas.runtime import evaluate

FOLDER = "0102-binary-tree-level-order-traversal"
TREES = st.recursive(
    st.none(),
    lambda children: st.tuples(st.integers(-1000, 1000), children, children),
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


def dfs_levels(tree):
    levels = []

    def visit(node, depth):
        if node is None:
            return
        if len(levels) == depth:
            levels.append([])
        levels[depth].append(node[0])
        visit(node[1], depth + 1)
        visit(node[2], depth + 1)

    visit(tree, 0)
    return levels


@given(TREES)
def test_bfs_levels_match_depth_grouped_dfs(tree):
    assert evaluate(FOLDER, args=[serialize(tree)]) == dfs_levels(tree)
