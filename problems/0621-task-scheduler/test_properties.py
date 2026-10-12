from collections import Counter
from functools import lru_cache

from hypothesis import given
from hypothesis import strategies as st

from atlas.runtime import evaluate

FOLDER = "0621-task-scheduler"


def exhaustive_schedule(tasks, cooldown):
    initial = tuple(Counter(tasks).values())

    @lru_cache(None)
    def finish(remaining, waits):
        if not any(remaining):
            return 0
        alternatives = []
        decremented = tuple(max(0, wait - 1) for wait in waits)
        for index, count in enumerate(remaining):
            if count and waits[index] == 0:
                next_counts = list(remaining)
                next_counts[index] -= 1
                next_waits = list(decremented)
                next_waits[index] = cooldown
                alternatives.append(1 + finish(tuple(next_counts), tuple(next_waits)))
        if any(count and wait for count, wait in zip(remaining, waits, strict=True)):
            alternatives.append(1 + finish(remaining, decremented))
        return min(alternatives)

    return finish(initial, (0,) * len(initial))


@given(st.lists(st.sampled_from("ABC"), min_size=1, max_size=7), st.integers(0, 3))
def test_frame_formula_matches_exhaustive_task_and_idle_choices(tasks, cooldown):
    assert evaluate(FOLDER, args=[tasks, cooldown]) == exhaustive_schedule(tasks, cooldown)
