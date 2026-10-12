from hypothesis import given
from hypothesis import strategies as st

from atlas.runtime import load_module

MedianFinder = load_module("0295-find-median-from-data-stream").MedianFinder


@given(st.lists(st.integers(-100000, 100000), min_size=1, max_size=80))
def test_every_prefix_median_matches_sorted_values(values):
    finder = MedianFinder()
    observed = []
    for value in values:
        assert finder.addNum(value) is None
        observed.append(value)
        ordered = sorted(observed)
        middle = len(ordered) // 2
        expected = (
            float(ordered[middle])
            if len(ordered) % 2
            else (ordered[middle - 1] + ordered[middle]) / 2.0
        )
        actual = finder.findMedian()
        assert isinstance(actual, float)
        assert actual == expected
        assert finder.findMedian() == expected
