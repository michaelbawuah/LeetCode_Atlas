from itertools import permutations

from hypothesis import given
from hypothesis import strategies as st

from atlas.runtime import load_module

Solution = load_module("0179-largest-number").Solution


@given(st.lists(st.integers(0, 99), min_size=1, max_size=6))
def test_custom_comparator_matches_every_possible_concatenation(nums):
    expected = max("".join(map(str, order)) for order in permutations(nums))
    expected = expected.lstrip("0") or "0"
    assert Solution().largestNumber(nums) == expected
