from hypothesis import given, settings
from hypothesis import strategies as st

from atlas.runtime import evaluate

FOLDER = "0132-palindrome-partitioning-ii"


def oracle(text):
    best = len(text) - 1
    for mask in range(1 << (len(text) - 1)):
        parts, start = [], 0
        for end in range(1, len(text)):
            if mask & (1 << (end - 1)):
                parts.append(text[start:end])
                start = end
        parts.append(text[start:])
        if all(part == part[::-1] for part in parts):
            best = min(best, len(parts) - 1)
    return best


@settings(max_examples=60, deadline=None)
@given(st.tuples(st.text(alphabet="abc", min_size=1, max_size=9)))
def test_optimized_matches_independent_small_or_model_oracle(args):
    assert evaluate(FOLDER, args=list(args)) == oracle(*args)
