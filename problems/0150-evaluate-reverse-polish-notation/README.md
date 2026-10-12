# 150. Evaluate Reverse Polish Notation

[Problem on LeetCode](https://leetcode.com/problems/evaluate-reverse-polish-notation/) · Medium

## Intuition
Postfix notation puts an operator after its operands. Each operator can consume the last two completed subexpressions from a stack.

## Approaches
- **Baseline:** repeatedly locate a reducible operand/operand/operator triple and rebuild the token list: O(n²) time, O(n) space.
- **Optimized:** scan once, pushing numbers and replacing the top two values with an operator's result.

## Correctness invariant
The stack contains the values of completed subexpressions that have not yet been consumed, in expression order. A number starts a completed subexpression. An operator combines the last two, so popping the right operand before the left preserves subtraction and division order. A valid complete expression leaves exactly one value.

## Complexity
O(n) time and O(n) extra space for n tokens under the problem's bounded-integer arithmetic model.

## Edge cases and pitfalls
Python floor division rounds negative results downward; this problem requires truncation toward zero. Divide the absolute values with integer arithmetic, then restore the sign. Converting a floating-point quotient to int is unnecessary and can lose precision on wider integer inputs. The input contract supplies valid expressions and nonzero divisors.

## Follow-up
Produce an infix expression tree from the same token stream, keeping enough parentheses to preserve its meaning.

## Verification
Named fixtures and an independent generated-input reference accompany this implementation. Official judge results are tracked separately in metadata.

## Python and C++23 comparison

Both sources consume postfix tokens with an operand stack, taking O(n) time and O(n) auxiliary space under the bounded-token arithmetic model. Python divides absolute values with integer floor division and restores the sign. C++ signed integer division already truncates toward zero. The C++ stack uses `long long` and checks every parsed operand and computed intermediate against the required `int` range before storing it; official valid inputs satisfy those bounds. C++ also checks operand availability and division by zero. These defensive checks do not turn invalid expressions into valid problem inputs. The token vector is read without mutation.
