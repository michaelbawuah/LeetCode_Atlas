# 171. Excel Sheet Column Number

[Problem on LeetCode](https://leetcode.com/problems/excel-sheet-column-number/) · Easy

## Approach

Evaluating each letter times a positional power repeats work. Horner-style accumulation advances the existing prefix by a factor of 26 and adds the next digit.

## Invariant and correctness

The accumulator equals the numeric value of the processed title prefix. Multiplication shifts all previous positions and the A=1 through Z=26 digit fills the last position.

## Complexity

Time: O(n). Space: O(1).

## Boundaries and pitfalls

Only valid titles whose numeric value fits signed 32-bit are supplied. Those bounds also keep every C++ prefix accumulation in range.

## Follow-up

Support longer titles with arbitrary-width arithmetic.

## Verification

Named cases and an independent generated-input oracle or operation model accompany the source. Judge results are recorded separately in metadata.

## C++23 counterpart

[Source](solution.cpp) · [Local adapter](cpp_runner.cpp) · [Parity generator](parity.py)

Both versions preserve input unless the problem specifies mutation. C++ string arguments use const references; adapter-decoded inputs are separately owned and excluded from solution auxiliary space.

Time: O(n). Space: O(1).
