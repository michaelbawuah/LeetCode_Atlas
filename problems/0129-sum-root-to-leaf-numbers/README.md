# 129 · Sum Root to Leaf Numbers

[LeetCode problem](https://leetcode.com/problems/sum-root-to-leaf-numbers/)

## Intuition
A child appends one digit to its root-to-parent number.

## Baseline and approach
Building a digit string for each complete path repeats copying. Carry its numerical prefix instead, multiplying by ten and adding the next digit; only leaves contribute to the sum.

## Why it works
The root begins with prefix zero. Appending a node digit computes exactly the number represented by the path ending there. Passing that value to both children preserves the invariant. Adding only at leaves includes each complete root-to-leaf number once.

## Complexity
**O(n) time; O(h) space.** Here n is the number of nodes and h is the tree height where relevant. Adapter construction and serialization are separate from submission-method costs.

## Pitfalls
An internal node is not a complete number. Leading zero digits still advance the position correctly. The official input is nonempty, digit-valued, and bounds the final result.

## Follow-up
Replace base ten with an arbitrary base and state the required digit bounds.

## C++23 implementation

C++23 carries numerical prefixes on an explicit DFS stack and widens decimal multiplication and the accumulated sum to `int64_t` before returning the officially bounded `int` result. Its adapter checks that every original node value and child link remain unchanged.

C++23 submission cost: **O(n) time; O(h) space**. Here n is node count, h is tree height, w is maximum level width, and L is the number of returned path elements when applicable. Adapter construction, snapshots, and serialization are measured separately.
