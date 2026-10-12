from itertools import combinations

from hypothesis import given
from hypothesis import strategies as st

from atlas.runtime import evaluate

FOLDER = "0684-redundant-connection"


@st.composite
def tree_plus_edge(draw):
    count = draw(st.integers(3, 7))
    tree = [(draw(st.integers(1, node - 1)), node) for node in range(2, count + 1)]
    available = [edge for edge in combinations(range(1, count + 1), 2) if edge not in tree]
    edges = tree + [draw(st.sampled_from(available))]
    return [list(edge) for edge in draw(st.permutations(edges))]


def latest_connected_removal(edges):
    count = len(edges)
    for removed in range(count - 1, -1, -1):
        adjacency = [[] for _ in range(count + 1)]
        for index, (first, second) in enumerate(edges):
            if index != removed:
                adjacency[first].append(second)
                adjacency[second].append(first)
        seen, pending = {1}, [1]
        while pending:
            for neighbor in adjacency[pending.pop()]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    pending.append(neighbor)
        if len(seen) == count:
            return edges[removed]
    raise AssertionError("Generator must create a connected tree plus one extra edge")


@given(tree_plus_edge())
def test_union_find_matches_latest_edge_whose_removal_restores_a_tree(edges):
    assert evaluate(FOLDER, args=[edges]) == latest_connected_removal(edges)
