# 19 · Remove Nth Node From End of List

[LeetCode problem](https://leetcode.com/problems/remove-nth-node-from-end-of-list/)

## Intuition
Keep two pointers n positions apart. When the front pointer reaches the last node, the rear pointer sits immediately before the node to remove.

## Baseline and approach
A two-pass solution first counts the nodes, then walks to the predecessor. A dummy head and a fixed pointer gap perform the removal in one traversal after establishing the gap. The platform supplies `ListNode`.

## Why it works
After advancing `fast` n links, the gap remains n because both pointers subsequently move together. At termination `fast` is the tail, placing `slow.next` exactly n nodes from the end. Bypassing that one node preserves every other link's order. The dummy handles removing the real head.

## Complexity
For L nodes: **O(L) time, O(1) auxiliary space**. The output reuses the remaining input nodes.

## Pitfalls
The dummy pointer and the loop condition form one consistent convention; mixing this with an n+1-step variant causes an off-by-one error. The problem guarantees 1 ≤ n ≤ L.

## Follow-up
How would the interface change if the caller needed the removed node as well as the new head?

## Python and C++23 comparison

Both versions keep two pointers a fixed distance apart and bypass one node, taking O(L) time and O(1) auxiliary space for L nodes. The C++ dummy node lives on the stack. Its raw pointers borrow input nodes: removing a node detaches it without deleting it, because the judge or the test adapter owns its lifetime. `ListArena` retains ownership of every allocated test node, including the detached node, and releases them when the arena is destroyed. That O(L) harness allocation is separate from the algorithm's O(1) working space. Python similarly returns the remaining existing nodes rather than rebuilding the list.
