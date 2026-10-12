from hypothesis import given, settings
from hypothesis import strategies as st

from atlas.runtime import evaluate

FOLDER = "0190-reverse-bits"


def reverse_with_padded_text(value):
    return int(format(value, "032b")[::-1], 2)


@settings(max_examples=100)
@given(st.integers(0, (1 << 30) - 1).map(lambda value: value << 1))
def test_bit_loop_matches_text_oracle_in_current_judge_domain(value):
    assert evaluate(FOLDER, args=[value]) == reverse_with_padded_text(value)


@settings(max_examples=100)
@given(st.integers(0, (1 << 32) - 1))
def test_robustness_full_unsigned_32_bit_domain(value):
    # An explicitly wider robustness domain than the current even signed-input constraints.
    result = evaluate(FOLDER, args=[value])
    assert result == reverse_with_padded_text(value)
    assert evaluate(FOLDER, args=[result]) == value
