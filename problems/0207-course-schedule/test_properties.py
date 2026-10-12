from itertools import permutations

from hypothesis import given
from hypothesis import strategies as st

from atlas.runtime import evaluate

FOLDER = "0207-course-schedule"


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
def test_completion_matches_exhaustive_course_orderings(graph):
    count, prerequisites = graph
    expected = next(exhaustive_orders(count, prerequisites), None) is not None
    assert evaluate(FOLDER, args=[count, prerequisites]) is expected
