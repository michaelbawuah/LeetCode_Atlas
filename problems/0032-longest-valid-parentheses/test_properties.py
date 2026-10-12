from hypothesis import given, settings
from hypothesis import strategies as st

from atlas.runtime import evaluate

FOLDER = "0032-longest-valid-parentheses"


def oracle(text):
    best = 0
    for start in range(len(text)):
        balance = 0
        for end in range(start, len(text)):
            balance += 1 if text[end] == "(" else -1
            if balance < 0:
                break
            if balance == 0:
                best = max(best, end - start + 1)
    return best


@settings(max_examples=60, deadline=None)
@given(st.tuples(st.text(alphabet="()", max_size=16)))
def test_optimized_matches_independent_small_or_model_oracle(args):
    assert evaluate(FOLDER, args=list(args)) == oracle(*args)
