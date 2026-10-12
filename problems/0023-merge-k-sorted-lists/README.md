# 23 · Merge k Sorted Lists

[LeetCode problem](https://leetcode.com/problems/merge-k-sorted-lists/)

## Intuition
The smallest unmerged node must be one of the current list heads.

## Baseline and approach
For k lists containing N total nodes, repeatedly scanning k heads costs O(Nk). A heap retains only those heads and replaces a popped head with its successor.

## Why it works
Each pending entry is the smallest unconsumed node of one input list. Popping the minimum therefore selects the smallest node overall. Appending it and inserting its successor preserves the invariant until all nodes are consumed.

## Complexity
**O(k + N log(k + 1)) time; O(k) auxiliary; existing nodes reused space.** Here n counts nodes, h is height, and w is maximum actual level width when relevant. Special symbols are explained in the approach. Adapter construction and serialization are separate.

## Pitfalls
Equal values need a tie field because Python nodes are not ordered. Reuse nodes without cycles, and terminate the result tail. Empty inputs still require scanning the k slots.

## Follow-up
Compare heap merging with balanced pairwise merging and discuss when either representation is preferable.

## Python and C++23
Both versions maintain one pending head per nonempty list. Python includes a serial tie field because its node objects cannot be ordered; C++ compares pointed-to values directly. Nodes are borrowed, relinked, and never deleted by either submission method. One ListArena owns all local input lists; a result owner is unnecessary.

C++23 submission-method complexity: **O(k + N log(k + 1)) time; O(k) auxiliary; existing nodes reused space**. Adapter ownership and JSON conversion are separate.
