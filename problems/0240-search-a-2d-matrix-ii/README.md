# 240 · Search a 2D Matrix II

[Problem](https://leetcode.com/problems/search-a-2d-matrix-ii/) · Medium

## Idea and approaches

Start at the top-right corner, where moving left lowers values and moving down raises them. A full membership scan is O(mn); staircase elimination discards one row or column per step.

## Correctness invariant

All possible matches remain in the rectangle below the current row and left of the current column. If its corner value exceeds target, every remaining value in that column is at least as large, so discard the column. If it is below target, every remaining value in that row is at most as small, so discard the row. Equality proves a match; exhaustion proves absence.

## Complexity

O(m + n) time and O(1) auxiliary space. Both languages preserve the matrix and rely on rows and columns each being sorted, without requiring flattened global order.

## Verification and pitfalls

Generated matrices are made independently monotone, and a full cell scan supplies the oracle. Cases include duplicates, negatives, single rows/columns, and absent interior targets.

The binary-search flattening method for problem 74 requires a stronger ordering guarantee and cannot be substituted here.

**Follow-up:** How would divide-and-conquer search compare on a very wide matrix?

## Python and C++23

C++ receives the matrix by reference and moves a scalar row/column boundary; it performs no matrix copy and no mutation. Its method has the same staircase bounds as Python. The JSON adapter owns decoded inputs; its conversion copies are outside the solution bounds.
