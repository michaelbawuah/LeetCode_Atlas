# 2127 · Maximum Employees to Be Invited to a Meeting

[Problem](https://leetcode.com/problems/maximum-employees-to-be-invited-to-a-meeting/) · Hard

## Idea and approach

Peel indegree-zero chains while storing the longest chain ending at each vertex, then compare long cycles with the sum of expanded mutual pairs.

**Baseline:** Enumerate employee subsets and circular seat permutations, checking every favorite neighbor.

## Why it works

Every functional component has one cycle. A cycle of length at least three occupies both adjacent seats at each cycle vertex, so extra incoming chains cannot attach. A mutual pair uses only one required neighbor slot per endpoint, allowing one longest incoming chain on each side. Expanded pair segments can be concatenated around one table, so their contributions add; longer cycles compete as separate alternatives.

## Complexity

O(n) time. O(n) space. These bounds describe the submitted implementation, excluding fixture-adapter allocations. Inputs are not modified.

## Counterexample and checks

Summing all cycles is invalid: cycles of length three or more cannot share one circular seating while preserving every required adjacency. Named fixtures cover different structural boundaries. An independent bounded reference accompanies deterministic generated inputs in `test_properties.py`; `parity.py` supplies varied inputs for the shared language checks.

**Follow-up:** Return an actual seating arrangement realizing the optimum.
