from collections import Counter

from hypothesis import given
from hypothesis import strategies as st

from atlas.runtime import load_module

Solution = load_module("0080-remove-duplicates-from-sorted-array-ii").Solution


@given(st.lists(st.integers(-100, 100), min_size=1, max_size=60))
def test_returned_count_and_mutated_prefix_keep_at_most_two_copies(values):
    nums = sorted(values)
    counts = Counter(values)
    expected = [value for value in sorted(counts) for _ in range(min(2, counts[value]))]
    identity = id(nums)
    count = Solution().removeDuplicates(nums)
    assert type(count) is int and count == len(expected)
    assert nums[:count] == expected
    assert id(nums) == identity and len(nums) == len(values)
