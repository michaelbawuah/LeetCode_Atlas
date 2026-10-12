# 2192 · All Ancestors of a Node in a Directed Acyclic Graph

[Problem](https://leetcode.com/problems/all-ancestors-of-a-node-in-a-directed-acyclic-graph/) · Medium

## Idea and approach

Process vertices topologically and union each parent’s finalized ancestor set into every child before adding the parent itself.

**Baseline:** Compute full transitive reachability and read each destination column.

## Why it works

Every ancestor of a child is either an immediate parent or an ancestor of an immediate parent. Topological order guarantees each parent set is complete before propagation, and sets remove duplicates from multiple routes. Sorting each final set supplies the required ordered ancestor lists.

## Complexity

O(E V + V^2 log(V + 1)) expected time. O(V^2 + E) including output space. These bounds describe the submitted implementation, excluding fixture-adapter allocations. Inputs are not modified.

## Counterexample and checks

Multiple routes to the same ancestor must not create duplicate IDs. Both outer node order and inner ascending order are required. Named fixtures cover different structural boundaries. An independent bounded reference accompanies deterministic generated inputs in `test_properties.py`; `parity.py` supplies varied inputs for the shared language checks.

**Follow-up:** Replace sets with bitsets and compare merging costs on dense DAGs.
