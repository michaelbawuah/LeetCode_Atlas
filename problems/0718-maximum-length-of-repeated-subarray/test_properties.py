from hypothesis import given, settings
from hypothesis import strategies as st

from atlas.runtime import evaluate

FOLDER = "0718-maximum-length-of-repeated-subarray"


def oracle(first, second):
    pieces = {
        tuple(second[start:end])
        for start in range(len(second))
        for end in range(start + 1, len(second) + 1)
    }
    return max(
        (
            end - start
            for start in range(len(first))
            for end in range(start + 1, len(first) + 1)
            if tuple(first[start:end]) in pieces
        ),
        default=0,
    )


@settings(max_examples=60, deadline=None)
@given(
    st.tuples(
        st.lists(st.integers(0, 8), min_size=1, max_size=10),
        st.lists(st.integers(0, 8), min_size=1, max_size=10),
    )
)
def test_optimized_matches_independent_small_or_model_oracle(args):
    assert evaluate(FOLDER, args=list(args)) == oracle(*args)
