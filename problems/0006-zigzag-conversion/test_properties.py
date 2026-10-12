from hypothesis import given
from hypothesis import strategies as st

from atlas.runtime import load_module

Solution = load_module("0006-zigzag-conversion").Solution


@given(s=st.text(alphabet="abcXYZ,.", min_size=1, max_size=50), rows=st.integers(1, 12))
def test_conversion_matches_periodic_row_coordinates(s, rows):
    if rows == 1:
        expected = s
    else:
        period = 2 * (rows - 1)
        assigned = [min(index % period, period - index % period) for index in range(len(s))]
        expected = "".join(
            letter
            for row in range(rows)
            for letter, where in zip(s, assigned, strict=True)
            if where == row
        )
    assert Solution().convert(s, rows) == expected
