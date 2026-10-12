# 454 · 4Sum II

[Problem](https://leetcode.com/problems/4sum-ii/) · Medium

## Idea and approaches

Count sums from the first two arrays, then query their negations for each pair from the last two. Enumerating all four index choices is the O(n^4) baseline.

## Correctness invariant

Each first-half sum count is the number of distinct index pairs producing it. A third/fourth pair completes a zero-sum quadruple exactly with first-half sum equal to its negation. Adding that frequency counts every valid four-index combination once, including different indices with equal values.

## Complexity

O(n^2) expected time and O(n^2) auxiliary space for equal input lengths n. Scalar output counts index combinations; all four inputs are preserved.

## Verification and pitfalls

The oracle explicitly enumerates the Cartesian product. Cases include duplicate-index multiplicities, no solution, and the official integer endpoints.

This is not the unique-value quadruplet problem: deduplicating the inputs would remove legitimate index combinations.

**Follow-up:** How would you balance the two halves for unequal array lengths?

## Python and C++23

C++ receives all four vectors by reference, uses long long pair keys and accumulation, and returns an int count. At n <= 200 the maximum n^4 count fits signed int. Hash operations give expected rather than guaranteed worst-case constant lookup. The JSON adapter owns decoded inputs; its conversion copies are outside the solution bounds.
