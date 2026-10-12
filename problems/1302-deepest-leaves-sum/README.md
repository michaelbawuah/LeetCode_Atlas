# 1302 · Deepest Leaves Sum

[LeetCode problem](https://leetcode.com/problems/deepest-leaves-sum/)

## Intuition
A newly reached depth replaces the previous sum; another node at that depth extends it.

## Baseline and approach
BFS can retain the final level sum. An explicit DFS carries depth and keeps one best-depth aggregate instead of a potentially wide frontier.

## Why it works
After each visit, total is the sum of all visited nodes at the greatest visited depth. A deeper visit resets that aggregate; equal-depth visits add to it. Once traversal finishes, nodes at maximum depth are necessarily leaves, so the aggregate is the deepest-leaf sum.

## Complexity
**O(n) time; O(h) space.** Here n counts nodes, h is height, and w is maximum actual level width when relevant. Special symbols are explained in the approach. Adapter construction and serialization are separate.

## Pitfalls
Do not add shallower leaves after a deeper one is known. Reset both depth and total together. Positive-valued input includes at least one node.

## Follow-up
Compute the deepest-leaf count and average with the same depth-based aggregate.
