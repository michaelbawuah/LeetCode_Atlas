from hypothesis import given
from hypothesis import strategies as st

from atlas.runtime import load_module

Solution = load_module("0217-contains-duplicate").Solution


@given(st.lists(st.integers(-30, 30), min_size=1, max_size=25))
def test_matches_pairwise_comparison(nums):
    expected = any(nums[i] == nums[j] for i in range(len(nums)) for j in range(i + 1, len(nums)))
    assert Solution().containsDuplicate(nums) == expected


@given(st.lists(st.integers(), min_size=1, max_size=20, unique=True))
def test_appending_an_existing_value_creates_a_duplicate(nums):
    assert not Solution().containsDuplicate(nums)
    assert Solution().containsDuplicate(nums + [nums[0]])
