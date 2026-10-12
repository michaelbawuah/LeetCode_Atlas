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

## C++23 counterpart

Every count update uses only nonnegative addition and copying. Clamping each count to INT_MAX commutes with these operations: min(M, min(M, a) + min(M, b)) = min(M, a + b). Each sum is widened to int64_t before addition and then clamped. The guaranteed final answer fits int, so its clamped value remains exact even when unrelated intermediate counts exceed 64 bits. Length comparisons do not depend on counts. A longer candidate replaces both optimum and count, while tied predecessor counts are added with saturation; this preserves the length/count invariant with the count clamped. The regression has 70 repeated positive layers (2^70 selections), followed by one unique negative chain of length 71, so its final longest-subsequence count is one. Two O(n) arrays store fixed-width lengths and counts.

C++: **O(n²) time; O(n) fixed-width length/count states space**. Named fixtures and 150 reproducible generated inputs compare this implementation with the Python track.
