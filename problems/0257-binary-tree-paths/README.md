# 257 · Binary Tree Paths

[LeetCode problem](https://leetcode.com/problems/binary-tree-paths/)

## Intuition
Keep one active root path and emit its string only at a leaf.

## Baseline and approach
Copying a partial path string at every edge can cost O(nh). Enter/leave frames maintain a single path; joining it at leaves accounts directly for required output characters.

## Why it works
Entering appends the current node and leaving removes it after both child regions. The active path therefore equals the root-to-current route. Leaves emit every complete route once, preserving duplicate-valued paths through distinct leaves.

## Complexity
**O(n + L), L = total output characters time; O(h) auxiliary; O(L) output space.** Here n counts nodes, h is height, and w is maximum actual level width when relevant. Special symbols are explained in the approach. Adapter construction and serialization are separate.

## Pitfalls
Internal prefixes are not complete paths. Copy output content at leaves rather than retaining the mutable path list. Outer result order is irrelevant; characters within each path are ordered.

## Follow-up
Return paths satisfying a predicate while preserving the same enter/leave state.
