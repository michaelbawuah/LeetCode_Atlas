# 100 · Same Tree

[LeetCode problem](https://leetcode.com/problems/same-tree/)

## Intuition
Equal value sequences are insufficient: matching positions must contain matching values or both be absent.

## Baseline and approach
Recursive comparison descends into corresponding children. An explicit stack stores pairs of corresponding nodes, rejecting a missing-node mismatch or unequal values immediately.

## Why it works
The stack starts with corresponding roots. For every nonempty equal-valued pair, its left and right child pairs are the next corresponding positions. If every pair agrees, all positions and values agree; any rejected pair supplies a direct counterexample.

## Complexity
For n and m input nodes and heights hp and hq: **O(n+m) worst-case time, O(hp+hq) auxiliary space**. Mismatches may return much earlier.

## Pitfalls
Traversal values without null markers lose shape information. Comparing node identity would reject separate trees with identical structure.

## Follow-up
How would comparison change if swapping the two children at any node were allowed?
