import ast
from fractions import Fraction

from hypothesis import given
from hypothesis import strategies as st

from atlas.runtime import load_module

Solution = load_module("0227-basic-calculator-ii").Solution


def evaluate(node):
    if isinstance(node, ast.Constant):
        return node.value
    left, right = evaluate(node.left), evaluate(node.right)
    if isinstance(node.op, ast.Add):
        return left + right
    if isinstance(node.op, ast.Sub):
        return left - right
    if isinstance(node.op, ast.Mult):
        return left * right
    return int(Fraction(left, right))


@given(numbers=st.lists(st.integers(1, 9), min_size=1, max_size=6), data=st.data())
def test_stack_calculator_matches_independent_ast(numbers, data):
    operations = data.draw(
        st.lists(
            st.sampled_from(list("+-*/")), min_size=len(numbers) - 1, max_size=len(numbers) - 1
        )
    )
    text = str(numbers[0]) + "".join(
        " " + op + " " + str(number) for op, number in zip(operations, numbers[1:], strict=True)
    )
    assert Solution().calculate(text) == evaluate(ast.parse(text, mode="eval").body)
