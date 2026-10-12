from hypothesis import given, settings
from hypothesis import strategies as st

from atlas.runtime import evaluate

FOLDER = "0790-domino-and-tromino-tiling"


def oracle(n):
    placements = [(3, 0), (1, 1), (2, 2)]
    for missing in range(4):
        mask = 15 ^ (1 << missing)
        placements.append((mask & 3, mask >> 2))
    transitions = []
    for occupied in range(4):
        outcomes = {}

        def fill(current, following, outcomes=outcomes):
            if current == 3:
                outcomes[following] = outcomes.get(following, 0) + 1
                return
            first_free = 1 if not current & 1 else 2
            for here, there in placements:
                if here & first_free and not here & current and not there & following:
                    fill(current | here, following | there)

        fill(occupied, 0)
        transitions.append(outcomes)
    counts = [1, 0, 0, 0]
    for _ in range(n):
        following = [0] * 4
        for state, count in enumerate(counts):
            for next_state, multiplicity in transitions[state].items():
                following[next_state] += count * multiplicity
        counts = [count % 1_000_000_007 for count in following]
    return counts[0]


@settings(max_examples=60, deadline=None)
@given(st.tuples(st.integers(1, 1000)))
def test_optimized_matches_independent_small_or_model_oracle(args):
    assert evaluate(FOLDER, args=list(args)) == oracle(*args)
