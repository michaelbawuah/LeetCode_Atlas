from collections import deque

from hypothesis import assume, given
from hypothesis import strategies as st

from atlas.runtime import evaluate

FOLDER = "0045-jump-game-ii"


def explicit_index_bfs(nums):
    pending = deque([(0, 0)])
    seen = {0}
    while pending:
        index, distance = pending.popleft()
        if index == len(nums) - 1:
            return distance
        for neighbor in range(index + 1, min(len(nums), index + nums[index] + 1)):
            if neighbor not in seen:
                seen.add(neighbor)
                pending.append((neighbor, distance + 1))
    return None


@given(st.lists(st.integers(0, 8), min_size=1, max_size=18))
def test_greedy_layers_match_explicit_shortest_path_bfs(nums):
    expected = explicit_index_bfs(nums)
    assume(expected is not None)
    assert evaluate(FOLDER, args=[nums]) == expected
