from itertools import permutations

from hypothesis import given
from hypothesis import strategies as st

from atlas.runtime import evaluate

FOLDER = "0210-course-schedule-ii"


@st.composite
def directed_graphs(draw):
    count = draw(st.integers(1, 5))
    choices = [
        (course, prerequisite)
        for course in range(count)
        for prerequisite in range(count)
        if course != prerequisite
    ]
    edges = (
        draw(st.lists(st.sampled_from(choices), unique=True, max_size=min(12, len(choices))))
        if choices
        else []
    )
    return count, [list(edge) for edge in edges]


def exhaustive_orders(count, prerequisites):
    for ordering in permutations(range(count)):
        positions = {course: index for index, course in enumerate(ordering)}
        if all(
            positions[prerequisite] < positions[course] for course, prerequisite in prerequisites
        ):
            yield ordering


@given(directed_graphs())
def test_order_is_legal_exactly_when_an_exhaustive_witness_exists(graph):
    count, prerequisites = graph
    witness = next(exhaustive_orders(count, prerequisites), None)
    actual = evaluate(FOLDER, args=[count, prerequisites])
    if witness is None:
        assert actual == []
    else:
        assert len(actual) == count
        assert set(actual) == set(range(count))
        assert all(type(course) is int for course in actual)
        positions = {course: index for index, course in enumerate(actual)}
        assert all(
            positions[prerequisite] < positions[course] for course, prerequisite in prerequisites
        )
