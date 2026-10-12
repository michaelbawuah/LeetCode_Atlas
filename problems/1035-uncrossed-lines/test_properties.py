from hypothesis import given, settings
from hypothesis import strategies as st

from atlas.runtime import evaluate

FOLDER = "1035-uncrossed-lines"


def subsequences(sequence):
    return {
        tuple(value for index, value in enumerate(sequence) if mask & (1 << index))
        for mask in range(1 << len(sequence))
    }


def oracle(first, second):
    return max(map(len, subsequences(first) & subsequences(second)))


@settings(max_examples=60, deadline=None)
@given(
    st.tuples(
        st.lists(st.integers(1, 8), min_size=1, max_size=8),
        st.lists(st.integers(1, 8), min_size=1, max_size=8),
    )
)
def test_optimized_matches_independent_small_or_model_oracle(args):
    assert evaluate(FOLDER, args=list(args)) == oracle(*args)
