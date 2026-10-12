# 1143 · Longest Common Subsequence

[LeetCode problem](https://leetcode.com/problems/longest-common-subsequence/)

## Intuition
Compare prefixes of the two strings. Matching last characters extend a smaller common subsequence; otherwise skip one of the last characters.

## Baseline and approach
Enumerating subsequences of both strings is exponential. A two-dimensional prefix DP takes O(m × n) time; retaining just the previous and current rows reduces storage.

## Why it works
At each cell, previous[column] describes dropping the newest character from the longer string, and current[column−1] describes dropping the newest character from the shorter string. A match extends the diagonal prefix optimum by one; a mismatch chooses the better neighboring optimum. These cases preserve the prefix-optimum invariant row by row.

## Complexity
For lengths m and n: **O(m × n) time, O(min(m, n)) auxiliary space**. The shorter string determines row width.

## Pitfalls
A subsequence may contain gaps; it is not a contiguous substring. Do not combine cells from inconsistent rows. Repeated letters still require respecting the order in both inputs.

## Follow-up
What information would you retain to reconstruct a common subsequence instead of only its length?
