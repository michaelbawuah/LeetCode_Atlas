from hypothesis import given, settings
from hypothesis import strategies as st

from atlas.runtime import evaluate

FOLDER = "0583-delete-operation-for-two-strings"


def subsequences(sequence):
    return {
        tuple(value for index, value in enumerate(sequence) if mask & (1 << index))
        for mask in range(1 << len(sequence))
    }


def oracle(first, second):
    kept = max(map(len, subsequences(first) & subsequences(second)))
    return len(first) + len(second) - 2 * kept


@settings(max_examples=60, deadline=None)
@given(
    st.tuples(
        st.text(alphabet="abc", min_size=1, max_size=7),
        st.text(alphabet="abc", min_size=1, max_size=7),
    )
)
def test_optimized_matches_independent_small_or_model_oracle(args):
    assert evaluate(FOLDER, args=list(args)) == oracle(*args)
