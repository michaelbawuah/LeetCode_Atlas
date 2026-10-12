import re

from hypothesis import given, settings
from hypothesis import strategies as st

from atlas.runtime import evaluate

FOLDER = "0044-wildcard-matching"


def oracle(text, pattern):
    expression = "".join(
        ".*" if token == "*" else "." if token == "?" else re.escape(token) for token in pattern
    )
    return re.fullmatch(expression, text) is not None


@settings(max_examples=60, deadline=None)
@given(st.tuples(st.text(alphabet="ab", max_size=8), st.text(alphabet="ab?*", max_size=7)))
def test_optimized_matches_independent_small_or_model_oracle(args):
    assert evaluate(FOLDER, args=list(args)) == oracle(*args)
