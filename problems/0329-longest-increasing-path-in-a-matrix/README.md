# 329 · Longest Increasing Path in a Matrix

[Problem](https://leetcode.com/problems/longest-increasing-path-in-a-matrix/) · Hard

## Idea and approach

Orient edges toward strictly greater neighboring values. Peel this acyclic graph backward from its local maxima and count layers.

**Baseline:** Enumerate every increasing walk separately, repeating suffixes.

## Why it works

Strict increases rule out cycles. The first reverse layer contains paths of remaining length one; a vertex is released only after all larger successors are removed, making its layer one beyond its longest successor layer. The total number of layers equals the longest path length.

## Complexity

O(rows * cols) time. O(rows * cols) space. These bounds describe the submitted implementation, excluding fixture-adapter allocations. Inputs are not modified.

## Counterexample and checks

Equal values do not form edges. The iterative method also avoids recursion limits on a long increasing matrix path. Named fixtures cover different structural boundaries. An independent bounded reference accompanies deterministic generated inputs in `test_properties.py`; `parity.py` supplies varied inputs for the shared language checks.

**Follow-up:** Recover one longest path by storing a successor that attains each layer.

## Python and C++23 comparison

Both sources peel local maxima from the matrix DAG one BFS layer at a time. The C++ queue and degree matrix own their storage, and the matrix is read without mutation. Explicit layers avoid recursion depth proportional to an increasing path. O(rows × cols) time and auxiliary storage exclude the runner’s decoded input copy. Neighbor values are compared directly rather than subtracted, so values near the maximum signed integer remain safe.
