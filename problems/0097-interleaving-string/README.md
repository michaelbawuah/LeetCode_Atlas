# 97 · Interleaving String

[LeetCode problem](https://leetcode.com/problems/interleaving-string/)

## Intuition
A prefix of the result ends with the next available character from one of the two source prefixes.

## Baseline and approach
Enumerating all choices of positions for the first source is exponential. Prefix-pair reachability uses a rolling Boolean row, with the shorter source across columns.

## Why it works
At row i and column j, the target character has index i+j−1. Reachability comes from the previous row when the first source supplies that character, or the current row’s previous column when the second source supplies it. These are all legal final choices and preserve both source orders. Boundaries correspond to using only one source.

## Complexity
For source lengths m and n, **O(mn + m + n + 1) time and O(min(m, n) + 1) auxiliary space**. Swapping the sources changes only references and preserves the problem’s symmetry.

## Pitfalls
Check total length before indexing. Preserving order inside each source matters; matching combined character frequencies is insufficient. Empty strings and repeated characters are valid.

## Follow-up
How would the same state graph count all valid interleavings instead of only reporting existence?

## Verification
Named fixtures and independent generated-input references accompany the implementation. Official judge results are tracked separately in metadata.
