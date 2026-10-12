from hypothesis import given
from hypothesis import strategies as st

from atlas.runtime import build_list_cycle, evaluate, load_module

FOLDER = "0141-linked-list-cycle"


@given(st.lists(st.integers(-100000, 100000), max_size=150), st.data())
def test_floyd_matches_the_independent_tail_target_contract(values, data):
    position = data.draw(st.integers(-1, len(values) - 1)) if values else -1
    encoded = {"values": values, "pos": position}
    assert evaluate(FOLDER, args=[encoded]) == (position >= 0)


def test_long_equal_valued_linear_list_is_not_a_cycle():
    assert evaluate(FOLDER, args=[{"values": [1] * 4000, "pos": -1}]) is False


def test_long_cycle_with_a_short_repeating_suffix():
    assert evaluate(FOLDER, args=[{"values": [0] * 4000, "pos": 3990}]) is True


@given(st.lists(st.integers(-10, 10), max_size=80), st.data())
def test_two_pointer_result_matches_visited_identity_oracle_without_mutation(values, data):
    position = data.draw(st.integers(-1, len(values) - 1)) if values else -1
    head = build_list_cycle({"values": values, "pos": position})
    nodes, seen = [], set()
    current = head
    while current is not None and id(current) not in seen:
        seen.add(id(current))
        nodes.append(current)
        current = current.next
    expected = current is not None
    links = [node.next for node in nodes]
    assert load_module(FOLDER).Solution().hasCycle(head) == expected
    assert [node.next for node in nodes] == links
