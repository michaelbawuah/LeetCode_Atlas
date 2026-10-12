from collections import deque

from hypothesis import given
from hypothesis import strategies as st

from atlas.runtime import evaluate

TREES = st.recursive(
    st.none(),
    lambda child: st.tuples(st.integers(-20, 20), child, child),
    max_leaves=20,
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


def identities(root):
    result, stack = set(), [root] if root is not None else []
    while stack:
        node = stack.pop()
        assert id(node) not in result
        result.add(id(node))
        if node.right is not None:
            stack.append(node.right)
        if node.left is not None:
            stack.append(node.left)
    return result


FOLDER = "0145-binary-tree-postorder-traversal"


def recursive_postorder(tree):
    return (
        []
        if tree is None
        else recursive_postorder(tree[1]) + recursive_postorder(tree[2]) + [tree[0]]
    )


@given(TREES)
def test_ready_frames_match_recursive_postorder(tree):
    assert evaluate(FOLDER, args=[encode(tree)]) == recursive_postorder(tree)
