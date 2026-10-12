# 547 · Number of Provinces

[Problem](https://leetcode.com/problems/number-of-provinces/) · Medium

## Idea

A province is a connected component, including indirect city connections. Start a traversal at each unseen city and count how many starts are necessary.

**Baseline:** repeatedly compute reachability from every city. One component traversal marks all members together; the adjacency matrix is read row by row.

## Why it works

A traversal follows every connection from its discovered cities, reaching precisely their connected component. Marking cities on insertion avoids duplicate work. Each later scan position either belongs to a previously counted component or starts one new component, so the count equals the number of provinces.

## Complexity

For n cities, O(n²) time to inspect every relevant matrix row and O(n) auxiliary visited and stack space. Output is scalar and the matrix is unchanged.

## Counterexample and checks

Counting only directly connected groups misses a chain joining distant city labels. Generated tests preserve symmetry and diagonal ones, then compare with an independent union-find partition.

**Follow-up:** replace the dense matrix with adjacency lists and update the time bound for sparse connections.

## Python and C++23 comparison

Both versions traverse one connected component at a time and inspect its adjacency-matrix rows. C++ uses visited flags and a vector of pending city indices, while Python uses a list stack. Each city is marked before insertion. Time is O(n²), auxiliary storage O(n), and output one integer. The matrix is read without mutation.
