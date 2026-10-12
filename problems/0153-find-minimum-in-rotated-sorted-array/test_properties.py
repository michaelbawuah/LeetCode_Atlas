from hypothesis import given
from hypothesis import strategies as st

from atlas.runtime import evaluate

FOLDER = "0153-find-minimum-in-rotated-sorted-array"


@given(
    st.lists(st.integers(-5000, 5000), min_size=1, max_size=80, unique=True),
    st.integers(min_value=0, max_value=10000),
)
def test_rotations_match_linear_scan(values, rotation):
    ordered = sorted(values)
    pivot = rotation % len(ordered)
    rotated = ordered[pivot:] + ordered[:pivot]
    assert evaluate(FOLDER, args=[rotated]) == min(rotated)
