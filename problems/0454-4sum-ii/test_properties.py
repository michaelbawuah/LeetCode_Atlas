from itertools import product

from hypothesis import given
from hypothesis import strategies as st

from atlas.runtime import load_module

Solution = load_module("0454-4sum-ii").Solution


@given(st.integers(1, 6), st.data())
def test_pair_counts_match_all_four_index_combinations(size, data):
    arrays = [
        data.draw(st.lists(st.integers(-6, 6), min_size=size, max_size=size)) for _ in range(4)
    ]
    expected = sum(sum(values) == 0 for values in product(*arrays))
    assert Solution().fourSumCount(*arrays) == expected
