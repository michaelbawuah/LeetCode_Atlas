from hypothesis import given
from hypothesis import strategies as st

from atlas.runtime import evaluate

FOLDER = "0787-cheapest-flights-within-k-stops"


@st.composite
def flight_cases(draw):
    count = draw(st.integers(2, 6))
    pairs = [(a, b) for a in range(count) for b in range(count) if a != b]
    selected = draw(
        st.lists(st.sampled_from(pairs), min_size=1, max_size=min(12, len(pairs)), unique=True)
    )
    prices = draw(st.lists(st.integers(1, 30), min_size=len(selected), max_size=len(selected)))
    flights = [[a, b, price] for (a, b), price in zip(selected, prices, strict=True)]
    source, target = draw(st.lists(st.integers(0, count - 1), min_size=2, max_size=2, unique=True))
    return count, flights, source, target, draw(st.integers(0, count - 1))


def enumerate_bounded_paths(count, flights, source, target, stops):
    adjacency = [[] for _ in range(count)]
    for first, last, price in flights:
        adjacency[first].append((last, price))
    best = float("inf")

    def visit(node, remaining, price):
        nonlocal best
        if node == target:
            best = min(best, price)
        if remaining:
            for neighbor, cost in adjacency[node]:
                visit(neighbor, remaining - 1, price + cost)

    visit(source, stops + 1, 0)
    return -1 if best == float("inf") else best


@given(flight_cases())
def test_layered_relaxation_matches_every_bounded_walk(case):
    assert evaluate(FOLDER, args=list(case)) == enumerate_bounded_paths(*case)
