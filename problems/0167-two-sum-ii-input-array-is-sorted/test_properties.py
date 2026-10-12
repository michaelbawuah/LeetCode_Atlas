from itertools import combinations

from hypothesis import assume, given
from hypothesis import strategies as st

from atlas.runtime import load_module

Solution = load_module("0167-two-sum-ii-input-array-is-sorted").Solution


@given(st.lists(st.integers(-100, 100), min_size=2, max_size=12), st.data())
def test_matches_unique_pair_enumeration(values, data):
    numbers = sorted(values)
    first, second = data.draw(st.sampled_from(list(combinations(range(len(numbers)), 2))))
    target = numbers[first] + numbers[second]
    witnesses = [
        [left + 1, right + 1]
        for left, right in combinations(range(len(numbers)), 2)
        if numbers[left] + numbers[right] == target
    ]
    assume(len(witnesses) == 1)
    assert Solution().twoSum(numbers, target) == witnesses[0]


def test_equal_values_still_require_different_positions():
    assert Solution().twoSum([3, 3], 6) == [1, 2]
