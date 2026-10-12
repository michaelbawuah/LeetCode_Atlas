# 1192 · Critical Connections in a Network

[Problem](https://leetcode.com/problems/critical-connections-in-a-network/) · Hard

## Idea and approach

Use iterative DFS frames to compute discovery times and each subtree’s lowest reachable ancestor time.

**Baseline:** Remove each edge in turn and test whether the graph remains connected, costing O(E(V+E)).

## Why it works

After a child finishes, low[child] summarizes back edges from its subtree. The tree edge to its parent is a bridge exactly when low[child] exceeds the parent discovery time; otherwise an alternate route reaches the parent or an ancestor. Propagating low values on frame completion is the iterative counterpart of DFS postorder.

## Complexity

O(V + E) time. O(V + E) auxiliary; O(E) output space. These bounds describe the submitted implementation, excluding fixture-adapter allocations. Inputs are not modified.

## Counterexample and checks

Propagate a child’s low-link value after all its neighbors finish; doing it at first discovery can miss a later return route. Official inputs have no repeated connections. If extending the problem to parallel edges, skip only the specific parent edge so another edge to that parent can supply a return route. Explicit frames avoid recursion failure at 100,000 vertices. Named fixtures cover different structural boundaries. An independent bounded reference accompanies deterministic generated inputs in `test_properties.py`; `parity.py` supplies varied inputs for the shared language checks.

**Follow-up:** Group vertices into components after deleting all bridges.
