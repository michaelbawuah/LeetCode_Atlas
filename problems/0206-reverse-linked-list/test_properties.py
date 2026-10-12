from hypothesis import given
from hypothesis import strategies as st

from atlas.runtime import build_list, evaluate, load_module

FOLDER = "0206-reverse-linked-list"


@given(st.lists(st.integers(-5000, 5000), max_size=100))
def test_reverse_matches_value_order(values):
    assert evaluate(FOLDER, args=[values]) == values[::-1]


@given(st.lists(st.integers(-50, 50), max_size=80))
def test_reversal_reuses_original_nodes(values):
    head = build_list(values)
    original_ids = []
    node = head
    while node is not None:
        original_ids.append(id(node))
        node = node.next
    result = load_module(FOLDER).Solution().reverseList(head)
    actual_ids = []
    node = result
    while node is not None:
        assert len(actual_ids) < len(values)
        actual_ids.append(id(node))
        node = node.next
    assert actual_ids == original_ids[::-1]
