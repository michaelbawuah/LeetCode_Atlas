# 417 · Pacific Atlantic Water Flow

[Problem](https://leetcode.com/problems/pacific-atlantic-water-flow/) · Medium

## Idea

Searching downhill from every cell repeats work. Reverse the direction: begin at each ocean's borders and move to equal or higher neighbors. Intersect the two reached sets.

**Baseline:** run a downhill reachability search from each cell, requiring O((rows × cols)²) worst-case time. Two reverse searches share that work.

## Why it works

A forward step from a higher cell to an equal or lower cell exists exactly when the reverse uphill step exists in the reversed graph. Thus reverse reachability from Pacific borders identifies precisely cells that can reach the Pacific; the same argument applies to the Atlantic. Their intersection is exactly the requested set. Both searches mark cells before pushing them, so equal-height cycles terminate.

## Complexity

O(rows × cols) time and O(rows × cols) total storage, including reached sets, traversal stacks, and output. The heights matrix is not modified.

## Counterexample and checks

A strict uphill comparison loses flat terrain: equal-height neighbors may exchange water. A low center enclosed by high cells must also stay excluded even when every boundary cell reaches both oceans. The generated oracle runs a forward downhill search independently from every starting cell. Coordinate order within `[row, col]` matters; ordering between coordinates does not.

**Follow-up:** intersect reachability from three or more boundary regions using a bitmask per cell.

## Python and C++23 comparison

Both implementations search uphill from each ocean border and intersect the reached sets. C++ uses owned boolean matrices and explicit stacks, with no recursive depth risk and no modification of the heights matrix. O(rows × cols) time and auxiliary storage exclude the O(rows × cols) maximum coordinate output and runner input copy. The shared checker ignores ordering between coordinate rows while preserving each `[row, col]` pair.
