# 1584 · Min Cost to Connect All Points

[Problem](https://leetcode.com/problems/min-cost-to-connect-all-points/) · Medium

## Idea

All point pairs form a complete graph weighted by Manhattan distance. Dense Prim's algorithm grows one connected tree using the cheapest edge crossing from included points to an excluded point.

**Baseline:** materialize and sort all O(n²) edges for Kruskal, using O(n²) space. Dense Prim computes distances as needed instead of storing the complete graph.

## Why it works

closest[v] records the minimum weight of an edge from the current tree to v. Choosing the smallest such value selects a minimum crossing edge. The cut property guarantees that edge can belong to a minimum spanning tree. Updating distances from the newly included point maintains the invariant; after n inclusions, the selected n−1 edges connect all points with minimum cost.

## Complexity

O(n²) time for repeated scans and distance updates, O(n) auxiliary storage for included flags and closest costs, and scalar output. Points are not modified.

## Counterexample and checks

Connecting every point directly to the first point can overpay; a chain through intermediate points may be cheaper. The independent oracle enumerates all n−1-edge subsets on small complete graphs and keeps the least-cost connected one. Unique coordinates, negative coordinates, and wide ranges are covered.

**Follow-up:** compare dense Prim with a heap-based approach when the graph is sparse rather than complete.

## Python and C++23 comparison

Both versions implement dense Prim without storing all pairwise edges: O(n²) time and O(n) auxiliary arrays, with scalar output. C++ promotes coordinates before subtraction, computes absolute Manhattan differences and accumulated costs in `long long`, then returns the platform's integer result. Python arithmetic has no fixed-width overflow. Neither version changes point coordinates.
