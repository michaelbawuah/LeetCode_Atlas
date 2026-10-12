from collections import Counter

from hypothesis import given
from hypothesis import strategies as st

from atlas.runtime import load_module

Solution = load_module("0136-single-number").Solution


@given(st.lists(st.integers(-100, 100), min_size=1, max_size=10, unique=True), st.data())
def test_matches_occurrence_count_for_valid_pairs(values, data):
    singleton = data.draw(st.sampled_from(values))
    nums = [singleton] + [value for value in values if value != singleton for _ in range(2)]
    nums = list(data.draw(st.permutations(nums)))
    expected = next(value for value, count in Counter(nums).items() if count == 1)
    assert Solution().singleNumber(nums) == expected
    assert Solution().singleNumber(nums + [500, 500]) == expected


def test_signed_xor_cancellation():
    assert Solution().singleNumber([-8, -3, -8]) == -3
