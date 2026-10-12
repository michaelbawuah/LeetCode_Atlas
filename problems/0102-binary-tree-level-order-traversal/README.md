# 102 · Binary Tree Level Order Traversal

[LeetCode problem](https://leetcode.com/problems/binary-tree-level-order-traversal/)

## Intuition
A queue visits parents before their children. Freezing the queue's length at the start of a round separates one depth from the next.

## Baseline and approach
DFS could group values by depth, but must preserve left-to-right order. BFS makes that ordering explicit: remove exactly the current queue size, append their values, and enqueue each left child before its right child. The platform supplies `TreeNode`.

## Why it works
At each round's start, the queue contains exactly the current level in left-to-right order. Processing its original size consumes that level only. Enqueuing children left before right produces the next level in the same order, preserving the invariant until the queue is empty.

## Complexity
For n nodes and maximum level width w: **O(n) time, O(w) auxiliary space**, plus **O(n) output storage**. During a round the queue may contain parts of two adjacent levels, still O(w).

## Pitfalls
Do not keep processing until the queue empties inside a level: newly enqueued children belong to the next level. `deque.popleft()` avoids the linear shifting cost of a list's `pop(0)`.

## Follow-up
Adapt the traversal to zigzag output without changing the actual child-enqueue order.

## C++23 implementation

C++23 freezes the queue size at each level and enqueues left before right. Its adapter verifies every original node value and child link remain unchanged.

C++23 submission cost: **O(n) time; O(w) auxiliary; O(n) output space**. Here n is node count, h is tree height, w is maximum level width, and L is the number of returned path elements when applicable. Adapter construction, snapshots, and serialization are measured separately.
