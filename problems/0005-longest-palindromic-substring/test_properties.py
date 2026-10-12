from hypothesis import given, settings
from hypothesis import strategies as st

from atlas.runtime import evaluate

FOLDER = "0005-longest-palindromic-substring"


@settings(max_examples=80)
@given(st.text(alphabet="abA1", min_size=1, max_size=14))
def test_center_expansion_matches_all_palindromic_slices(text):
    candidates = [
        text[start:end]
        for start in range(len(text))
        for end in range(start + 1, len(text) + 1)
        if text[start:end] == text[start:end][::-1]
    ]
    answer = evaluate(FOLDER, args=[text])
    assert answer in text
    assert answer == answer[::-1]
    assert len(answer) == max(map(len, candidates))
