from hypothesis import given
from hypothesis import strategies as st

from atlas.runtime import load_module

Solution = load_module("0649-dota2-senate").Solution


def round_reference(senate):
    active = list(senate)
    bans = {"R": 0, "D": 0}
    while len(set(active)) > 1:
        survivors = []
        for party in active:
            if bans[party]:
                bans[party] -= 1
            else:
                bans["D" if party == "R" else "R"] += 1
                survivors.append(party)
        active = survivors
    return "Radiant" if active[0] == "R" else "Dire"


@given(st.text(alphabet="RD", min_size=1, max_size=30))
def test_turn_queues_match_round_and_pending_ban_simulation(senate):
    assert Solution().predictPartyVictory(senate) == round_reference(senate)
