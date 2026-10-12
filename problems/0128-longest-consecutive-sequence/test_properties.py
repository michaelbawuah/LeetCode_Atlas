from hypothesis import given
from hypothesis import strategies as st

from atlas.runtime import load_module

Solution = load_module("0128-longest-consecutive-sequence").Solution


def sorting_oracle(nums):
    best = run = 0
    previous = None
    for value in sorted(nums):
        if value == previous:
            continue
        run = run + 1 if previous is not None and value == previous + 1 else 1
        best = max(best, run)
        previous = value
    return best


@given(st.lists(st.integers(-20, 20), max_size=35))
def test_matches_sorted_run_scan(nums):
    assert Solution().longestConsecutive(nums) == sorting_oracle(nums)


@given(st.lists(st.integers(-20, 20), max_size=35), st.integers(-100, 100))
def test_translation_and_duplicate_insertion_preserve_length(nums, offset):
    expected = Solution().longestConsecutive(nums)
    assert Solution().longestConsecutive([value + offset for value in nums]) == expected
    assert Solution().longestConsecutive(nums + nums) == expected
