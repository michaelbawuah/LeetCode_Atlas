# 133 · Clone Graph

[Problem](https://leetcode.com/problems/clone-graph/) · Medium

## Idea

Map each original node to one new node, then copy its neighbor references through that map. A breadth-first queue discovers every reachable original node once.

**Baseline:** copying values without a node map loses sharing, while recursively following edges without visited state fails on cycles.

## Why it works

The map assigns exactly one fresh node to each discovered original. Every processed original edge appends the corresponding mapped neighbor, preserving connections, cycles, and shared neighbors. Because the map is populated before a node is queued, an edge back to an earlier node never creates a second copy or infinite traversal.

## Complexity

O(V + E) expected time for map operations, O(V) auxiliary map and queue space, and O(V + E) cloned output. The original graph and its neighbor lists are unchanged.

## Counterexample and checks

Returning new nodes whose neighbors still reference original nodes is a shallow copy. The property test checks disjoint identities, mapped-edge consistency, distinct neighbor-list objects, and mutation independence. Adjacency fixtures use connected graphs labeled 1 through V, with `[]` representing no node. Neighbor order does not determine graph equality; multiplicity and outer label order still matter.

**Follow-up:** clone only nodes reachable within a fixed distance and define the handling of edges leaving that region.
