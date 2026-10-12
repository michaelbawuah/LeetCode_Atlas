# 1462 · Course Schedule IV

[Problem](https://leetcode.com/problems/course-schedule-iv/) · Medium

## Idea and approach

Build directed transitive reachability before answering repeated prerequisite queries.

**Baseline:** Search outward separately for each query, repeating the same graph traversals.

## Why it works

After processing intermediate vertex v, reach[a][b] covers paths whose internal vertices come from processed IDs. A path using v splits into a path to v and one from v, so the update adds exactly the newly allowed paths.

## Complexity

O(n^3 + Q) time. O(n^2) auxiliary; O(Q) output space. These bounds describe the submitted implementation, excluding fixture-adapter allocations. Inputs are not modified.

## Counterexample and checks

The prerequisite pair here means before→after; reversing it changes every directional query. Named fixtures cover different structural boundaries. An independent bounded reference accompanies deterministic generated inputs in `test_properties.py`; `parity.py` supplies varied inputs for the shared language checks.

**Follow-up:** Use topological bitsets to reduce preprocessing on larger DAGs.
