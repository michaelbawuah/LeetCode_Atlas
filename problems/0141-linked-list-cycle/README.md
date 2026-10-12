# 141 · Linked List Cycle

[LeetCode problem](https://leetcode.com/problems/linked-list-cycle/)

## Intuition
Two speeds distinguish a repeating path from a path that ends.

## Baseline and approach
A visited-node set detects the first repeated reference using O(n) space. Floyd's method advances one pointer by one link and another by two without changing any links. The platform supplies `ListNode`; cycle positions are adapter input, not submission parameters.

## Why it works
Without a cycle, the faster pointer reaches a missing link. With a cycle, both pointers eventually enter it. Their relative position advances one step per iteration modulo the cycle length, so they must coincide within one cycle length. Compare identity, since different nodes may have equal values.

## Complexity
**O(n) time; O(1) space.** Here n is the number of nodes and h is the tree height where relevant. Adapter construction and serialization are separate from submission-method costs.

## Pitfalls
Check both `fast` and `fast.next` before advancing twice. Equal values are not a cycle. A one-node self-link must be detected.

## Follow-up
After a meeting, move one pointer to the head and advance both one step at a time to locate the cycle entry.

## C++23 implementation

C++23 Floyd pointers compare node identity and do not modify the list. `ListArena.build_cycle` links the final borrowed node to the requested position and retains independent ownership, so a cycle cannot cause recursive destruction. The adapter snapshots each distinct reachable node and checks all values and links after detection.

C++23 submission cost: **O(n) time; O(1) space**. Here n is node count, h is tree height, w is maximum level width, and L is the number of returned path elements when applicable. Adapter construction, snapshots, and serialization are measured separately.
