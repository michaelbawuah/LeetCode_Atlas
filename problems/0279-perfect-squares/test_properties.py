from math import isqrt

from hypothesis import given, settings
from hypothesis import strategies as st

from atlas.runtime import evaluate

FOLDER = "0279-perfect-squares"


def oracle(n):
    squares = [value * value for value in range(1, isqrt(n) + 1)]
    frontier, seen, distance = {0}, {0}, 0
    while n not in frontier:
        frontier = {
            total + square
            for total in frontier
            for square in squares
            if total + square <= n and total + square not in seen
        }
        seen.update(frontier)
        distance += 1
    return distance


@settings(max_examples=60, deadline=None)
@given(st.tuples(st.integers(1, 120)))
def test_optimized_matches_independent_small_or_model_oracle(args):
    assert evaluate(FOLDER, args=list(args)) == oracle(*args)
