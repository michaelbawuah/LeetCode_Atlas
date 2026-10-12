# 227. Basic Calculator II

[Problem on LeetCode](https://leetcode.com/problems/basic-calculator-ii/) · Medium

## Approach

A general expression tree parser stores syntax before evaluating. A term stack resolves multiplication/division immediately while deferring addition/subtraction.

## Invariant and correctness

Completed stack entries are signed additive terms. Multiplication and division change only the newest term, preserving operator precedence and left associativity; summing terms finishes the expression.

## Complexity

The parser makes O(n) character scans and arithmetic steps. Integer operations depend on the maximum intermediate bit length B, giving an O(n B) bit-work bound. With bounded 32-bit input operands, B can still grow linearly in the expression length. The copied text and term stack use O(n) storage; the terms can contain large integers.

## Boundaries and pitfalls

Division truncates toward zero, including a negative signed term. Operands are nonnegative, expressions valid, and divisors nonzero. The appended sentinel and term list use O(n) storage. A bounded final answer does not bound intermediate products: two identical large products may cancel. Python retains exact integers, and division uses integer arithmetic rather than conversion to a floating-point value.

## Follow-up

Keep only the current term and completed sum to retain O(1) arithmetic objects; their bit storage still depends on intermediate magnitudes.

## Verification

Named cases and an independent generated-input oracle or operation model accompany the source. Judge results are recorded separately in metadata.
