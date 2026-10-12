# 542 · 01 Matrix

[Problem](https://leetcode.com/problems/01-matrix/) · Medium

## Idea and approach

Start BFS from every zero simultaneously and fill one distance matrix.

**Baseline:** For each cell, scan all zero coordinates and minimize Manhattan distance.

## Why it works

A cell first reached at layer d has a path of length d to a zero. All shorter layers were exhausted, so no shorter path exists. With no walls, every cell is eventually reached because the contract guarantees at least one zero.

## Complexity

O(rows * cols) time. O(rows * cols) auxiliary and output space. These bounds describe the submitted implementation, excluding fixture-adapter allocations. Inputs are not modified.

## Counterexample and checks

Starting a new traversal at every one repeats work; simultaneous sources handle competing nearest zeros correctly. Named fixtures cover different structural boundaries. An independent bounded reference accompanies deterministic generated inputs in `test_properties.py`; `parity.py` supplies varied inputs for the shared language checks.

**Follow-up:** Adapt the traversal when some cells are walls and may be unreachable.

## Python and C++23 comparison

The C++ result matrix doubles as its visited/distance table. Both sources need O(R C) output and up to O(R C) queue space, process each cell once, and preserve the input matrix.
