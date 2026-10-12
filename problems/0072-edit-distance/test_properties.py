from collections import deque

from hypothesis import given, settings
from hypothesis import strategies as st

from atlas.runtime import evaluate

FOLDER = "0072-edit-distance"


def shortest_edit_path(source, target):
    alphabet = "ab"
    limit = max(len(source), len(target))
    pending = deque([(source, 0)])
    seen = {source}
    while pending:
        text, distance = pending.popleft()
        if text == target:
            return distance
        neighbors = {text[:index] + text[index + 1 :] for index in range(len(text))}
        neighbors.update(
            text[:index] + letter + text[index + 1 :]
            for index in range(len(text))
            for letter in alphabet
        )
        if len(text) < limit:
            neighbors.update(
                text[:index] + letter + text[index:]
                for index in range(len(text) + 1)
                for letter in alphabet
            )
        for neighbor in neighbors - seen:
            seen.add(neighbor)
            pending.append((neighbor, distance + 1))
    raise AssertionError("Deleting source then inserting target must be feasible")


@settings(max_examples=60)
@given(st.text(alphabet="ab", max_size=3), st.text(alphabet="ab", max_size=3))
def test_rolling_dp_matches_breadth_first_edit_operations(source, target):
    assert evaluate(FOLDER, args=[source, target]) == shortest_edit_path(source, target)
