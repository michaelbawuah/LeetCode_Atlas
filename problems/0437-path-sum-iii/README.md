# 437 · Path Sum III

[LeetCode problem](https://leetcode.com/problems/path-sum-iii/)

## Intuition
Two prefixes on the same root path differ by the sum of the downward segment between them.

## Baseline and approach
Starting a new sum walk at every node can take O(n²). Count matching earlier prefixes on the active ancestor path, and remove them when leaving a subtree.

## Why it works
Before visiting a node, the prefix frequencies describe exactly its ancestors plus the empty root prefix. Every occurrence of prefix-target identifies one matching downward path ending here. Adding the current prefix enables descendants; its leaving frame removes it before a sibling is explored, so unrelated branches never combine.

## Complexity
**O(n) expected time; O(h) space.** Here n counts nodes, h is height, and w is maximum actual level width when relevant. Special symbols are explained in the approach. Adapter construction and serialization are separate.

## Pitfalls
Frequencies, rather than a set, are necessary for repeated prefixes such as zeros. Delete zero-count entries to retain O(h) active state. Negative values invalidate positive-sum pruning.

## Follow-up
Count paths whose sums lie in an interval using an ordered structure for active prefix values.
