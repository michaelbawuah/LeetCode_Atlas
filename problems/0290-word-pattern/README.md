# 290. Word Pattern

[Problem on LeetCode](https://leetcode.com/problems/word-pattern/) · Easy

## Approach

Pairwise equality checks take quadratic time. Tokenize words and enforce a bijection from pattern letters to words and back.

## Invariant and correctness

The two maps encode a consistent one-to-one association for every processed position. A length mismatch prevents pairing positions; a conflicting association prevents the required pattern.

## Complexity

Time: O(n + m) expected. Space: O(n + m).

## Boundaries and pitfalls

Several letters cannot map to one word. m is input string length and n is pattern length; token copies and word hashing are included.

## Follow-up

Match streaming words without retaining the entire token list.

## Verification

Named cases and an independent generated-input oracle or operation model accompany the source. Judge results are recorded separately in metadata.
