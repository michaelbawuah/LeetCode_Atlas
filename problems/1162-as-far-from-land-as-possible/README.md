# 1162 · As Far from Land as Possible

[Problem](https://leetcode.com/problems/as-far-from-land-as-possible/) · Medium

## Idea and approach

Launch BFS from every land cell and retain the largest distance assigned to water.

**Baseline:** For each water cell, scan every land coordinate for the nearest Manhattan distance.

## Why it works

Every water cell receives its shortest distance to any source in the first BFS layer reaching it. Taking the maximum of those nearest-source distances gives the requested farthest water cell. If either class is missing, the requested comparison is undefined and returns -1.

## Complexity

O(n^2) time. O(n^2) space. These bounds describe the submitted implementation, excluding fixture-adapter allocations. Inputs are not modified.

## Counterexample and checks

Distance to the farthest individual land cell is not the nearest-land distance. Named fixtures cover different structural boundaries. An independent bounded reference accompanies deterministic generated inputs in `test_properties.py`; `parity.py` supplies varied inputs for the shared language checks.

**Follow-up:** Return all farthest water coordinates as well as the distance.

## Python and C++23 comparison

Both sources seed BFS from every land cell and assign nearest-land distances to water. C++ owns a distance matrix and queue and does not change the grid. O(n²) time and auxiliary storage exclude the runner’s decoded O(n²) matrix copy. Empty source sets and all-land grids return -1, and no recursive traversal is used.
