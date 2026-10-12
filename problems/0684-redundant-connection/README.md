# 684 · Redundant Connection

[Problem](https://leetcode.com/problems/redundant-connection/) · Medium

## Idea

Add edges one at a time while tracking connected components. If an edge joins two vertices already connected, it closes the unique cycle. Union-find provides fast component tests and merges.

**Baseline:** try removals from the end and check connectivity with a graph traversal, costing O(n²). The optimized version uses union by size and path compression.

## Why it works

After each accepted edge, union-find represents connectivity of the edges seen so far. Two endpoints already in one component have an existing path, so adding their edge creates a cycle. The contract supplies a connected tree plus one extra edge, hence exactly one cycle. Its last edge in input order is precisely the first edge whose endpoints are already connected, satisfying the required latest-removal rule. Later bridge edges cannot replace that answer.

## Complexity

For n vertices and n edges, O(n α(n)) amortized time and O(n) auxiliary space. α is the inverse Ackermann function. The edge list is not changed.

## Counterexample and checks

Returning the final input edge is wrong when a bridge appears after the cycle closes. The generated oracle examines removals from latest to earliest and independently traverses the remaining graph; with n−1 edges, connectivity proves it is a tree. Generated inputs preserve the tree-plus-extra-edge contract and labels 1 through n.

**Follow-up:** support online edge deletion; explain why ordinary union-find cannot undo arbitrary merges directly.

## Python and C++23 comparison

Both sources use union by size and path compression, giving O(n α(n)) amortized time and O(n) auxiliary space under the tree-plus-one-edge contract. Python sizes its arrays from the edge count, using the guaranteed labels 1 through n. C++ first scans for the largest label and sizes its vectors from that bound; under the same contract this is still O(n). Each returns the original closing edge's two endpoints in a constant-size result, preserving the input edge order and orientation. Neither input is modified.
