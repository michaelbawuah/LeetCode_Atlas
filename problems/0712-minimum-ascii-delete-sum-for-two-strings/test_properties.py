from hypothesis import given, settings
from hypothesis import strategies as st

from atlas.runtime import evaluate

FOLDER = "0712-minimum-ascii-delete-sum-for-two-strings"


def subsequences(sequence):
    return {
        tuple(value for index, value in enumerate(sequence) if mask & (1 << index))
        for mask in range(1 << len(sequence))
    }


def oracle(first, second):
    kept = max(sum(map(ord, common)) for common in subsequences(first) & subsequences(second))
    return sum(map(ord, first + second)) - 2 * kept


@settings(max_examples=60, deadline=None)
@given(
    st.tuples(
        st.text(alphabet="abcd", min_size=1, max_size=6),
        st.text(alphabet="abcd", min_size=1, max_size=6),
    )
)
def test_optimized_matches_independent_small_or_model_oracle(args):
    assert evaluate(FOLDER, args=list(args)) == oracle(*args)
