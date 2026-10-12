from collections import deque

from hypothesis import given
from hypothesis import strategies as st

from atlas.runtime import build_tree, load_module

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


FOLDER = "0538-convert-bst-to-greater-tree"


@given(st.lists(st.integers(-10000, 10000), max_size=35, unique=True))
def test_changed_values_match_independent_greater_sums_without_link_changes(values):
    root = build_tree(encode(bst(values)))
    before = snapshot(root)
    assert load_module(FOLDER).Solution().convertBST(root) is root
    after = snapshot(root)
    assert set(after) == set(before)
    for identifier, (value, left, right) in before.items():
        assert after[identifier] == (sum(other for other in values if other >= value), left, right)
