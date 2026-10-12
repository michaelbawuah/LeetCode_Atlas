from hypothesis import given
from hypothesis import strategies as st

from atlas.runtime import load_module

Solution = load_module("0074-search-a-2d-matrix").Solution


@given(
    rows=st.integers(1, 6),
    columns=st.integers(1, 6),
    target=st.integers(-10000, 10000),
    data=st.data(),
)
def test_matrix_search_matches_membership(rows, columns, target, data):
    values = sorted(
        data.draw(
            st.lists(
                st.integers(-10000, 10000),
                min_size=rows * columns,
                max_size=rows * columns,
                unique=True,
            )
        )
    )
    matrix = [values[index : index + columns] for index in range(0, len(values), columns)]
    expected = any(target == value for row in matrix for value in row)
    assert Solution().searchMatrix(matrix, target) == expected
    # Random targets usually miss, so also check every generated cell.
    for value in values:
        assert Solution().searchMatrix(matrix, value) is True
