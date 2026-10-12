# 13. Roman to Integer

[Problem on LeetCode](https://leetcode.com/problems/roman-to-integer/) · Easy

## Approach

A pair-token parser can consume subtractive forms explicitly. Instead give a symbol a negative contribution when its successor is larger.

## Invariant and correctness

For a valid Roman numeral every subtractive pair contributes negative-small plus positive-large. All other symbols contribute positively, so summing the signed contributions gives the represented value.

## Complexity

Time: O(n). Space: O(1).

## Boundaries and pitfalls

Inputs are valid Roman numerals in 1..3999; this decoder does not validate arbitrary symbol sequences. Inspect the next symbol only when it exists.

## Follow-up

Validate noncanonical Roman input rather than assuming the contract.

## Verification

Named cases and an independent generated-input oracle or operation model accompany the source. Judge results are recorded separately in metadata.

## C++23 counterpart

[Source](solution.cpp) · [Local adapter](cpp_runner.cpp) · [Parity generator](parity.py)

Both versions preserve input unless the problem specifies mutation. C++ string arguments use const references; adapter-decoded inputs are separately owned and excluded from solution auxiliary space.

Time: O(n). Space: O(1).
