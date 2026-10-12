# 1971 · Find if Path Exists in Graph

[Problem](https://leetcode.com/problems/find-if-path-exists-in-graph/) · Easy

## Idea and approach

Union the endpoints of every undirected edge and compare the final component representatives.

**Baseline:** Search the adjacency graph directly from the source for each query.

## Why it works

Each union combines exactly two components connected by an input edge. Inductively the resulting partition matches connectivity of all processed edges. Equal representatives after all unions are therefore equivalent to an existing path; a vertex always reaches itself.

## Complexity

O((V + E) alpha(V)) amortized time. O(V) space. These bounds describe the submitted implementation, excluding fixture-adapter allocations. Inputs are not modified.

## Counterexample and checks

An empty edge list can still yield true when source equals destination. Named fixtures cover different structural boundaries. An independent bounded reference accompanies deterministic generated inputs in `test_properties.py`; `parity.py` supplies varied inputs for the shared language checks.

**Follow-up:** Maintain connectivity online while edges are added.

## Python and C++23 comparison

C++ parent and size vectors support path compression and union by size just as the Python lists do. Time is O((V+E) α(V)) amortized and auxiliary storage O(V), with boolean output. IDs stay in the official int domain.
