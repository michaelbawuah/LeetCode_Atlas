from hypothesis import given, settings
from hypothesis import strategies as st

from atlas.runtime import evaluate

FOLDER = "0647-palindromic-substrings"


@settings(max_examples=80)
@given(st.text(alphabet="abc", min_size=1, max_size=16))
def test_centers_match_all_position_distinct_substrings(text):
    expected = sum(
        text[start:end] == text[start:end][::-1]
        for start in range(len(text))
        for end in range(start + 1, len(text) + 1)
    )
    assert evaluate(FOLDER, args=[text]) == expected
