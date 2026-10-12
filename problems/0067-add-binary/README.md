# 67. Add Binary

[Problem on LeetCode](https://leetcode.com/problems/add-binary/) · Easy

## Approach

Converting both complete strings to integers requires arbitrary-width conversion. Add one binary column at a time with a carry.

## Invariant and correctness

The reversed result holds the sum digits already finalized, and carry is the value carried into the next unprocessed column. Division/modulo by two produce the next digit and carry exactly.

## Complexity

Time: O(n + m). Space: O(n + m) including output.

## Boundaries and pitfalls

Continue when either input or carry remains. Inputs use canonical binary strings, including the single zero.

## Follow-up

Generalize the same loop to an arbitrary base supplied at runtime.

## Verification

Named cases and an independent generated-input oracle or operation model accompany the source. Judge results are recorded separately in metadata.

## C++23 counterpart

[Source](solution.cpp) · [Local adapter](cpp_runner.cpp) · [Parity generator](parity.py)

Both versions preserve input unless the problem specifies mutation. C++ string arguments use const references; adapter-decoded inputs are separately owned and excluded from solution auxiliary space.

Time: O(n + m). Space: O(n + m) including output.
