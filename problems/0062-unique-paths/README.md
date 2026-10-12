# 62 · Unique Paths

[LeetCode problem](https://leetcode.com/problems/unique-paths/)

## Intuition
Every interior cell is reached from above or from its left neighbor. Add those two route counts.

## Baseline and approach
Enumerating right/down routes repeats many suffixes. A grid DP counts paths once per cell, and a rolling row retains only the states needed for the next update.

## Why it works
Before updating a cell, paths[column] counts routes to the cell above, while paths[column−1] already counts routes to the cell on its left in the current row. Their sum covers the disjoint possible final moves. The first row and first column each have one route, establishing the boundary counts.

## Complexity
For an m by n grid: **O(m × n) time, O(min(m, n)) auxiliary space**.

## Pitfalls
The starting cell counts as one route, including a 1 by 1 grid. Update from left to right so the left count belongs to the current row. Rotating dimensions preserves the route count and reduces storage.

## Follow-up
How would blocked cells change initialization and the cell update?

## C++23 counterpart
The C++23 counterpart matches O(mn) time/O(min(m,n)) auxiliary space and uses int64_t for row additions. Every partial-cell path count can be extended to the bottom-right cell, so it is no larger than the guaranteed-bounded final count. The final conversion to int is therefore valid.
