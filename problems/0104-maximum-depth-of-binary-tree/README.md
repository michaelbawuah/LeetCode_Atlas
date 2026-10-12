# 104 · Maximum Depth of Binary Tree

[LeetCode problem](https://leetcode.com/problems/maximum-depth-of-binary-tree/)

## Intuition
Depth is the number of nodes on a root-to-leaf path. Carry each node's depth while traversing the tree and retain the largest value.

## Baseline and approach
Recursive DFS uses the recurrence `1 + max(left_depth, right_depth)`. An explicit stack implements the same traversal without Python's recursion-depth limit, which matters for a long chain. An absent root has depth zero. The platform supplies `TreeNode`.

## Why it works
The root enters the stack at depth one. Each pushed child receives exactly its parent's depth plus one, so every visited depth is correct. Every node is visited once, and the maximum visited depth equals the longest root-to-leaf path.

## Complexity
For n nodes and tree height h: **O(n) time, O(h) auxiliary space**. The DFS stack stores pending siblings along a path. A chain actually needs only one pending node, while O(h) is the general bound.

## Pitfalls
Count nodes rather than edges. Using recursive DFS on a valid deeply skewed tree can exceed Python's default recursion limit.

## Follow-up
Return a deepest path as well as its length, without copying every partial path.
