# 206 · Reverse Linked List

[LeetCode problem](https://leetcode.com/problems/reverse-linked-list/)

## Intuition
Move one node at a time from the front of the unreversed suffix to the front of the reversed prefix.

## Baseline and approach
Copying values into an array and rebuilding a list costs O(n) extra space. The iterative solution instead rewires each existing node using `previous`, `current`, and a saved next pointer. The platform supplies `ListNode`; the local adapter does the same.

## Why it works
Before each iteration, `previous` heads the reversed processed prefix and `current` heads the untouched suffix. Saving `current.next` preserves access to the suffix; redirecting that pointer and advancing both heads extends the invariant by one node. When the suffix is empty, `previous` heads the complete reversed list.

## Complexity
For n nodes: **O(n) time, O(1) auxiliary space**. Nodes are reused.

## Pitfalls
Save the next pointer before overwriting it. Returning the original head would return the new tail. The empty list naturally returns `None`.

## Follow-up
Reverse only the nodes between two positions while preserving the surrounding links.
