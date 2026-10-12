# 673 · Number of Longest Increasing Subsequence

[LeetCode problem](https://leetcode.com/problems/number-of-longest-increasing-subsequence/)

## Intuition
At each endpoint, record both the longest achievable length and how many subsequences achieve it.

## Baseline and approach
Enumerating all position subsequences is exponential. Pairwise endpoint DP aggregates counts only from predecessors that establish or tie the best length.

## Why it works
A longer predecessor candidate replaces the endpoint’s old optimum and count; a tied candidate adds independent selections with a different previous endpoint. Shorter candidates cannot contribute to a longest subsequence ending here. Summing counts at globally longest endpoints covers every longest selection once.

## Complexity
Python: **O(n²) arithmetic operations time; O(n) integer states auxiliary space**. n is number count. O(n²) counts comparisons and arithmetic operations; Python avoids overflow if intermediate counts grow beyond the guaranteed-bounded final answer. Length/count arrays use O(n) integer states.

## Pitfalls
Strict increase excludes equal predecessor values. Equal values at distinct positions still form separate length-one selections. Never add counts from shorter candidates.

## Follow-up
How could a Fenwick tree aggregate length/count pairs in O(n log n) time?

## Verification
Named fixtures and an independent generated-input oracle accompany this implementation. Official judge results are recorded separately in metadata.
