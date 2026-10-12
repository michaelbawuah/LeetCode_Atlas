# 647 · Palindromic Substrings

[LeetCode problem](https://leetcode.com/problems/palindromic-substrings/)

## Intuition
Each successful outward expansion identifies one palindrome by its start and end positions.

## Baseline and approach
The direct baseline checks all slices and reverses them, costing O(n³). Expanding around odd and even centers avoids rescanning interiors.

## Why it works
Each expansion maintains a palindrome by adding equal endpoints to a previously valid interior. Each position-distinct palindrome has exactly one center and radius, so it is counted once. Equal substring text at different positions still contributes separate occurrences.

## Complexity
For length n, **O(n²) time and O(1) auxiliary space**.

## Pitfalls
Count single-character substrings and even centers. A set of substring values loses repeated occurrences: three identical characters have six palindromic substrings, not three distinct string values.

## Follow-up
Can you sum palindrome radii from a linear-time center-radius algorithm?

## Verification
Named fixtures and independent generated-input references accompany the implementation. Official judge results are tracked separately in metadata.
