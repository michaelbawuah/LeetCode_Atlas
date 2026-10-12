# 90 · Subsets II

[LeetCode problem](https://leetcode.com/problems/subsets-ii/)

## Intuition
Equal values must not create duplicate choices at the same search depth, while deeper calls may still choose additional copies.

## Baseline and approach
Enumerating index masks and deduplicating their value multisets is the baseline. Sort a copy, then skip equal siblings during backtracking.

## Why it works
At a call starting at an index, path is one valid subset and is emitted once. Choosing the first occurrence of each available value covers every distinct next value. Recursing beyond that occurrence permits further copies, so multiplicities are preserved while equal sibling branches are excluded.

## Complexity
For n values, **O(n log n+n2^n) time and O(n) auxiliary space** for sorting, the path, and recursion. Output is bounded by **O(n2^n)**. Sorting a copy preserves the original input.

## Pitfalls
Skip duplicates only when index > start. Skipping every repeated value globally would remove subsets containing multiple copies. Empty subset is always one answer even though the input is nonempty.

## Follow-up
How could a frequency representation choose a count from zero through each value’s multiplicity?

## Verification
Named fixtures and independent generated-input references accompany the implementation. Official judge results are tracked separately in metadata.

## C++23 counterpart

C++ sorts a copy and emits each current path once. Skip equal siblings only at the current depth so subsets can still contain multiple occurrences. The checker ignores answer and subset order while retaining duplicate counts.

Time: O(n log n + n 2^n). Space: O(n) auxiliary; O(n 2^n) output.

The JSON adapter creates fresh state per case. Named fixtures and 150 deterministic generated inputs compare the two language implementations; existing independent Python oracles supply a separate behavioral reference.
