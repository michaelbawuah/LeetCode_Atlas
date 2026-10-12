from hypothesis import given
from hypothesis import strategies as st

from atlas.runtime import build_list_array, evaluate, load_module


def nodes(head):
    result, seen = [], set()
    while head is not None:
        assert id(head) not in seen
        seen.add(id(head))
        result.append(head)
        head = head.next
    return result


FOLDER = "0023-merge-k-sorted-lists"


@given(st.lists(st.lists(st.integers(-10000, 10000), max_size=25).map(sorted), max_size=12))
def test_heap_merge_matches_sorted_multiset_and_reuses_every_node(inputs):
    expected = sorted(value for values in inputs for value in values)
    assert evaluate(FOLDER, args=[inputs]) == expected
    heads = build_list_array(inputs)
    original = [node for head in heads for node in nodes(head)]
    result = load_module(FOLDER).Solution().mergeKLists(heads)
    actual = nodes(result)
    assert [node.val for node in actual] == expected
    assert len(actual) == len(original)
    assert {id(node) for node in actual} == {id(node) for node in original}
