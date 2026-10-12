# 12. Integer to Roman

[Problem on LeetCode](https://leetcode.com/problems/integer-to-roman/) · Medium

## Approach

Decimal-place lookup is a constant-size alternative. Consume the largest representable symbol or subtractive pair first.

## Invariant and correctness

At each pair, emitted symbols encode exactly the value removed from num. The ordered pairs include the required subtractive forms, so the remaining lower value is encoded canonically by subsequent pairs.

## Complexity

Time: O(1) under 1..3999. Space: O(1) bounded output.

## Boundaries and pitfalls

The supported range is 1 through 3999. Include 4/9 forms at each decimal place rather than emitting four copies of the smaller symbol.

## Follow-up

Describe how the representation would change beyond 3999.

## Verification

Named cases and an independent generated-input oracle or operation model accompany the source. Judge results are recorded separately in metadata.

## C++23 counterpart

[Source](solution.cpp) · [Local adapter](cpp_runner.cpp) · [Parity generator](parity.py)

Both versions preserve input unless the problem specifies mutation. C++ string arguments use const references; adapter-decoded inputs are separately owned and excluded from solution auxiliary space.

Time: O(1) under 1..3999. Space: O(1) bounded output.
