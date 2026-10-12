from hypothesis import given
from hypothesis import strategies as st

from atlas.runtime import load_module

NumMatrix = load_module("0304-range-sum-query-2d-immutable").NumMatrix


@given(rows=st.integers(1, 5), cols=st.integers(1, 5), data=st.data())
def test_all_rectangles_match_direct_cell_sums(rows, cols, data):
    matrix = data.draw(
        st.lists(
            st.lists(st.integers(-100, 100), min_size=cols, max_size=cols),
            min_size=rows,
            max_size=rows,
        )
    )
    obj = NumMatrix(matrix)
    for r1 in range(rows):
        for r2 in range(r1, rows):
            for c1 in range(cols):
                for c2 in range(c1, cols):
                    assert obj.sumRegion(r1, c1, r2, c2) == sum(
                        matrix[r][c] for r in range(r1, r2 + 1) for c in range(c1, c2 + 1)
                    )
