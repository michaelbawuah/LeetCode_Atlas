from hypothesis import given
from hypothesis import strategies as st

from atlas.runtime import build_list, evaluate, load_module

FOLDER = "0019-remove-nth-node-from-end-of-list"


@given(st.lists(st.integers(0, 100), min_size=1, max_size=30), st.data())
def test_removal_matches_sequence_deletion(values, data):
    n = data.draw(st.integers(1, len(values)))
    index = len(values) - n
    assert evaluate(FOLDER, args=[values, n]) == values[:index] + values[index + 1 :]
    head = build_list(values)
    nodes = []
    current = head
    while current is not None:
        nodes.append(current)
        current = current.next
    result = load_module(FOLDER).Solution().removeNthFromEnd(head, n)
    actual_ids = []
    while result is not None:
        assert len(actual_ids) < len(values)
        actual_ids.append(id(result))
        result = result.next
    expected = nodes[:index] + nodes[index + 1 :]
    assert actual_ids == [id(node) for node in expected]
