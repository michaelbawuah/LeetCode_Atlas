from itertools import combinations

from hypothesis import given
from hypothesis import strategies as st

from atlas.runtime import evaluate

FOLDER = "1584-min-cost-to-connect-all-points"


def exhaustive_spanning_trees(points):
    count = len(points)
    edges = list(combinations(range(count), 2))
    best = float("inf")
    for selected in combinations(edges, count - 1):
        adjacency = [[] for _ in points]
        cost = 0
        for first, last in selected:
            adjacency[first].append(last)
            adjacency[last].append(first)
            cost += abs(points[first][0] - points[last][0]) + abs(
                points[first][1] - points[last][1]
            )
        seen, pending = {0}, [0]
        while pending:
            for neighbor in adjacency[pending.pop()]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    pending.append(neighbor)
        if len(seen) == count:
            best = min(best, cost)
    return best


@given(
    st.lists(
        st.tuples(st.integers(-10, 10), st.integers(-10, 10)), min_size=1, max_size=5, unique=True
    )
)
def test_dense_prim_matches_exhaustive_spanning_tree_edge_sets(points):
    assert evaluate(FOLDER, args=[points]) == exhaustive_spanning_trees(points)
