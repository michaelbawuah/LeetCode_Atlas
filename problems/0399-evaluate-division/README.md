# 399 · Evaluate Division

[Problem](https://leetcode.com/problems/evaluate-division/) · Medium

## Idea and approach

Represent a ratio as a directed weighted edge and its reciprocal edge, then multiply weights along a query path.

**Baseline:** Search every simple path independently; visited traversal avoids cycles and repeated vertices.

## Why it works

Each edge expresses a valid ratio, so multiplying a path telescopes to the ratio of its endpoints. Consistent equations guarantee path-independent results. A known variable divided by itself is one; an unknown variable has no ratio even to itself.

## Complexity

O(E + Q(V + E)) time. O(V + E) auxiliary; O(Q) output space. These bounds describe the submitted implementation, excluding fixture-adapter allocations. Inputs are not modified.

## Counterexample and checks

Returning one for x/x without checking whether x exists violates unknown-variable semantics. Floating results use tolerance comparison. Named fixtures cover different structural boundaries. An independent bounded reference accompanies deterministic generated inputs in `test_properties.py`; `parity.py` supplies varied inputs for the shared language checks.

**Follow-up:** Use weighted union-find to accelerate a large number of queries.

## Python and C++23 comparison

Both sources store forward and reciprocal ratios and traverse iteratively for each query. C++ uses `double`; Python uses floats. Results use the shared `approx_list` checker and the metadata’s relative and absolute tolerance of 1e-5, and each source returns -1 for unknown or disconnected variables. Expected O(E+Q(V+E)) time assumes the official bounded variable-name length and expected hash-table operations. Owned adjacency, visited, and stack containers require O(V+E) auxiliary storage, plus O(Q) output; decoded runner inputs are additional copies. Equation, value, and query inputs are unchanged.
