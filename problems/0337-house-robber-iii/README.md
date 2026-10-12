# 337 · House Robber III

[LeetCode problem](https://leetcode.com/problems/house-robber-iii/)

## Intuition
For each subtree, retain separate best totals when its root is taken and when it is skipped.

## Baseline and approach
Enumerating all nonadjacent node subsets is exponential. Iterative postorder computes each subtree’s two outcomes once.

## Why it works
Taking a node forces both child roots to be skipped. Skipping it permits either outcome independently for each child. Once child states are ready, these two cases cover all legal selections in the parent subtree. Their maximum at the root is globally optimal.

## Complexity
Python: **O(n) expected time; O(n) auxiliary space**. n is node count. Each node is visited a constant number of times; expected dictionary lookup cost gives O(n) time. The outcome map uses O(n) space in addition to the O(h) traversal stack.

## Pitfalls
Use node identity as the map key: duplicate values are different houses. The enter/ready stack avoids Python recursion failure on a legal 10,000-node chain. The tree is not modified.

## Follow-up
Can child outcomes be discarded after their parent is processed to reduce retained storage?

## Verification
Named fixtures and an independent generated-input oracle accompany this implementation. Official judge results are recorded separately in metadata.

## C++23 implementation

C++23 explicit postorder frames carry each child’s take/skip outcomes back to its parent and discard the completed frame. This gives deterministic O(n) time and O(h) auxiliary space without a hash map or native recursion. The officially bounded node values and 10,000-node limit keep totals within signed `int`; the adapter verifies all original links and values remain unchanged.

C++23 submission cost: **O(n) time; O(h) space**. Here n is node count, h is tree height, w is maximum level width, and L is the number of returned path elements when applicable. Adapter construction, snapshots, and serialization are measured separately.
