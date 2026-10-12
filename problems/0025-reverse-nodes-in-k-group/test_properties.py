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


FOLDER = "0025-reverse-nodes-in-k-group"


def grouped(sequence, k):
    output = []
    for start in range(0, len(sequence), k):
        group = sequence[start : start + k]
        output.extend(group[::-1] if len(group) == k else group)
    return output


@given(st.lists(st.integers(0, 1000), min_size=1, max_size=120), st.data())
def test_complete_groups_match_slices_and_reuse_nodes(values, data):
    k = data.draw(st.integers(1, len(values)))
    assert evaluate(FOLDER, args=[values, k]) == grouped(values, k)
    head = build_list(values)
    original = node_sequence(head)
    result = load_module(FOLDER).Solution().reverseKGroup(head, k)
    assert [id(node) for node in node_sequence(result)] == [
        id(node) for node in grouped(original, k)
    ]


def test_long_list_does_not_use_recursion_per_group():
    values = [index % 1001 for index in range(4000)]
    assert evaluate(FOLDER, args=[values, 2]) == grouped(values, 2)
