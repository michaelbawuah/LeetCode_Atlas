# 1631 · Path With Minimum Effort

[Problem](https://leetcode.com/problems/path-with-minimum-effort/) · Medium

## Idea and approach

Use Dijkstra with path cost equal to its largest edge difference, replacing additive relaxation with a maximum.

**Baseline:** Try each distinct edge threshold and check whether its permitted subgraph connects the endpoints.

## Why it works

Extending a path cannot decrease its maximum edge. Therefore the smallest tentative effort is final when popped, just as with nonnegative additive distances. A relaxation considers every candidate last edge and minimizes the resulting maximum. R and C are grid dimensions.

## Complexity

O(R C log(R C + 1)) time. O(R C) space. These bounds describe the submitted implementation, excluding fixture-adapter allocations. Inputs are not modified.

## Counterexample and checks

Minimizing total height change solves a different objective than minimizing the largest individual jump. Named fixtures cover different structural boundaries. An independent bounded reference accompanies deterministic generated inputs in `test_properties.py`; `parity.py` supplies varied inputs for the shared language checks.

**Follow-up:** Recover one optimal path or answer many endpoint queries with a spanning tree.

## Python and C++23 comparison

C++ stores minimax efforts in integer tables and a min-priority queue. Official heights are at most one million, so signed height differences and their absolute values fit int. Each cost is a maximum edge difference, not an accumulated sum; inputs stay unchanged.
