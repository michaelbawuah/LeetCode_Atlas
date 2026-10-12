# 127 · Word Ladder

[Problem](https://leetcode.com/problems/word-ladder/) · Hard

## Idea

Words sharing a wildcard pattern, such as `h*t`, differ in at most that one position. Bucket words by those patterns and perform BFS from the starting word.

**Baseline:** compare every pair of dictionary words to construct all one-letter edges, costing O(N²L) before traversal. Wildcard buckets avoid the pairwise comparison.

## Why it works

Each one-letter edge appears in a shared bucket. BFS visits words in increasing number of transformations, so the first arrival at the target gives the shortest chain. Once a bucket is scanned, all its words have been reached at the earliest possible next distance; clearing it cannot discard a shorter future path. Distances count words, including both endpoints.

## Complexity

For N dictionary words plus the start and length L, constructing and hashing sliced pattern strings costs O(NL²) expected time. Each bucket is scanned once; traversal key creation has the same bound. Stored pattern strings use O(NL²) space in the worst case, with O(NL) bucket references and O(N) queue/visited entries. Input words are not modified.

## Counterexample and checks

The end word must belong to the dictionary; reaching an absent word through a conceptual edit is invalid. Tests compare wildcard traversal against pairwise Hamming-distance edges and Floyd–Warshall on small dictionaries. The named cases include branches, missing targets, and a start already in the dictionary.

**Follow-up:** keep all shortest predecessor edges to return every shortest transformation chain.

## Python and C++23 comparison

Both implementations create wildcard buckets and scan each bucket once during BFS. Python buckets reference immutable word objects; C++ bucket vectors own copies of their words, and hash keys own pattern strings. Including string creation and hashing, both take expected O(NL²) time and O(NL²) auxiliary storage. The word list remains unchanged. The runner owns decoded strings and containers; the solution owns its local buckets, visited set, and queue through standard containers.
