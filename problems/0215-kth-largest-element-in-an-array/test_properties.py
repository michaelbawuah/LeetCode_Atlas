from hypothesis import given
from hypothesis import strategies as st

from atlas.runtime import load_module

Solution = load_module("0215-kth-largest-element-in-an-array").Solution


@given(values=st.lists(st.integers(-10000, 10000), min_size=1, max_size=35))
def test_all_ranks_match_sorting(values):
    ordered = sorted(values, reverse=True)
    snapshot = list(values)
    for rank, expected in enumerate(ordered, start=1):
        assert Solution().findKthLargest(values, rank) == expected
    assert values == snapshot
