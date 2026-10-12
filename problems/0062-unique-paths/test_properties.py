from hypothesis import given, settings
from hypothesis import strategies as st

from atlas.runtime import evaluate

FOLDER = "0062-unique-paths"


def enumerate_grid_routes(rows, columns):
    if rows == 1 or columns == 1:
        return 1
    return enumerate_grid_routes(rows - 1, columns) + enumerate_grid_routes(rows, columns - 1)


@settings(max_examples=50)
@given(st.integers(1, 6), st.integers(1, 6))
def test_rolling_grid_matches_recursive_route_enumeration(rows, columns):
    assert evaluate(FOLDER, args=[rows, columns]) == enumerate_grid_routes(rows, columns)
