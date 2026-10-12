from collections import deque

from hypothesis import given
from hypothesis import strategies as st

from atlas.runtime import build_tree, evaluate, load_module

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


FOLDER = "0114-flatten-binary-tree-to-linked-list"


def preorder_values(tree):
    return [] if tree is None else [tree[0]] + preorder_values(tree[1]) + preorder_values(tree[2])


def chain_encoding(values):
    return (
        [] if not values else [values[0]] + [item for value in values[1:] for item in (None, value)]
    )


@given(TREES)
def test_flatten_matches_preorder_and_reuses_nodes_once(tree):
    assert evaluate(FOLDER, args=[encode(tree)]) == chain_encoding(preorder_values(tree))
    root = build_tree(encode(tree))
    before = identities(root)
    assert load_module(FOLDER).Solution().flatten(root) is None
    seen, values, node = set(), [], root
    while node is not None:
        assert node.left is None
        assert id(node) not in seen
        seen.add(id(node))
        values.append(node.val)
        node = node.right
    assert seen == before
    assert values == preorder_values(tree)


def test_deep_left_chain_is_flattened_iteratively():
    size = 1800
    chain = [1] + [item for _ in range(size - 1) for item in (1, None)]
    chain.pop()
    assert evaluate(FOLDER, args=[chain]) == chain_encoding([1] * size)
