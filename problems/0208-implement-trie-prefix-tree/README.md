# 208. Implement Trie (Prefix Tree)

[Problem on LeetCode](https://leetcode.com/problems/implement-trie-prefix-tree/) · Medium

## Intuition
Words with the same beginning can share a path. Mark complete words separately from nodes that merely represent prefixes.

## Approaches
- **Baseline:** retain a set of words; exact search is expected O(L), while a prefix query may scan all stored words: O(WL) time for W words and query length L.
- **Optimized:** store one edge per next letter. Insert, exact search, and prefix search all follow the query's path.

## Correctness invariant
Each node represents exactly the letters on the path from the root to that node. Its terminal flag is true precisely when that whole path has been inserted as a word. Insertion creates missing edges and marks the final node. Traversing a present path proves prefix membership, while exact membership additionally requires the terminal flag.

## Complexity
O(L) expected time per operation for a length-L word or prefix with dictionary edge lookups. The fixed lowercase alphabet also bounds the number of children per node. Stored space is O(T), where T is the sum of inserted word lengths; shared prefixes and duplicate insertions may use less. Traversal uses O(1) auxiliary space. Insertion may allocate O(L) new stored nodes.

## Edge cases and pitfalls
A prefix need not be a complete word. Duplicate insertion is idempotent. Queries against an empty trie fail for nonempty strings. Fixtures and generated tests use the nonempty lowercase word/prefix domain.

## Follow-up
Add deletion without removing a prefix used by another word, or maintain the count of stored words beneath each node.

## Verification
Named fixtures and an independent generated-input reference accompany this implementation. Official judge results are tracked separately in metadata.

## C++23 counterpart

[Source](solution.cpp) · [Local adapter](cpp_runner.cpp)

C++ stores nodes in a vector with fixed 26-child index arrays. Node indexes survive vector reallocation; no pointer or reference is held across an insertion. Nodes are owned by the vector; inserted words are represented by node paths rather than retained strings. By-value word and prefix parameters copy O(L) characters.

Time: O(L) amortized per insert; O(L) search/prefix. Space: O(T) stored, plus O(L) by-value parameter copying. The local adapter constructs a fresh object for each fixture and owns any converted inputs.
