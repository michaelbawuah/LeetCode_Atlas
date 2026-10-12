from hypothesis import given
from hypothesis import strategies as st

from atlas.runtime import load_module

Solution = load_module("0268-missing-number").Solution


@given(st.integers(1, 35), st.data())
def test_matches_arithmetic_difference_under_permutation(size, data):
    missing = data.draw(st.integers(0, size))
    nums = [value for value in range(size + 1) if value != missing]
    nums = list(data.draw(st.permutations(nums)))
    expected = size * (size + 1) // 2 - sum(nums)
    assert expected == missing
    assert Solution().missingNumber(nums) == expected


def test_zero_can_be_missing():
    assert Solution().missingNumber([1, 2, 3]) == 0
