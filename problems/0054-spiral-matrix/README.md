# 54 · Spiral Matrix

[Problem](https://leetcode.com/problems/spiral-matrix/) · Medium · Boundary simulation

## Approach

**Baseline:** simulate movement with a visited-cell set, using O(mn) extra storage.
**Chosen approach:** keep top, bottom, left, and right boundaries of the unvisited
rectangle. Visit its four edges clockwise and shrink each boundary afterward.

## Invariant and correctness

At each outer iteration, the current rectangle contains precisely the unvisited
cells. Reading its top edge, right edge, bottom edge, and left edge visits its
perimeter in spiral order, without repeating corners. Shrinking removes exactly
those cells. Guarding the last two edges prevents revisiting a collapsed row or
column. Induction over shrinking rectangles visits every cell once.

## Complexity

O(mn) time and O(1) auxiliary space excluding the O(mn) returned sequence.
The input matrix is read without mutation.

## Verification and pitfalls

An independent oracle walks one cell at a time, turning when the next cell is
blocked or already visited. Fixtures cover tall/wide rectangles, one row, one
column, and a singleton. Recheck whether boundaries have crossed before reading
the bottom or left edge of the final layer.

**Follow-up:** how would you fill an empty matrix in spiral order instead?

## C++23 counterpart

C++ uses signed boundary indexes so decrementing a collapsed edge cannot wrap an unsigned value. It reserves the returned O(mn) sequence once, while boundary state uses O(1) auxiliary space. The nonempty rectangular matrix is preserved. Single-row and single-column fixtures exercise the final-layer guards.
