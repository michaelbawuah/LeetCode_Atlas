from hypothesis import given, settings
from hypothesis import strategies as st

from atlas.runtime import evaluate

FOLDER = "0516-longest-palindromic-subsequence"


def oracle(text):
    return max(
        len(candidate)
        for mask in range(1 << len(text))
        for candidate in ["".join(value for index, value in enumerate(text) if mask & (1 << index))]
        if candidate == candidate[::-1]
    )


@settings(max_examples=60, deadline=None)
@given(st.tuples(st.text(alphabet="abc", min_size=1, max_size=11)))
def test_optimized_matches_independent_small_or_model_oracle(args):
    assert evaluate(FOLDER, args=list(args)) == oracle(*args)
