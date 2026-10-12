from collections import deque

from hypothesis import given
from hypothesis import strategies as st

from atlas.runtime import evaluate

TREES = st.recursive(
    st.none(),
    lambda child: st.tuples(st.integers(-20, 20), child, child),
    max_leaves=20,
)
NONEMPTY = TREES.filter(lambda tree: tree is not None)


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


def levels(tree):
    result, level = [], [tree] if tree is not None else []
    while level:
        result.append([node[0] for node in level])
        level = [child for node in level for child in (node[1], node[2]) if child is not None]
    return result


def snapshot(root):
    output, pending = {}, [root] if root is not None else []
    while pending:
        node = pending.pop()
        assert id(node) not in output
        output[id(node)] = (node.val, node.left, node.right)
        if node.left is not None:
            pending.append(node.left)
        if node.right is not None:
            pending.append(node.right)
    return output


def bst(values):
    if not values:
        return None
    value = values[0]
    return (
        value,
        bst([other for other in values[1:] if other < value]),
        bst([other for other in values[1:] if other > value]),
    )


FOLDER = "0662-maximum-width-of-binary-tree"


def binary_path_positions(tree):
    rows = {}

    def visit(node, path):
        if node is None:
            return
        rows.setdefault(len(path), []).append(int(path or "0", 2))
        visit(node[1], path + "0")
        visit(node[2], path + "1")

    visit(tree, "")
    return max(max(row) - min(row) + 1 for row in rows.values())


@given(NONEMPTY)
def test_normalized_indexes_match_independent_binary_edge_paths(tree):
    assert evaluate(FOLDER, args=[encode(tree)]) == binary_path_positions(tree)


def test_deep_sparse_chain_keeps_normalized_width_one():
    chain = [0] + [item for _ in range(2499) for item in (None, 0)]
    assert evaluate(FOLDER, args=[chain]) == 1
