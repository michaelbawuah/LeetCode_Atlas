# 513 · Find Bottom Left Tree Value

[LeetCode problem](https://leetcode.com/problems/find-bottom-left-tree-value/)

## Intuition
The first queued node of the final BFS level is the desired value.

## Baseline and approach
Tracking every depth and its nodes stores the whole traversal. BFS needs only its frontier and the current level's first value.

## Why it works
Child enqueue order preserves left-to-right level order. Each round replaces the answer with that level's first value; when the frontier empties, the last such value belongs to the deepest level.

## Complexity
**O(n) time; O(w) space.** Here n counts nodes, h is height, and w is maximum actual level width when relevant. Special symbols are explained in the approach. Adapter construction and serialization are separate.

## Pitfalls
The deepest leftmost node need not follow only left-child links. A right-only chain still has one leftmost node at each level.

## Follow-up
Find the bottom-right value by changing only the level-selection rule.

## Python and C++23
Both versions retain the first value from each left-to-right level. The last retained value is the deepest leftmost node; frontier width rather than tree height bounds BFS storage. Input nodes remain unchanged.

C++23 submission-method complexity: **O(n) time; O(w) space**. Adapter ownership and JSON conversion are separate.
