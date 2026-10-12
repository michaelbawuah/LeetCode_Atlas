from itertools import product

from hypothesis import given
from hypothesis import strategies as st

from atlas.runtime import evaluate

FOLDER = "0785-is-graph-bipartite"


@st.composite
def undirected_graphs(draw):
    count = draw(st.integers(1, 8))
    adjacency = [[] for _ in range(count)]
    for first in range(count):
        for last in range(first + 1, count):
            if draw(st.booleans()):
                adjacency[first].append(last)
                adjacency[last].append(first)
    return adjacency


def any_legal_coloring(graph):
    return any(
        all(
            colors[node] != colors[neighbor]
            for node, neighbors in enumerate(graph)
            for neighbor in neighbors
        )
        for colors in product((0, 1), repeat=len(graph))
    )


@given(undirected_graphs())
def test_propagated_colors_match_exhaustive_binary_assignments(graph):
    assert evaluate(FOLDER, args=[graph]) is any_legal_coloring(graph)
