from hypothesis import given
from hypothesis import strategies as st

from atlas.runtime import load_module

Solution = load_module("0026-remove-duplicates-from-sorted-array").Solution


@given(st.lists(st.integers(-100, 100), min_size=1, max_size=60))
def test_returned_length_and_mutated_prefix_are_both_correct(values):
    nums = sorted(values)
    expected = sorted(set(values))
    identity = id(nums)
    count = Solution().removeDuplicates(nums)
    assert type(count) is int
    assert count == len(expected)
    assert nums[:count] == expected
    assert len(nums) == len(values) and id(nums) == identity
