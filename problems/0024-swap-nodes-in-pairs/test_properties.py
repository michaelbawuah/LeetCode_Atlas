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


FOLDER = "0024-swap-nodes-in-pairs"


def paired(sequence):
    output = []
    for index in range(0, len(sequence), 2):
        output.extend(sequence[index : index + 2][::-1])
    return output


@given(st.lists(st.integers(0, 100), max_size=100))
def test_pairs_match_sequence_order_and_reuse_nodes(values):
    assert evaluate(FOLDER, args=[values]) == paired(values)
    head = build_list(values)
    original = node_sequence(head)
    result = load_module(FOLDER).Solution().swapPairs(head)
    assert [id(node) for node in node_sequence(result)] == [id(node) for node in paired(original)]
