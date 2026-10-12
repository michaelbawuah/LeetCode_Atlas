from hypothesis import given, settings
from hypothesis import strategies as st

from atlas.runtime import evaluate

FOLDER = "0474-ones-and-zeroes"


def oracle(words, m, n):
    best = 0
    for mask in range(1 << len(words)):
        chosen = [word for index, word in enumerate(words) if mask & (1 << index)]
        if (
            sum(word.count("0") for word in chosen) <= m
            and sum(word.count("1") for word in chosen) <= n
        ):
            best = max(best, len(chosen))
    return best


@settings(max_examples=60, deadline=None)
@given(
    st.tuples(
        st.lists(st.text(alphabet="01", min_size=1, max_size=5), min_size=1, max_size=9),
        st.integers(1, 6),
        st.integers(1, 6),
    )
)
def test_optimized_matches_independent_small_or_model_oracle(args):
    assert evaluate(FOLDER, args=list(args)) == oracle(*args)
