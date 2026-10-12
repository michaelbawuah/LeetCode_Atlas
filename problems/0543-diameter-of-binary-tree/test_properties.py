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


FOLDER = "0543-diameter-of-binary-tree"


def adjacency(tree):
    edges = []

    def visit(node, parent):
        if node is None:
            return
        index = len(edges)
        edges.append([])
        if parent is not None:
            edges[index].append(parent)
            edges[parent].append(index)
        visit(node[1], index)
        visit(node[2], index)

    visit(tree, None)
    return edges


def all_pair_distances(tree):
    edges = adjacency(tree)
    answer = 0
    for start in range(len(edges)):
        pending = deque([(start, -1, 0)])
        while pending:
            node, parent, distance = pending.popleft()
            answer = max(answer, distance)
            for neighbor in edges[node]:
                if neighbor != parent:
                    pending.append((neighbor, node, distance + 1))
    return answer


@given(TREES.filter(lambda tree: tree is not None))
def test_cached_heights_match_all_pair_bfs_distances(tree):
    assert evaluate(FOLDER, args=[encode(tree)]) == all_pair_distances(tree)


def test_deep_chain_diameter_counts_edges():
    chain = [0] + [item for _ in range(3999) for item in (None, 0)]
    assert evaluate(FOLDER, args=[chain]) == 3999
