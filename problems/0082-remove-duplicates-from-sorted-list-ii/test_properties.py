from collections import Counter

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


FOLDER = "0082-remove-duplicates-from-sorted-list-ii"


@given(st.lists(st.integers(-100, 100), max_size=100).map(sorted))
def test_singleton_runs_match_frequency_oracle_and_keep_original_nodes(values):
    counts = Counter(values)
    expected = [value for value in values if counts[value] == 1]
    assert evaluate(FOLDER, args=[values]) == expected
    head = build_list(values)
    original = nodes(head)
    result = load_module(FOLDER).Solution().deleteDuplicates(head)
    assert [id(node) for node in nodes(result)] == [
        id(node) for node in original if counts[node.val] == 1
    ]
