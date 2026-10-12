from hypothesis import given
from hypothesis import strategies as st

from atlas.runtime import evaluate

FOLDER = "0743-network-delay-time"


@st.composite
def networks(draw):
    count = draw(st.integers(2, 7))
    pairs = [(a, b) for a in range(1, count + 1) for b in range(1, count + 1) if a != b]
    selected = draw(
        st.lists(st.sampled_from(pairs), min_size=1, max_size=min(20, len(pairs)), unique=True)
    )
    weights = draw(st.lists(st.integers(0, 100), min_size=len(selected), max_size=len(selected)))
    edges = [[a, b, weight] for (a, b), weight in zip(selected, weights, strict=True)]
    return edges, count, draw(st.integers(1, count))


def floyd_delay(edges, count, source):
    distances = [[0 if i == j else float("inf") for j in range(count)] for i in range(count)]
    for first, last, weight in edges:
        distances[first - 1][last - 1] = weight
    for via in range(count):
        for first in range(count):
            for last in range(count):
                distances[first][last] = min(
                    distances[first][last], distances[first][via] + distances[via][last]
                )
    answer = max(distances[source - 1])
    return -1 if answer == float("inf") else answer


@given(networks())
def test_dijkstra_matches_floyd_warshall(case):
    assert evaluate(FOLDER, args=list(case)) == floyd_delay(*case)
