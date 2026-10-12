# 1448 · Count Good Nodes in Binary Tree

[LeetCode problem](https://leetcode.com/problems/count-good-nodes-in-binary-tree/)

## Intuition
A node qualifies when its value reaches the maximum of its ancestor path.

## Baseline and approach
Rechecking every root path costs O(nh). Retain its maximum while exploring each branch.

## Why it works
Each frontier entry contains the greatest value on the path before its node. Comparing with that bound decides qualification exactly; updating it before scheduling children preserves the same meaning for their paths. Every node is evaluated once.

## Complexity
**O(n) time; O(h) space.** Here n counts nodes, h is height, and w is maximum actual level width when relevant. Special symbols are explained in the approach. Adapter construction and serialization are separate.

## Pitfalls
Equality qualifies. A zero initial bound would reject a negative root incorrectly; initialize from the actual root. Sibling paths need independent maxima.

## Follow-up
Count nodes whose value is among the top r values of their root path using an ordered ancestor structure.

## Python and C++23
Both versions keep an ancestor maximum in each explicit frontier entry. Equality qualifies, and negative roots initialize the bound from their actual value. TreeArena owns all borrowed nodes, whose values and links remain unchanged.

C++23 submission-method complexity: **O(n) time; O(h) space**. Adapter ownership and JSON conversion are separate.
