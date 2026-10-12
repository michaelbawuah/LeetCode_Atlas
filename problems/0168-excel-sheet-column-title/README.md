# 168. Excel Sheet Column Title

[Problem on LeetCode](https://leetcode.com/problems/excel-sheet-column-title/) · Easy

## Approach

Ordinary base-26 digits include zero and do not model A=1. Subtract one before each divmod to extract a bijective numeral digit.

## Invariant and correctness

The extracted letters encode the removed low-order positions, and the remaining quotient describes all higher positions. Reversing the extraction order reconstructs the title.

## Complexity

Time: O(log(columnNumber + 1)). Space: O(log(columnNumber + 1)) output.

## Boundaries and pitfalls

The Z-to-AA transition requires subtracting one before division. Column numbers are positive and bounded by signed 32-bit maximum.

## Follow-up

Design a bijective numeral system with a supplied alphabet.

## Verification

Named cases and an independent generated-input oracle or operation model accompany the source. Judge results are recorded separately in metadata.
