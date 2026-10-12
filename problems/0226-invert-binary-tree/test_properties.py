from collections import deque

from hypothesis import given
from hypothesis import strategies as st

from atlas.runtime import build_tree, evaluate, load_module

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


FOLDER = "0226-invert-binary-tree"


def mirror(tree):
    return None if tree is None else (tree[0], mirror(tree[2]), mirror(tree[1]))


@given(TREES)
def test_iterative_inversion_matches_structural_mirror(tree):
    inverted = evaluate(FOLDER, args=[encode(tree)])
    assert inverted == encode(mirror(tree))
    assert evaluate(FOLDER, args=[inverted]) == encode(tree)


@given(TREES)
def test_mirror_reuses_exactly_the_input_nodes(tree):
    root = build_tree(encode(tree))

    def identities(start):
        ids, stack = set(), [start] if start is not None else []
        while stack:
            node = stack.pop()
            assert id(node) not in ids
            ids.add(id(node))
            if node.left is not None:
                stack.append(node.left)
            if node.right is not None:
                stack.append(node.right)
        return ids

    before = identities(root)
    mirrored = load_module(FOLDER).Solution().invertTree(root)
    assert mirrored is root
    assert identities(mirrored) == before
