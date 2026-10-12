from hypothesis import given
from hypothesis import strategies as st

from atlas.runtime import load_module

Solution = load_module("0228-summary-ranges").Solution


@given(st.lists(st.integers(-100, 100), max_size=20, unique=True))
def test_ranges_decode_to_exact_input_and_cannot_be_joined(values):
    nums = sorted(values)
    result = Solution().summaryRanges(nums)
    decoded, intervals = [], []
    for text in result:
        if "->" in text:
            start, end = map(int, text.split("->"))
            assert start < end
        else:
            start = end = int(text)
        intervals.append((start, end))
        decoded.extend(range(start, end + 1))
    assert decoded == nums
    assert all(intervals[i - 1][1] + 1 < intervals[i][0] for i in range(1, len(intervals)))
