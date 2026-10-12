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


FOLDER = "0002-add-two-numbers"


@st.composite
def digit_lists(draw):
    length = draw(st.integers(1, 60))
    digits = draw(st.lists(st.integers(0, 9), min_size=length, max_size=length))
    if length > 1:
        digits[-1] = draw(st.integers(1, 9))
    return digits


def number(digits):
    return int("".join(map(str, digits[::-1])))


@given(digit_lists(), digit_lists())
def test_digits_match_integer_arithmetic_without_input_aliases(first, second):
    expected = list(map(int, str(number(first) + number(second))[::-1]))
    assert evaluate(FOLDER, args=[first, second]) == expected
    left, right = build_list(first), build_list(second)
    original = nodes(left) + nodes(right)
    links = [(node.val, node.next) for node in original]
    result = load_module(FOLDER).Solution().addTwoNumbers(left, right)
    output = nodes(result)
    assert [node.val for node in output] == expected
    assert {id(node) for node in output}.isdisjoint(id(node) for node in original)
    assert [(node.val, node.next) for node in original] == links
