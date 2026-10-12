from functools import lru_cache
from itertools import combinations

from hypothesis import given
from hypothesis import strategies as st

from atlas.runtime import evaluate

FOLDER = "0846-hand-of-straights"


def exhaustive_groups(hand, group_size):
    if len(hand) % group_size:
        return False

    @lru_cache(None)
    def partition(remaining):
        if not remaining:
            return True
        for indices in combinations(range(len(remaining)), group_size):
            if 0 not in indices:
                continue
            values = sorted(remaining[index] for index in indices)
            if all(last == first + 1 for first, last in zip(values, values[1:], strict=False)):
                kept = tuple(value for index, value in enumerate(remaining) if index not in indices)
                if partition(kept):
                    return True
        return False

    return partition(tuple(hand))


@given(st.lists(st.integers(1, 8), min_size=1, max_size=8), st.data())
def test_greedy_multiplicity_consumption_matches_exhaustive_card_groups(hand, data):
    group_size = data.draw(st.integers(1, len(hand)), label="group size")
    assert evaluate(FOLDER, args=[hand, group_size]) is exhaustive_groups(hand, group_size)
