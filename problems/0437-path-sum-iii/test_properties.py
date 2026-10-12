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


FOLDER = "0437-path-sum-iii"


def downward(tree, remaining):
    if tree is None:
        return 0
    return (
        int(tree[0] == remaining)
        + downward(tree[1], remaining - tree[0])
        + downward(tree[2], remaining - tree[0])
    )


def every_start(tree, target):
    return (
        0
        if tree is None
        else downward(tree, target) + every_start(tree[1], target) + every_start(tree[2], target)
    )


@given(TREES, st.integers(-1000, 1000))
def test_prefix_counts_match_independent_walks_from_every_start(tree, target):
    assert evaluate(FOLDER, args=[encode(tree), target]) == every_start(tree, target)


def test_deep_zero_chain_counts_every_contiguous_downward_segment():
    size = 900
    chain = [0] + [item for _ in range(size - 1) for item in (None, 0)]
    assert evaluate(FOLDER, args=[chain, 0]) == size * (size + 1) // 2
