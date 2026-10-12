# 40 · Combination Sum II

[LeetCode problem](https://leetcode.com/problems/combination-sum-ii/)

## Intuition
Choose a value and advance past its position because each candidate is available once. Equal values at one search depth share a single branch.

## Baseline and approach
Enumerating all position subsets and deduplicating value combinations is the baseline. Sorted backtracking skips duplicate siblings and stops when a positive candidate exceeds the remaining target.

## Why it works
Path uses only positions before the current start, and its sum is target minus remaining. Advancing to index+1 prevents reuse. Equal siblings would produce identical value choices, so skipping later copies removes duplication without losing combinations that use multiple copies at different depths. Every valid combination follows one remaining canonical branch.

## Complexity
For n candidates and K answers, a conservative bound is **O(n log n+n2^n) time and O(n) auxiliary space**, with **O(Kn)** output storage. Sorting a copy leaves the input unchanged.

## Pitfalls
This differs from unlimited-reuse Combination Sum: recurse from index+1. Positive values justify the early break. Equal candidates are separate available positions, but answers are unique value multisets.

## Follow-up
How would zeros or negative candidates change the pruning rule and target-zero base case?

## Verification
Named fixtures and independent generated-input references accompany the implementation. Official judge results are tracked separately in metadata.

## C++23 counterpart

C++ sorts a copy, preserving the caller input. Equal siblings are skipped while different depths may consume further equal values. Positive candidates justify early pruning, and each answer path is copied. Multiplicity is preserved by the unordered-groups checker.

Time: O(n log n + n 2^n) conservative bound. Space: O(n) auxiliary; O(K n) output.

The JSON adapter creates fresh state per case. Named fixtures and 150 deterministic generated inputs compare the two language implementations; existing independent Python oracles supply a separate behavioral reference.
