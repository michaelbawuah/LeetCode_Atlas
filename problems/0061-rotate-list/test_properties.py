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


FOLDER = "0061-rotate-list"


@given(st.lists(st.integers(-100, 100), max_size=100), st.integers(0, 2000000000))
def test_rotation_matches_slices_and_preserves_all_node_identities(values, k):
    shift = k % len(values) if values else 0
    expected = values[-shift:] + values[:-shift] if shift else values.copy()
    assert evaluate(FOLDER, args=[values, k]) == expected
    head = build_list(values)
    original = nodes(head)
    result = load_module(FOLDER).Solution().rotateRight(head, k)
    ordered = original[-shift:] + original[:-shift] if shift else original
    assert [id(node) for node in nodes(result)] == [id(node) for node in ordered]
