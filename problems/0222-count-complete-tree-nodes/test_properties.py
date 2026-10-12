from hypothesis import given
from hypothesis import strategies as st

from atlas.runtime import evaluate

FOLDER = "0222-count-complete-tree-nodes"


@given(st.lists(st.integers(0, 50000), max_size=300))
def test_complete_encoding_count_matches_the_number_of_supplied_positions(values):
    assert evaluate(FOLDER, args=[values]) == len(values)


def test_large_complete_final_level():
    assert evaluate(FOLDER, args=[[0] * 4095]) == 4095
