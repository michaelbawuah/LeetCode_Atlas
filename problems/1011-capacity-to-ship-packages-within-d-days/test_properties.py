from itertools import combinations

from hypothesis import given
from hypothesis import strategies as st

from atlas.runtime import load_module

Solution = load_module("1011-capacity-to-ship-packages-within-d-days").Solution


@given(st.lists(st.integers(1, 20), min_size=1, max_size=9), st.data())
def test_capacity_search_matches_every_order_preserving_partition(weights, data):
    days = data.draw(st.integers(1, len(weights)))
    best = sum(weights)
    for parts in range(1, days + 1):
        for cuts in combinations(range(1, len(weights)), parts - 1):
            boundaries = (0, *cuts, len(weights))
            capacity = max(
                sum(weights[left:right])
                for left, right in zip(boundaries, boundaries[1:], strict=False)
            )
            best = min(best, capacity)
    assert Solution().shipWithinDays(weights, days) == best
