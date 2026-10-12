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


FOLDER = "0235-lowest-common-ancestor-of-a-binary-search-tree"


def original_paths(root):
    output = {}

    def visit(node, path):
        if node is None:
            return
        current = path + [node]
        output[node.val] = current
        visit(node.left, current)
        visit(node.right, current)

    visit(root, [])
    return output


def common_prefix_node(first, second):
    answer = None
    for left, right in zip(first, second, strict=False):
        if left is not right:
            break
        answer = left
    return answer


@given(st.lists(st.integers(-100, 100), min_size=2, max_size=35, unique=True), st.data())
def test_lca_is_exact_original_common_prefix_node_and_leaves_tree_unchanged(values, data):
    tree = bst(values)
    root = build_tree(encode(tree))
    paths = original_paths(root)
    pval, qval = data.draw(
        st.lists(st.sampled_from(list(paths)), min_size=2, max_size=2, unique=True)
    )
    p, q = paths[pval][-1], paths[qval][-1]
    expected = common_prefix_node(paths[pval], paths[qval])
    before = snapshot(root)
    result = load_module(FOLDER).Solution().lowestCommonAncestor(root, p, q)
    assert result is expected
    assert snapshot(root) == before
    assert evaluate(FOLDER, args=[encode(tree), pval, qval]) == expected.val


def test_deep_chain_keeps_original_target_as_ancestor_without_recursion():
    tree = [0] + [item for value in range(1, 3000) for item in (None, value)]
    assert evaluate(FOLDER, args=[tree, 1499, 2999]) == 1499
