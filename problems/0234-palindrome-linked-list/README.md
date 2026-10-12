# 234 · Palindrome Linked List

[LeetCode problem](https://leetcode.com/problems/palindrome-linked-list/)

## Intuition
A reversed second half exposes symmetric positions through forward pointers.

## Baseline and approach
Copying values and comparing with their reverse takes O(n) space. The implementation finds the first-half endpoint, reverses the second half, compares corresponding values, then restores the original links before returning.

## Why it works
The first half has the same length as the reversed second half, except for the unpaired middle node in an odd-length list. Comparing the latter's entire length checks every symmetric pair exactly once. Reversing it again restores both its order and the midpoint connection, including after a mismatch.

## Complexity
**O(n) time; O(1) space.** Here n is the number of nodes and h is the tree height where relevant. Adapter construction and serialization are separate from submission-method costs.

## Pitfalls
Returning immediately on a mismatch would skip restoration. The odd middle value needs no partner. Restoration should preserve the exact node identities and links.

## Follow-up
If reversing links is forbidden, compare the O(n)-space array approach with a stack holding only one half.

## C++23 implementation

C++23 records mismatches without returning early, then reverses the second half back and reconnects it. The adapter verifies every original pointer, value, and next link after both successful and unsuccessful comparisons, so restored values alone cannot conceal lost or replaced nodes.

C++23 submission cost: **O(n) time; O(1) space**. Here n is node count, h is tree height, w is maximum level width, and L is the number of returned path elements when applicable. Adapter construction, snapshots, and serialization are measured separately.
