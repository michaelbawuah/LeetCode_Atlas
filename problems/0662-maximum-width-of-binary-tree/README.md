# 662 · Maximum Width of Binary Tree

[LeetCode problem](https://leetcode.com/problems/maximum-width-of-binary-tree/)

## Intuition
Logical positions count missing slots between the first and last existing node.

## Baseline and approach
Actual level-node counts miss gaps. Track complete-tree positions, subtracting the first current position each round to keep indexes small on deep sparse trees.

## Why it works
Children occupy twice their parent position and twice plus one. Subtracting a common level offset preserves every positional difference, so last-first+1 still equals the logical width. Left-to-right BFS ensures the last processed relative index determines that width.

## Complexity
**O(n) under the bounded-width contract time; O(w) space.** Here n counts nodes, h is height, and w is maximum actual level width when relevant. Special symbols are explained in the approach. Adapter construction and serialization are separate.

## Pitfalls
The frontier width w counts actual nodes, while the answer includes gaps. Normalize each level to avoid exponentially large absolute indexes on a chain. The official answer fits a signed 32-bit integer.

## Follow-up
Compute the width at every depth and return the deepest level attaining the maximum.
