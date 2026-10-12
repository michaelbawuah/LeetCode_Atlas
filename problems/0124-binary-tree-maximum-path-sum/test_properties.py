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


FOLDER = "0124-binary-tree-maximum-path-sum"


def graph_from_tuple(tree):
    values, edges = [], []

    def visit(node, parent):
        if node is None:
            return
        index = len(values)
        values.append(node[0])
        edges.append([])
        if parent is not None:
            edges[index].append(parent)
            edges[parent].append(index)
        visit(node[1], index)
        visit(node[2], index)

    visit(tree, None)
    return values, edges


def all_endpoint_path_sums(tree):
    values, edges = graph_from_tuple(tree)
    best = max(values)
    for start in range(len(values)):
        pending = [(start, -1, values[start])]
        while pending:
            node, parent, total = pending.pop()
            best = max(best, total)
            for neighbor in edges[node]:
                if neighbor != parent:
                    pending.append((neighbor, node, total + values[neighbor]))
    return best


@given(TREES.filter(lambda tree: tree is not None))
def test_postorder_gain_matches_all_undirected_endpoint_paths(tree):
    assert evaluate(FOLDER, args=[encode(tree)]) == all_endpoint_path_sums(tree)


def test_deep_positive_chain_avoids_recursion_limit():
    chain = [1] + [item for _ in range(4999) for item in (None, 1)]
    assert evaluate(FOLDER, args=[chain]) == 5000
