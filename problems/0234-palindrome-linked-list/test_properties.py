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


FOLDER = "0234-palindrome-linked-list"


@given(st.lists(st.integers(0, 9), min_size=1, max_size=150))
def test_palindrome_matches_values_and_restores_all_links(values):
    assert evaluate(FOLDER, args=[values]) == (values == values[::-1])
    head = build_list(values)
    original = node_sequence(head)
    links = [node.next for node in original]
    actual = load_module(FOLDER).Solution().isPalindrome(head)
    assert actual == (values == values[::-1])
    assert node_sequence(head) == original
    assert [node.next for node in original] == links


def test_long_palindrome_uses_constant_pointer_state():
    values = [index % 10 for index in range(2000)]
    assert evaluate(FOLDER, args=[values + values[::-1]]) is True
