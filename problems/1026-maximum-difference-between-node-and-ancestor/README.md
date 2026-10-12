# 1026 · Maximum Difference Between Node and Ancestor

[LeetCode problem](https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/)

## Intuition
Only the smallest and largest value on the current ancestor path can maximize a later difference.

## Baseline and approach
Comparing every node with its complete ancestor list can cost O(nh). Carry the two extrema instead of the list.

## Why it works
Updating the extrema includes exactly the root-to-current path. Their difference is achieved by two nodes on that path, one ancestral to the other. Every ancestor-descendant pair appears in some visited path and is bounded by that path's extrema, so the greatest recorded range is the desired maximum.

## Complexity
**O(n) time; O(h) space.** Here n counts nodes, h is height, and w is maximum actual level width when relevant. Special symbols are explained in the approach. Adapter construction and serialization are separate.

## Pitfalls
Values from different sibling branches must never combine. Carry separate extrema in each frontier entry. The input contains at least two nodes.

## Follow-up
Return the ancestor and descendant achieving the maximum by carrying references with each extremum.
