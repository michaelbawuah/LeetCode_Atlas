from functools import cache

from hypothesis import given, settings
from hypothesis import strategies as st

from atlas.runtime import evaluate

FOLDER = "0087-scramble-string"


@cache
def possible_scrambles(text):
    if len(text) == 1:
        return {text}
    results = set()
    for cut in range(1, len(text)):
        for left in possible_scrambles(text[:cut]):
            for right in possible_scrambles(text[cut:]):
                results.update((left + right, right + left))
    return results


def oracle(first, second):
    return second in possible_scrambles(first)


@settings(max_examples=60, deadline=None)
@given(
    st.integers(1, 6).flatmap(
        lambda size: st.tuples(
            st.text(alphabet="abc", min_size=size, max_size=size),
            st.text(alphabet="abc", min_size=size, max_size=size),
        )
    )
)
def test_optimized_matches_independent_small_or_model_oracle(args):
    assert evaluate(FOLDER, args=list(args)) == oracle(*args)
