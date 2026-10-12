# 797 · All Paths From Source to Target

[Problem](https://leetcode.com/problems/all-paths-from-source-to-target/) · Medium

## Idea and approach

Backtrack over outgoing DAG edges while maintaining one source-to-current path.

**Baseline:** Enumerate permutations of intermediate vertices and retain paths whose edges exist.

## Why it works

Acyclicity makes every directed walk simple and finite. Every emitted path ends at the designated target, and each distinct edge-choice sequence identifies one source-to-target path. Restoring the path after each call preserves sibling state. P is output path count; recursion depth is at most V, bounded by fifteen under the contract.

## Complexity

O(V 2^V) conservative bound time. O(V) auxiliary; O(P V) output space. These bounds describe the submitted implementation, excluding fixture-adapter allocations. Inputs are not modified.

## Counterexample and checks

Inner vertex order matters even when outer path order is arbitrary. Named fixtures cover different structural boundaries. An independent bounded reference accompanies deterministic generated inputs in `test_properties.py`; `parity.py` supplies varied inputs for the shared language checks.

**Follow-up:** Count paths with dynamic programming when enumerating them would be too large.

## Python and C++23 comparison

C++ passes the path by reference through helper calls and copies it at complete paths. Auxiliary recursion/path storage is O(V), with O(P V) output; the DAG contract bounds recursion depth by fifteen.
