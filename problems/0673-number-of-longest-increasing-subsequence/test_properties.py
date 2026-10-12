from hypothesis import given, settings
from hypothesis import strategies as st

from atlas.runtime import evaluate

FOLDER = "0673-number-of-longest-increasing-subsequence"


def oracle(values):
    longest, count = 0, 0
    for mask in range(1, 1 << len(values)):
        selected = [value for index, value in enumerate(values) if mask & (1 << index)]
        if all(first < second for first, second in zip(selected, selected[1:], strict=False)):
            if len(selected) > longest:
                longest, count = len(selected), 1
            elif len(selected) == longest:
                count += 1
    return count


@settings(max_examples=60, deadline=None)
@given(st.tuples(st.lists(st.integers(-10, 10), min_size=1, max_size=12)))
def test_optimized_matches_independent_small_or_model_oracle(args):
    assert evaluate(FOLDER, args=list(args)) == oracle(*args)
