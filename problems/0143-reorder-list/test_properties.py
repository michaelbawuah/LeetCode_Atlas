from hypothesis import given
from hypothesis import strategies as st

from atlas.runtime import build_list, evaluate, load_module

FOLDER = "0143-reorder-list"


def reordered(sequence):
    result = []
    left, right = 0, len(sequence) - 1
    while left <= right:
        result.append(sequence[left])
        if left != right:
            result.append(sequence[right])
        left += 1
        right -= 1
    return result


@given(st.lists(st.integers(1, 1000), min_size=1, max_size=150))
def test_weaving_matches_alternating_ends_and_reuses_nodes(values):
    assert evaluate(FOLDER, args=[values]) == reordered(values)
    head = build_list(values)
    original = []
    current = head
    while current is not None:
        original.append(current)
        current = current.next
    assert load_module(FOLDER).Solution().reorderList(head) is None
    actual = []
    current = head
    while current is not None:
        assert len(actual) < len(values)
        actual.append(id(current))
        current = current.next
    assert actual == [id(node) for node in reordered(original)]


def test_long_list_uses_no_recursive_calls():
    values = [index % 1000 + 1 for index in range(3000)]
    assert evaluate(FOLDER, args=[values]) == reordered(values)
