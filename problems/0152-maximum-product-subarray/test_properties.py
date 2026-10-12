from math import prod

from hypothesis import given
from hypothesis import strategies as st

from atlas.runtime import load_module

Solution = load_module("0152-maximum-product-subarray").Solution


@given(st.lists(st.integers(-3, 3), min_size=1, max_size=9))
def test_matches_products_of_every_nonempty_slice(nums):
    expected = max(
        prod(nums[left:right])
        for left in range(len(nums))
        for right in range(left + 1, len(nums) + 1)
    )
    assert Solution().maxProduct(nums) == expected


@given(st.lists(st.integers(1, 3), min_size=1, max_size=10))
def test_all_positive_factors_make_the_entire_product_optimal(nums):
    assert Solution().maxProduct(nums) == prod(nums)
