from hypothesis import given
from hypothesis import strategies as st

from atlas.runtime import load_module

Solution = load_module("0394-decode-string").Solution

trees = st.tuples(
    st.lists(st.integers(1, 3), max_size=4), st.text(alphabet="ab", min_size=1, max_size=3)
)


def encode(tree):
    return "".join(str(count) + "[" for count in tree[0]) + tree[1] + "]" * len(tree[0])


def expand(tree):
    result = tree[1]
    for count in tree[0]:
        result *= count
    return result


@given(st.lists(trees, min_size=1, max_size=2))
def test_stack_decoder_matches_generated_expression_tree(trees):
    assert Solution().decodeString("".join(encode(tree) for tree in trees)) == "".join(
        expand(tree) for tree in trees
    )
