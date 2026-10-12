# 802 · Find Eventual Safe States

[Problem](https://leetcode.com/problems/find-eventual-safe-states/) · Medium

## Idea and approach

Reverse edges and release a node only after every outgoing neighbor has been certified safe.

**Baseline:** Compute transitive reachability and identify every node reaching a cycle.

## Why it works

Terminals are safe initially. Removing a safe node subtracts one unfinished outgoing neighbor from each parent; a parent with no unfinished neighbor has only safe continuations. Nodes left behind have a continuation into a remaining cycle, so precisely safe nodes are released. Scanning IDs in order supplies the required sorted output.

## Complexity

O(V + E) time. O(V + E) auxiliary; O(V) output space. These bounds describe the submitted implementation, excluding fixture-adapter allocations. Inputs are not modified.

## Counterexample and checks

One safe successor does not make a node safe if another successor reaches a cycle. Named fixtures cover different structural boundaries. An independent bounded reference accompanies deterministic generated inputs in `test_properties.py`; `parity.py` supplies varied inputs for the shared language checks.

**Follow-up:** Return a cycle reachable from each unsafe component.

## Python and C++23 comparison

Both versions release nodes whose remaining outgoing degree becomes zero and scan vertex IDs in increasing order afterward, so output sorting needs no extra O(V log V) step. Reverse adjacency is O(V+E) storage.
