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


FOLDER = "0129-sum-root-to-leaf-numbers"


def digit_paths(tree):
    if tree is None:
        return []
    if tree[1] is None and tree[2] is None:
        return [[tree[0] % 10]]
    return [[tree[0] % 10] + path for child in (tree[1], tree[2]) for path in digit_paths(child)]


def digits(tree):
    return None if tree is None else (tree[0] % 10, digits(tree[1]), digits(tree[2]))


def depth(tree):
    return 0 if tree is None else 1 + max(depth(tree[1]), depth(tree[2]))


@given(TREES.filter(lambda tree: tree is not None and depth(tree) <= 6))
def test_carried_number_matches_independent_digit_string_paths(tree):
    expected = sum(int("".join(map(str, path))) for path in digit_paths(tree))
    assert evaluate(FOLDER, args=[encode(digits(tree))]) == expected
