from math import prod

from hypothesis import given
from hypothesis import strategies as st

from atlas.runtime import load_module

Solution = load_module("0238-product-of-array-except-self").Solution


@given(st.lists(st.integers(-3, 3), min_size=2, max_size=10))
def test_matches_independent_multiplication(nums):
    expected = [prod(nums[:index] + nums[index + 1 :]) for index in range(len(nums))]
    assert Solution().productExceptSelf(nums) == expected


@given(st.lists(st.integers(-3, 3), min_size=2, max_size=10))
def test_reversal_reverses_the_answer(nums):
    assert Solution().productExceptSelf(nums[::-1]) == Solution().productExceptSelf(nums)[::-1]
