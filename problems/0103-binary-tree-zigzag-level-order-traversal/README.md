# 103 · Binary Tree Zigzag Level Order Traversal

[LeetCode problem](https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/)

## Intuition
Keep traversal order consistent and change only each returned row direction.

## Baseline and approach
Depth-first grouping is possible but requires separate ordering logic. BFS collects ordinary left-to-right levels, reversing alternate output rows.

## Why it works
At each round, the queue contains one level from left to right. Processing its original size produces that level and schedules the next in the same order. Reversing every second completed row creates the requested zigzag without changing discovery order.

## Complexity
**O(n) time; O(w) auxiliary; O(n) output space.** Here n counts nodes, h is height, and w is maximum actual level width when relevant. Special symbols are explained in the approach. Adapter construction and serialization are separate.

## Pitfalls
Alternating child enqueue order without carefully tracking the frontier can scramble subsequent levels. Include the temporary reversed row and output in storage accounting.

## Follow-up
Produce zigzag rows with a deque of values rather than reversing a finished list.

## Python and C++23
Both implementations keep discovery left-to-right and reverse alternate output rows. Python creates a reversed row list; C++ reverses its local vector and moves it into the output. Both retain O(w) temporary frontier/row storage and preserve the tree.

C++23 submission-method complexity: **O(n) time; O(w) auxiliary; O(n) output space**. Adapter ownership and JSON conversion are separate.
