from hypothesis import given, settings
from hypothesis import strategies as st

from atlas.runtime import evaluate

FOLDER = "1143-longest-common-subsequence"


def all_subsequences(text):
    return {
        "".join(value for index, value in enumerate(text) if mask & (1 << index))
        for mask in range(1 << len(text))
    }


@settings(max_examples=80)
@given(
    st.text(alphabet="abc", min_size=1, max_size=8),
    st.text(alphabet="abc", min_size=1, max_size=8),
)
def test_rolling_grid_matches_common_subsequence_intersection(first, second):
    expected = max(map(len, all_subsequences(first) & all_subsequences(second)))
    assert evaluate(FOLDER, args=[first, second]) == expected
