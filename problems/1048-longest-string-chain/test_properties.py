from hypothesis import given, settings
from hypothesis import strategies as st

from atlas.runtime import evaluate

FOLDER = "1048-longest-string-chain"


def oracle(words):
    def follows(short, long):
        return len(long) == len(short) + 1 and any(
            long[:index] + long[index + 1 :] == short for index in range(len(long))
        )

    def chain(word):
        return 1 + max(
            (chain(next_word) for next_word in words if follows(word, next_word)), default=0
        )

    return max(map(chain, words))


@settings(max_examples=60, deadline=None)
@given(st.tuples(st.lists(st.text(alphabet="ab", min_size=1, max_size=5), min_size=1, max_size=8)))
def test_optimized_matches_independent_small_or_model_oracle(args):
    assert evaluate(FOLDER, args=list(args)) == oracle(*args)
