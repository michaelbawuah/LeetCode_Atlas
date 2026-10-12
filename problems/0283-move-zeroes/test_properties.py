from hypothesis import given
from hypothesis import strategies as st

from atlas.runtime import load_module

Solution = load_module("0283-move-zeroes").Solution


@given(st.lists(st.integers(-5, 5), min_size=1, max_size=50))
def test_in_place_stable_partition_matches_filtering(nums):
    original = nums.copy()
    identity = id(nums)
    expected = [value for value in original if value != 0] + [0] * original.count(0)
    returned = Solution().moveZeroes(nums)
    assert returned is None
    assert id(nums) == identity
    assert nums == expected
    assert len(nums) == len(original)


@given(st.lists(st.integers(-5, 5), min_size=1, max_size=50))
def test_second_pass_does_not_change_the_result(nums):
    Solution().moveZeroes(nums)
    expected = nums.copy()
    Solution().moveZeroes(nums)
    assert nums == expected
