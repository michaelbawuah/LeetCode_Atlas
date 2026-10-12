# 2050 · Parallel Courses III

[Problem](https://leetcode.com/problems/parallel-courses-iii/) · Hard

## Idea and approach

Topologically propagate earliest completion times, waiting for the maximum completion among prerequisites rather than their sum.

**Baseline:** Enumerate every DAG path and select the largest duration sum.

## Why it works

A course can start only after all its prerequisites finish, so its earliest completion is its own duration plus the maximum predecessor completion. Topological processing finalizes every predecessor first. Unlimited simultaneous courses make that critical-path bound achievable.

## Complexity

O(V + E) time. O(V + E) space. These bounds describe the submitted implementation, excluding fixture-adapter allocations. Inputs are not modified.

## Counterexample and checks

Summing independent prerequisite durations overestimates the elapsed time. The iterative traversal handles large DAG depth. Named fixtures cover different structural boundaries. An independent bounded reference accompanies deterministic generated inputs in `test_properties.py`; `parity.py` supplies varied inputs for the shared language checks.

**Follow-up:** Limit the number of simultaneous courses and explain why critical-path length is then only a lower bound.
