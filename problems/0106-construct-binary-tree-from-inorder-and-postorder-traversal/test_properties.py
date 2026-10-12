from collections import deque

from hypothesis import given
from hypothesis import strategies as st

from atlas.runtime import evaluate, load_module

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


FOLDER = "0106-construct-binary-tree-from-inorder-and-postorder-traversal"


def uniquely_labeled(tree):
    counter = iter(range(-100, 100))

    def assign(node):
        if node is None:
            return None
        value = next(counter)
        return (value, assign(node[1]), assign(node[2]))

    return assign(tree)


def preorder(tree):
    return [] if tree is None else [tree[0]] + preorder(tree[1]) + preorder(tree[2])


def inorder(tree):
    return [] if tree is None else inorder(tree[1]) + [tree[0]] + inorder(tree[2])


def postorder(tree):
    return [] if tree is None else postorder(tree[1]) + postorder(tree[2]) + [tree[0]]


@given(TREES.filter(lambda tree: tree is not None))
def test_constructed_tree_matches_independent_original_shape_and_calls_do_not_alias(tree):
    tree = uniquely_labeled(tree)
    arguments = [inorder(tree), postorder(tree)]
    snapshot = [array.copy() for array in arguments]
    assert evaluate(FOLDER, args=arguments) == encode(tree)
    solver = load_module(FOLDER).Solution()
    first = solver.buildTree(*arguments)
    second = solver.buildTree(*arguments)
    assert identities(first).isdisjoint(identities(second))
    assert arguments == snapshot


def test_deep_skewed_tree_is_constructed_without_recursive_calls():
    values = list(range(2500))
    arguments = [values, values[::-1]]
    expected = [0] + [item for value in values[1:] for item in (None, value)]
    assert evaluate(FOLDER, args=arguments) == expected
