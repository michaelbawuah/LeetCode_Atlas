from fractions import Fraction

from hypothesis import given
from hypothesis import strategies as st

from atlas.runtime import load_module

Solution = load_module("0150-evaluate-reverse-polish-notation").Solution


def reference(tree):
    if isinstance(tree, int):
        return tree
    operator, left_tree, right_tree = tree
    left, right = reference(left_tree), reference(right_tree)
    if operator == "+":
        return left + right
    if operator == "-":
        return left - right
    if operator == "*":
        return left * right
    return int(Fraction(left, right))


def postfix(tree):
    if isinstance(tree, int):
        return [str(tree)]
    operator, left, right = tree
    return postfix(left) + postfix(right) + [operator]


expressions = st.recursive(
    st.integers(-5, 5),
    lambda children: st.tuples(st.sampled_from(["+", "-", "*", "/"]), children, children).filter(
        lambda node: node[0] != "/" or reference(node[2]) != 0
    ),
    max_leaves=6,
)


@given(expressions)
def test_postfix_matches_expression_tree(tree):
    tokens = postfix(tree)
    snapshot = list(tokens)
    assert Solution().evalRPN(tokens) == reference(tree)
    assert tokens == snapshot
