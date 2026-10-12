from hypothesis import given
from hypothesis import strategies as st

from atlas.runtime import load_module

FOLDER = "0133-clone-graph"


class ReferenceNode:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = [] if neighbors is None else neighbors


@st.composite
def connected_adjacency(draw):
    count = draw(st.integers(0, 8))
    if count == 0:
        return []
    edges = {(draw(st.integers(1, node - 1)), node) for node in range(2, count + 1)}
    optional = [
        (a, b) for a in range(1, count + 1) for b in range(a + 1, count + 1) if (a, b) not in edges
    ]
    if optional:
        edges.update(draw(st.lists(st.sampled_from(optional), unique=True, max_size=len(optional))))
    adjacency = [[] for _ in range(count)]
    for first, second in sorted(edges):
        adjacency[first - 1].append(second)
        adjacency[second - 1].append(first)
    return adjacency


@given(connected_adjacency())
def test_clone_has_independent_nodes_and_neighbor_lists_with_identical_edges(adjacency):
    module = load_module(FOLDER)
    module.Node = ReferenceNode
    originals = {value: ReferenceNode(value) for value in range(1, len(adjacency) + 1)}
    for value, neighbors in enumerate(adjacency, 1):
        originals[value].neighbors = [originals[neighbor] for neighbor in neighbors]
    clone = module.Solution().cloneGraph(originals.get(1))
    if not originals:
        assert clone is None
        return
    copies, pending = {}, [clone]
    while pending:
        current = pending.pop()
        if current.val in copies:
            assert copies[current.val] is current
            continue
        copies[current.val] = current
        pending.extend(current.neighbors)
    assert set(copies) == set(originals)
    assert {id(node) for node in copies.values()}.isdisjoint(
        id(node) for node in originals.values()
    )
    for value in originals:
        assert copies[value].neighbors is not originals[value].neighbors
        assert sorted(neighbor.val for neighbor in copies[value].neighbors) == adjacency[value - 1]
        assert all(neighbor is copies[neighbor.val] for neighbor in copies[value].neighbors)
    original_edges = [list(node.neighbors) for node in originals.values()]
    clone.neighbors.clear()
    clone.val = -1
    assert [node.val for node in originals.values()] == list(range(1, len(adjacency) + 1))
    assert [node.neighbors for node in originals.values()] == original_edges
