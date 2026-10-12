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


FOLDER = "0086-partition-list"


@given(st.lists(st.integers(-100, 100), max_size=100), st.integers(-200, 200))
def test_partition_matches_stable_filters_and_identity_order(values, x):
    expected = [value for value in values if value < x] + [value for value in values if value >= x]
    assert evaluate(FOLDER, args=[values, x]) == expected
    head = build_list(values)
    original = nodes(head)
    result = load_module(FOLDER).Solution().partition(head, x)
    ordered = [node for node in original if node.val < x] + [
        node for node in original if node.val >= x
    ]
    assert nodes(result) == ordered
