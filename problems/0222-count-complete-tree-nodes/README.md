# 222 · Count Complete Tree Nodes

[LeetCode problem](https://leetcode.com/problems/count-complete-tree-nodes/)

## Intuition
Equal extreme heights identify a perfect subtree within a complete tree.

## Baseline and approach
Visiting every node takes O(n). Count perfect subtrees from their height and only split regions whose final level is incomplete.

## Why it works
Completeness means a subtree with equal leftmost and rightmost heights contains every position through that height, so its count is 2^height-1. Otherwise counting its root and both child regions partitions its nodes exactly. Only one incomplete region persists per depth; height scans across those regions and perfect siblings sum to O(log²(n+1)).

## Complexity
**O(log^2(n + 1)) time; O(log(n + 1)) space.** Here n counts nodes, h is height, and w is maximum actual level width when relevant. Special symbols are explained in the approach. Adapter construction and serialization are separate.

## Pitfalls
Equal extreme heights do not certify perfection for an arbitrary tree; the complete-tree guarantee is essential. Height counts nodes, and empty input counts zero.

## Follow-up
Binary-search the occupied positions in the final level using a root-to-position existence test.

## Python and C++23
Both versions count perfect subtrees through equal extreme heights under the complete-tree contract. C++ widens the shift before producing a subtree count; the bounded node count keeps heights and the returned int safe. Input links are untouched.

C++23 submission-method complexity: **O(log^2(n + 1)) time; O(log(n + 1)) space**. Adapter ownership and JSON conversion are separate.
