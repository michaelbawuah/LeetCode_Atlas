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


FOLDER = "1448-count-good-nodes-in-binary-tree"


def direct_path_checks(tree, ancestors=()):
    if tree is None:
        return 0
    good = int(all(tree[0] >= value for value in ancestors))
    return (
        good
        + direct_path_checks(tree[1], ancestors + (tree[0],))
        + direct_path_checks(tree[2], ancestors + (tree[0],))
    )


@given(NONEMPTY)
def test_running_maximum_matches_comparison_with_every_ancestor(tree):
    assert evaluate(FOLDER, args=[encode(tree)]) == direct_path_checks(tree)


def test_deep_negative_chain_uses_iterative_state():
    chain = [-1] + [item for _ in range(3999) for item in (None, -1)]
    assert evaluate(FOLDER, args=[chain]) == 4000
