from hypothesis import given
from hypothesis import strategies as st

from atlas.runtime import build_list, evaluate, load_module


def node_sequence(head):
    nodes, seen = [], set()
    while head is not None:
        assert id(head) not in seen
        seen.add(id(head))
        nodes.append(head)
        head = head.next
    return nodes


FOLDER = "0092-reverse-linked-list-ii"


@given(st.lists(st.integers(-500, 500), min_size=1, max_size=100), st.data())
def test_segment_reversal_matches_slice_order_and_node_identity(values, data):
    left = data.draw(st.integers(1, len(values)))
    right = data.draw(st.integers(left, len(values)))
    expected = values[: left - 1] + values[left - 1 : right][::-1] + values[right:]
    assert evaluate(FOLDER, args=[values, left, right]) == expected
    head = build_list(values)
    nodes = node_sequence(head)
    expected_nodes = nodes[: left - 1] + nodes[left - 1 : right][::-1] + nodes[right:]
    result = load_module(FOLDER).Solution().reverseBetween(head, left, right)
    assert [id(node) for node in node_sequence(result)] == [id(node) for node in expected_nodes]
