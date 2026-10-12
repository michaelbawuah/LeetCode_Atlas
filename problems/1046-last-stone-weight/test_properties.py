from hypothesis import given
from hypothesis import strategies as st

from atlas.runtime import load_module

Solution = load_module("1046-last-stone-weight").Solution


@given(st.lists(st.integers(1, 1000), min_size=1, max_size=30))
def test_smashes_match_repeated_sorting(stones):
    remaining = list(stones)
    while len(remaining) > 1:
        remaining.sort()
        heavier = remaining.pop()
        lighter = remaining.pop()
        if heavier != lighter:
            remaining.append(heavier - lighter)
    expected = remaining[0] if remaining else 0
    snapshot = list(stones)
    assert Solution().lastStoneWeight(stones) == expected
    assert stones == snapshot
