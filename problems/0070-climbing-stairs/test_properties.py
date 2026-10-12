from hypothesis import given, settings
from hypothesis import strategies as st

from atlas.runtime import evaluate

FOLDER = "0070-climbing-stairs"


def enumerate_step_sequences(remaining):
    if remaining == 0:
        return 1
    if remaining < 0:
        return 0
    return enumerate_step_sequences(remaining - 1) + enumerate_step_sequences(remaining - 2)


@settings(max_examples=50)
@given(st.integers(1, 16))
def test_rolling_count_matches_step_sequence_enumeration(n):
    assert evaluate(FOLDER, args=[n]) == enumerate_step_sequences(n)
