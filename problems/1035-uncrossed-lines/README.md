# 1035 · Uncrossed Lines

[LeetCode problem](https://leetcode.com/problems/uncrossed-lines/)

## Intuition
Noncrossing matches are exactly order-preserving matches, so they form a common subsequence.

## Baseline and approach
Enumerating index-subsequence pairs is exponential. A rolling LCS table finds the maximum number of order-preserving equal pairs.

## Why it works
Matching equal endpoints extends an optimum from the diagonal prefixes by one. Otherwise an optimum skips an endpoint, represented by the top or left state. Increasing endpoint indices in both arrays prevents crossing, so this recurrence maximizes precisely the legal lines.

## Complexity
Python: **O(m n) time; O(min(m, n)) auxiliary space**. m and n are lengths. O(mn) time and O(min(m,n)) row storage include the saved diagonal. Arrays are swapped by reference and preserved.

## Pitfalls
A value may occur repeatedly, but each position can be used once. Matching every equal pair independently can create crossing or reused positions.

## Follow-up
How would differently weighted matches change the recurrence?

## Verification
Named fixtures and an independent generated-input oracle accompany this implementation. Official judge results are recorded separately in metadata.
