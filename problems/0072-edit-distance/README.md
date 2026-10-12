# 72 · Edit Distance

[LeetCode problem](https://leetcode.com/problems/edit-distance/)

## Intuition
An optimal prefix transformation ends with inserting, deleting, or replacing the newest character; equal newest characters can remain unchanged.

## Baseline and approach
A breadth-first baseline explores strings reachable through individual edits. The optimized DP compares prefix pairs, retaining only the previous and current rows and placing the shorter word across columns.

## Why it works
Before computing a cell, the upper, left, and diagonal entries are optimal costs for their smaller prefix pairs. Each possible final edit reduces to one of those states and adds one. Equal characters extend the diagonal optimum at no cost. The initial row and column represent inserting or deleting an entire prefix.

## Complexity
For lengths m and n, **O(mn + m + n + 1) time and O(min(m, n) + 1) auxiliary space**. The extra terms cover empty words. C++ accepts string references rather than creating input copies; both implementations use rolling rows and leave inputs unchanged.

## Pitfalls
Insertion and deletion correspond to different neighbors. Empty strings are valid. Reusing a row in the wrong order can overwrite diagonal values that are still needed.

## Follow-up
How would differing insertion, deletion, and replacement costs change the recurrence?

## Verification
Named fixtures and independent generated-input references accompany the implementation. Official judge results are tracked separately in metadata.
