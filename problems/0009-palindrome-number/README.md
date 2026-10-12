# 9. Palindrome Number

[Problem on LeetCode](https://leetcode.com/problems/palindrome-number/) · Easy

## Approach

Converting to text uses digit-sized storage. Reverse only the trailing half into a scalar.

## Invariant and correctness

The reversed suffix grows while the unreversed prefix shrinks. When their lengths meet, equal halves certify an even-length palindrome; dropping the suffix middle digit handles odd length.

## Complexity

Time: O(log(x + 1)) for nonnegative x. Space: O(1).

## Boundaries and pitfalls

Negative numbers cannot match their leading minus sign. A nonzero multiple of ten cannot have a leading zero. Reversing only half avoids full-number overflow in C++.

## Follow-up

Check a palindrome in another numeral base without converting to text.

## Verification

Named cases and an independent generated-input oracle or operation model accompany the source. Judge results are recorded separately in metadata.

## C++23 counterpart

[Source](solution.cpp) · [Local adapter](cpp_runner.cpp) · [Parity generator](parity.py)

Both versions preserve input unless the problem specifies mutation. C++ string arguments use const references; adapter-decoded inputs are separately owned and excluded from solution auxiliary space.

Time: O(log(x + 1)) for nonnegative x. Space: O(1).
