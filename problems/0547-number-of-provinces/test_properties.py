from hypothesis import given
from hypothesis import strategies as st

from atlas.runtime import evaluate

FOLDER = "0547-number-of-provinces"


@st.composite
def symmetric_matrices(draw):
    count = draw(st.integers(1, 10))
    matrix = [[int(i == j) for j in range(count)] for i in range(count)]
    for first in range(count):
        for last in range(first + 1, count):
            matrix[first][last] = matrix[last][first] = draw(st.integers(0, 1))
    return matrix


def union_find_components(matrix):
    parent = list(range(len(matrix)))

    def root(city):
        while parent[city] != city:
            city = parent[city]
        return city

    for first in range(len(matrix)):
        for last in range(first):
            if matrix[first][last]:
                parent[root(first)] = root(last)
    return len({root(city) for city in range(len(matrix))})


@given(symmetric_matrices())
def test_matrix_traversal_matches_union_find_partition(matrix):
    assert evaluate(FOLDER, args=[matrix]) == union_find_components(matrix)
