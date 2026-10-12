from itertools import combinations

from hypothesis import given
from hypothesis import strategies as st

from atlas.runtime import load_module

Solution = load_module("1482-minimum-number-of-days-to-make-m-bouquets").Solution


@given(st.lists(st.integers(1, 20), min_size=1, max_size=9), st.integers(1, 5), st.data())
def test_day_search_matches_enumerated_disjoint_bouquet_positions(bloom, count, data):
    width = data.draw(st.integers(1, len(bloom)))
    expected = -1
    for day in sorted(set(bloom)):
        starts = [
            start
            for start in range(len(bloom) - width + 1)
            if max(bloom[start : start + width]) <= day
        ]
        if any(
            all(a + width <= b for a, b in zip(chosen, chosen[1:], strict=False))
            for chosen in combinations(starts, count)
        ):
            expected = day
            break
    assert Solution().minDays(bloom, count, width) == expected
