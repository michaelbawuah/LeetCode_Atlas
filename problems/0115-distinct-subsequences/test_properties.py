from itertools import combinations

from hypothesis import given, settings
from hypothesis import strategies as st

from atlas.runtime import evaluate

FOLDER = "0115-distinct-subsequences"


@settings(max_examples=80)
@given(
    st.text(alphabet="abAB", min_size=1, max_size=12),
    st.text(alphabet="abAB", min_size=1, max_size=6),
)
def test_descending_updates_match_index_combination_enumeration(source, target):
    expected = sum(
        "".join(source[index] for index in selected) == target
        for selected in combinations(range(len(source)), len(target))
    )
    assert evaluate(FOLDER, args=[source, target]) == expected
