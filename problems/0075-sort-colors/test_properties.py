from hypothesis import given
from hypothesis import strategies as st

from atlas.runtime import load_module

Solution = load_module("0075-sort-colors").Solution


@given(st.lists(st.integers(0, 2), min_size=1, max_size=80))
def test_partition_matches_sort_without_replacing_the_list(nums):
    expected = sorted(nums)
    identity = id(nums)
    assert Solution().sortColors(nums) is None
    assert nums == expected
    assert id(nums) == identity
