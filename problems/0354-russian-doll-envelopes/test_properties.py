from hypothesis import given, settings
from hypothesis import strategies as st

from atlas.runtime import evaluate

FOLDER = "0354-russian-doll-envelopes"


def oracle(envelopes):
    def choose(width, height):
        return max((1 + choose(w, h) for w, h in envelopes if w > width and h > height), default=0)

    return choose(0, 0)


@settings(max_examples=60, deadline=None)
@given(
    st.tuples(st.lists(st.lists(st.integers(1, 8), min_size=2, max_size=2), min_size=1, max_size=7))
)
def test_optimized_matches_independent_small_or_model_oracle(args):
    assert evaluate(FOLDER, args=list(args)) == oracle(*args)
