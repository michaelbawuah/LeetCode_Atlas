from itertools import combinations

from hypothesis import given
from hypothesis import strategies as st

from atlas.runtime import load_module

Solution = load_module("0018-4sum").Solution


@given(st.lists(st.integers(-6, 6), min_size=1, max_size=11), st.integers(-15, 15))
def test_matches_exhaustive_distinct_index_quadruplets(nums, target):
    expected = {tuple(sorted(group)) for group in combinations(nums, 4) if sum(group) == target}
    answer = Solution().fourSum(nums, target)
    actual = {tuple(sorted(group)) for group in answer}
    assert actual == expected
    assert len(actual) == len(answer)


def test_sum_uses_values_wider_than_a_signed_32_bit_intermediate():
    assert Solution().fourSum([1000000000] * 4, -294967296) == []
