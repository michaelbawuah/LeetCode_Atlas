from collections import deque

from hypothesis import given
from hypothesis import strategies as st

from atlas.runtime import build_tree, evaluate, load_module

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


FOLDER = "0617-merge-two-binary-trees"


def tuple_merge(first, second):
    if first is None:
        return second
    if second is None:
        return first
    return (
        first[0] + second[0],
        tuple_merge(first[1], second[1]),
        tuple_merge(first[2], second[2]),
    )


@given(TREES, TREES)
def test_fresh_merge_matches_tuple_positions_and_never_aliases_inputs(first, second):
    assert evaluate(FOLDER, args=[encode(first), encode(second)]) == encode(
        tuple_merge(first, second)
    )
    left, right = build_tree(encode(first)), build_tree(encode(second))
    before_left, before_right = snapshot(left), snapshot(right)
    result = load_module(FOLDER).Solution().mergeTrees(left, right)
    assert set(snapshot(result)).isdisjoint(set(before_left) | set(before_right))
    assert snapshot(left) == before_left and snapshot(right) == before_right
