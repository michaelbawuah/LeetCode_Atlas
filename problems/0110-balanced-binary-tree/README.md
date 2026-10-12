# 110 · Balanced Binary Tree

[LeetCode problem](https://leetcode.com/problems/balanced-binary-tree/)

## Intuition
A node's balance can be decided once both child heights are known. Every node, rather than just the root, must satisfy the height difference bound.

## Baseline and approach
Recomputing each subtree height separately can take O(n²) time. An iterative postorder traversal computes each height once and caches it by node. A visited flag delays the parent until after its children, avoiding recursion on deep input.

## Why it works
An unvisited node schedules its children before its final processing. When the node is processed, both cached child heights are correct. Rejecting a difference greater than one detects a violating node; otherwise its height is one plus the greater child height. Completing the traversal establishes the balance condition everywhere.

## Complexity
For n nodes: **O(n) time, O(n) auxiliary space**, because computed heights remain in the dictionary. This iterative version trades that storage for freedom from Python's recursion limit.

## Pitfalls
Similar heights at the root can hide an unbalanced subtree. Measure subtree heights, not immediate child counts.

## Follow-up
Can an explicit traversal frame return heights to its parent while retaining only O(h) memory?
