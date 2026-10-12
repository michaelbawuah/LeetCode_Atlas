# 543 · Diameter of Binary Tree

[LeetCode problem](https://leetcode.com/problems/diameter-of-binary-tree/)

## Intuition
The longest path with a chosen highest node combines its left and right subtree heights.

## Baseline and approach
Repeatedly computing subtree depths at every node can take O(n²) time. A postorder traversal computes each height once, caches it, and updates the greatest combined child height.

## Why it works
Child heights are known before their parent is processed. A path joining the deepest node on each side has `left_height + right_height` edges through that parent. Every tree path has a highest node, so checking all parents considers the diameter. The cached parent height keeps only its longer branch for ancestors.

## Complexity
**O(n) time; O(n) space.** Here n is the number of nodes and h is the tree height where relevant. Adapter construction and serialization are separate from submission-method costs.

## Pitfalls
The answer counts edges, while cached subtree heights count nodes. The longest path may lie entirely below the root. A singleton therefore has diameter zero.

## Follow-up
Recover the two endpoint nodes, or use two graph traversals to find the diameter with a different invariant.

## Python and C++23
Both versions cache child heights by node identity and use explicit postorder frames. C++ unordered-map accesses make the O(n) time bound expected; retained height entries use O(n) auxiliary space. Input nodes remain borrowed and unchanged.

C++23 submission-method complexity: **O(n) expected with unordered-map height storage time; O(n) space**. Adapter ownership and JSON conversion costs are separate.
