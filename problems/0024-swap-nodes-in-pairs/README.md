# 24 · Swap Nodes in Pairs

[LeetCode problem](https://leetcode.com/problems/swap-nodes-in-pairs/)

## Intuition
Treat each complete pair as one small link-rewiring operation.

## Baseline and approach
Collecting node references in an array makes swaps easy but uses O(n) extra space. A dummy head and a pointer to the completed prefix swap one pair at a time using constant storage.

## Why it works
Before each iteration, all nodes before `previous.next` are correctly paired. Reconnecting the predecessor, second node, first node, and untouched suffix swaps exactly the next two nodes. The former first node becomes the predecessor for the following pair. A final unmatched node remains unchanged.

## Complexity
**O(n) time; O(1) space.** Here n is the number of nodes and h is the tree height where relevant. Adapter construction and serialization are separate from submission-method costs.

## Pitfalls
Swap references rather than values. Keep access to the suffix before replacing the pair's links. An odd final node must survive.

## Follow-up
Generalize the rewiring to complete groups of k nodes.

## Python and C++23
Both implementations swap existing nodes with a dummy predecessor and O(1) pointer state. The C++ adapter owns the nodes through ListArena; submission code borrows and rewires them without deleting any node.

C++23 submission-method complexity: **O(n) time; O(1) space**. Adapter ownership and JSON conversion costs are separate.
