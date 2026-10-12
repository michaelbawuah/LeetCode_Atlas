# 25 · Reverse Nodes in k-Group

[LeetCode problem](https://leetcode.com/problems/reverse-nodes-in-k-group/)

## Intuition
A complete group can be reversed locally once its ending boundary is known.

## Baseline and approach
An array of node references makes group reversal straightforward but uses O(n) space. The pointer implementation first confirms that k nodes remain, then reverses exactly that segment and reconnects it to the prefix and suffix.

## Why it works
The completed prefix already has the required group order. Locating `kth` proves the next group is complete. Initializing the reversed tail with `group_next` preserves the suffix; connecting the predecessor to `kth` installs the new group head. The old first node becomes the next predecessor. An incomplete suffix is never rewired.

## Complexity
**O(n) time; O(1) space.** Here n is the number of nodes and h is the tree height where relevant. Adapter construction and serialization are separate from submission-method costs.

## Pitfalls
Do not reverse a partial final group. Save its following node before modifying links. Using node identity for the stop boundary avoids repeated-value ambiguity.

## Follow-up
What additional state is required if alternating groups should be reversed while the others remain unchanged?
