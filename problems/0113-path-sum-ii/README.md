# 113 · Path Sum II

[LeetCode problem](https://leetcode.com/problems/path-sum-ii/)

## Intuition
Record a path only when a leaf completes the requested sum; undo path state when leaving a subtree.

## Baseline and approach
Copying a partial path into every frontier entry can cost O(nh) even with little output. Enter/leave frames maintain one path in O(h) space, and copy it only when it becomes an answer.

## Why it works
An entering frame appends exactly its node to the active root path. Its leaving frame runs after both child regions and removes that same entry. The carried total equals the active path sum; leaf matches are copied into independent result rows. Every root-to-leaf path is considered once.

## Complexity
**O(n + L), L = total returned path elements time; O(h) auxiliary; O(L) output space.** Here n is the number of nodes and h is the tree height where relevant. Adapter construction and serialization are separate from submission-method costs.

## Pitfalls
Appending the mutable path itself would alias all answers. Equal-valued paths through different leaves must retain their multiplicity. Only outer row order is ignored; values within a path stay ordered.

## Follow-up
Count matching paths without materializing them, or extend the condition to paths that may begin below the root.

## C++23 implementation

C++23 enter/leave frames maintain one active path and copy only matching answers, preserving equal-valued path multiplicity. Signed sums fit `int` under the official node-count and value limits. The adapter verifies all original links and values remain unchanged.

C++23 submission cost: **O(n + L), L = total returned path elements time; O(h) auxiliary; O(L) output space**. Here n is node count, h is tree height, w is maximum level width, and L is the number of returned path elements when applicable. Adapter construction, snapshots, and serialization are measured separately.
