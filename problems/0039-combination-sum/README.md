# 39 · Combination Sum

[Problem](https://leetcode.com/problems/combination-sum/) · Medium

## Idea

Choose candidates in nondecreasing index order. Reusing the current index allows repeated values; never moving backward prevents generating different permutations of one combination.

**Baseline:** enumerate how many copies of every candidate might fit and check their weighted sum. Backtracking instead prunes a branch as soon as its next sorted candidate exceeds the remaining target.

## Why it works

A recursive call's path uses only allowed candidates and sums to target minus remaining. Because all candidates are positive, adding a value decreases remaining and recursion terminates. Every valid multiset has one nondecreasing representation; keeping the same index for repetition and considering larger indices enumerates it exactly once. Saving only paths with remaining zero yields precisely valid combinations.

## Complexity

Let c be the candidate count, d = floor(target / min(candidates)), and k the number of results. Runtime is output-sensitive and exponential in the worst case; O(c log c + d c^d) is a conservative bound including sorting and path copying. O(c + d) auxiliary storage covers a sorted copy, path, and recursion stack; output uses O(kd) space. The caller's candidate list is preserved.

## Counterexample and checks

Advancing to index + 1 after choosing a candidate would lose `[2, 2, 3]` for target 7. Restarting at index zero generates duplicate reorderings. Fixtures cover reuse and unsorted input; the independent oracle enumerates candidate multiplicity vectors rather than recursive paths.

**Follow-up:** require each candidate to be used at most once, including duplicate values in the input.
