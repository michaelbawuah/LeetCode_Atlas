# 354 · Russian Doll Envelopes

[LeetCode problem](https://leetcode.com/problems/russian-doll-envelopes/)

## Intuition
Sort widths upward, then reduce nesting to a strictly increasing subsequence of heights.

## Baseline and approach
An exhaustive chain search or quadratic pairwise DP is the baseline. Binary-searched minimal tails compute the height LIS after sorting.

## Why it works
Widths increase in sorted order. Equal-width envelopes are ordered by decreasing height, so no increasing height subsequence can use two equal widths. For each subsequence length, the stored tail is the smallest achievable ending height, preserving every possible future extension. Its count is therefore the maximum valid nesting depth.

## Complexity
Python: **O(n log n) time; O(n) auxiliary space**. n is envelope count. Sorting a copy and storing LIS tails use O(n) space and O(n log n) time; the input is preserved.

## Pitfalls
Equal widths must use descending heights. Both dimensions must increase strictly; equal heights replace a tail instead of extending it.

## Follow-up
How would predecessor indices reconstruct the actual envelope chain?

## Verification
Named fixtures and an independent generated-input oracle accompany this implementation. Official judge results are recorded separately in metadata.
