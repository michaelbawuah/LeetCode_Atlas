# 82 · Remove Duplicates from Sorted List II

[LeetCode problem](https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/)

## Intuition
Sorted input places every occurrence of a value in one contiguous run.

## Baseline and approach
Counting values with a dictionary works with O(n) storage. The pointer scan locates each run and keeps it only when its first and last node are the same.

## Why it works
The completed prefix contains exactly previously seen singleton runs. A one-node run is retained; a longer run is bypassed entirely. Advancing to the next run applies the same condition to every value, leaving only values that originally occurred once.

## Complexity
**O(n) time; O(1) space.** Here n counts nodes, h is height, and w is maximum actual level width when relevant. Special symbols are explained in the approach. Adapter construction and serialization are separate.

## Pitfalls
This problem removes the entire repeated run, rather than keeping one occurrence. A dummy handles repeated values at the head. Detach borrowed nodes without assuming ownership of their deletion.

## Follow-up
Remove values whose multiplicity exceeds an arbitrary threshold while preserving original node identities.

## Python and C++23
Both versions discard entire repeated runs while preserving singleton nodes. C++ detaches links without deleting borrowed nodes; ListArena retains ownership even for nodes absent from the returned head.

C++23 submission-method complexity: **O(n) time; O(1) space**. Adapter ownership and JSON conversion are separate.
