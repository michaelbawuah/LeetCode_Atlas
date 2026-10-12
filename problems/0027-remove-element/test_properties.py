from hypothesis import given
from hypothesis import strategies as st

from atlas.runtime import load_module

Solution = load_module("0027-remove-element").Solution


@given(st.lists(st.integers(0, 50), max_size=100), st.integers(0, 100))
def test_returned_length_and_mutated_prefix_preserve_exact_multiplicity(values, target):
    nums = values.copy()
    expected = [value for value in values if value != target]
    identity = id(nums)
    count = Solution().removeElement(nums, target)
    assert type(count) is int and count == len(expected)
    assert sorted(nums[:count]) == sorted(expected)
    assert target not in nums[:count]
    assert id(nums) == identity and len(nums) == len(values)
