from functools import lru_cache

from hypothesis import given
from hypothesis import strategies as st

from atlas.runtime import load_module

Solution = load_module("0881-boats-to-save-people").Solution


@given(st.integers(1, 20), st.data())
def test_greedy_pairing_matches_all_legal_boat_pairings(limit, data):
    people = data.draw(st.lists(st.integers(1, limit), min_size=1, max_size=9))

    @lru_cache(None)
    def solve(mask):
        if mask == 0:
            return 0
        first = next(index for index in range(len(people)) if mask & (1 << index))
        remaining = mask ^ (1 << first)
        best = 1 + solve(remaining)
        for partner in range(first + 1, len(people)):
            if remaining & (1 << partner) and people[first] + people[partner] <= limit:
                best = min(best, 1 + solve(remaining ^ (1 << partner)))
        return best

    assert Solution().numRescueBoats(people, limit) == solve((1 << len(people)) - 1)
