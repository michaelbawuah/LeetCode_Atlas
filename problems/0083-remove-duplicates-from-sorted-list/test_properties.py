from hypothesis import given
from hypothesis import strategies as st

from atlas.runtime import build_list, evaluate, load_module


def nodes(head):
    result, seen = [], set()
    while head is not None:
        assert id(head) not in seen
        seen.add(id(head))
        result.append(head)
        head = head.next
    return result


FOLDER = "0083-remove-duplicates-from-sorted-list"


@given(st.lists(st.integers(-100, 100), max_size=100).map(sorted))
def test_dedup_matches_set_and_keeps_first_node_per_value(values):
    assert evaluate(FOLDER, args=[values]) == sorted(set(values))
    head = build_list(values)
    original = nodes(head)
    first = {}
    for node in original:
        first.setdefault(node.val, node)
    result = load_module(FOLDER).Solution().deleteDuplicates(head)
    assert nodes(result) == list(first.values())
