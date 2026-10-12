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


FOLDER = "0701-insert-into-a-binary-search-tree"


def inorder(node):
    return [] if node is None else inorder(node.left) + [node.val] + inorder(node.right)


@given(st.lists(st.integers(-100, 100), max_size=35, unique=True), st.data())
def test_insert_preserves_existing_nodes_and_adds_exactly_one_key(values, data):
    val = data.draw(st.integers(-200, 200).filter(lambda value: value not in values))
    root = build_tree(encode(bst(values)))
    before = snapshot(root)
    result = load_module(FOLDER).Solution().insertIntoBST(root, val)
    after = snapshot(result)
    assert inorder(result) == sorted(values + [val])
    assert set(before) <= set(after)
    assert len(after) == len(before) + 1
    assert all(after[identifier][0] == before[identifier][0] for identifier in before)
    if root is not None:
        assert result is root
        attachments = 0
        for identifier, (_, left, right) in before.items():
            for original, current in zip((left, right), after[identifier][1:], strict=True):
                if original is not None:
                    assert current is original
                elif current is not None:
                    assert id(current) not in before
                    attachments += 1
        assert attachments == 1
