# 236 · Lowest Common Ancestor of a Binary Tree

[LeetCode problem](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/)

## Intuition
Parent references turn ancestry into two upward walks.

## Baseline and approach
Recursive postorder can combine target discoveries but risks call-depth failure on long chains. An iterative discovery map records parent links until both targets are found, then intersects their ancestor chains.

## Why it works
Discovery assigns each reachable node its actual parent. The set built from p contains exactly its ancestors, including p. Walking upward from q encounters its common ancestors from lowest to highest; the first set member is therefore the lowest common ancestor.

## Complexity
**O(n) expected time; O(n) space.** Here n counts nodes, h is height, and w is maximum actual level width when relevant. Special symbols are explained in the approach. Adapter construction and serialization are separate.

## Pitfalls
The targets are original node references, not just matching values. The source preserves all links. Expected map/set costs are qualified, and retained parent entries use O(n) space.

## Follow-up
Return an LCA for repeated queries after preprocessing depth and ancestor jumps.

## C++23 implementation

C++23 uses an iterative enter/leave traversal with one active root path and copies the paths only when the actual p and q pointers are found. Their last common prefix node is the LCA. This gives deterministic O(n) time and O(h) auxiliary space, including the two saved paths; it avoids the Python version’s retained parent hash map. `TreeReferences` validates original result identity and an unchanged tree.

C++23 submission cost: **O(n) time; O(h) space**. Here n is node count, h is tree height, w is maximum level width, and L is the number of returned path elements when applicable. Adapter construction, snapshots, and serialization are measured separately.
