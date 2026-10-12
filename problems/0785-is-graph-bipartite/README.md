# 785 · Is Graph Bipartite?

[Problem](https://leetcode.com/problems/is-graph-bipartite/) · Medium

## Idea

Assign each newly reached vertex the opposite color from its parent. Every edge must connect opposite colors, and disconnected components need their own starting color.

**Baseline:** enumerate all 2^V two-color assignments and check every edge. BFS propagates required choices instead.

## Why it works

Each component's first color can be chosen freely; every traversed edge then forces its neighbor's opposite color. A same-color edge contradicts this requirement, so no legal coloring exists for that component. If all edges pass, the produced colors partition the vertices into two sets with no internal edge.

## Complexity

O(V + E) time and O(V) auxiliary colors and queue storage, with scalar output. The adjacency list is not modified.

## Counterexample and checks

Checking only the component containing vertex 0 misses an odd cycle elsewhere. The generated oracle enumerates all binary assignments on small undirected graphs, including disconnected components and isolated vertices.

**Follow-up:** return an odd cycle as a witness when a conflict is detected.
