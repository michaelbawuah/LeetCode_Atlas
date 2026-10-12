from itertools import combinations

from hypothesis import given, settings
from hypothesis import strategies as st

from atlas.runtime import evaluate

FOLDER = "0097-interleaving-string"


def exhaustive_interleavings(first, second):
    size = len(first) + len(second)
    for chosen in combinations(range(size), len(first)):
        first_positions = set(chosen)
        first_iterator, second_iterator = iter(first), iter(second)
        yield "".join(
            next(first_iterator) if position in first_positions else next(second_iterator)
            for position in range(size)
        )


@settings(max_examples=80)
@given(
    st.text(alphabet="ab", max_size=5),
    st.text(alphabet="ab", max_size=5),
    st.text(alphabet="ab", max_size=10),
)
def test_rolling_grid_matches_all_order_preserving_merges(first, second, candidate):
    assert evaluate(FOLDER, args=[first, second, candidate]) == (
        candidate in set(exhaustive_interleavings(first, second))
    )


@settings(max_examples=50)
@given(st.text(alphabet="ab", max_size=5), st.text(alphabet="ab", max_size=5), st.data())
def test_every_constructed_order_preserving_merge_is_accepted(first, second, data):
    candidate = data.draw(st.sampled_from(list(exhaustive_interleavings(first, second))))
    assert evaluate(FOLDER, args=[first, second, candidate]) is True
