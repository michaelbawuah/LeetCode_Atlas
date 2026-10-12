from hypothesis import given
from hypothesis import strategies as st

from atlas.runtime import build_list, evaluate, load_module

FOLDER = "0021-merge-two-sorted-lists"
VALUES = st.lists(st.integers(-100, 100), max_size=50).map(sorted)


@given(VALUES, VALUES)
def test_merge_matches_sorted_multiset(left, right):
    assert evaluate(FOLDER, args=[left, right]) == sorted(left + right)


@given(VALUES, VALUES)
def test_merge_reuses_all_input_nodes(left, right):
    first, second = build_list(left), build_list(right)
    input_ids = set()
    for head in (first, second):
        node = head
        while node is not None:
            input_ids.add(id(node))
            node = node.next
    result = load_module(FOLDER).Solution().mergeTwoLists(first, second)
    output_ids = set()
    node = result
    while node is not None:
        assert id(node) not in output_ids
        output_ids.add(id(node))
        node = node.next
    assert output_ids == input_ids
