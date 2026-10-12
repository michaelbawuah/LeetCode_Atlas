from hypothesis import given
from hypothesis import strategies as st

from atlas.runtime import evaluate

FOLDER = "0055-jump-game"


def reachable_positions(nums):
    reachable = [True] + [False] * (len(nums) - 1)
    for index in range(len(nums)):
        if reachable[index]:
            for neighbor in range(index + 1, min(len(nums), index + nums[index] + 1)):
                reachable[neighbor] = True
    return reachable[-1]


@given(st.lists(st.integers(0, 10), min_size=1, max_size=25))
def test_farthest_prefix_matches_explicit_reachability_table(nums):
    assert evaluate(FOLDER, args=[nums]) is reachable_positions(nums)
