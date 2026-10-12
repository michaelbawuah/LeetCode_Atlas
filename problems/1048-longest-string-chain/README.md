# 1048 · Longest String Chain

[LeetCode problem](https://leetcode.com/problems/longest-string-chain/)

## Intuition
A predecessor is produced by deleting one character from a word.

## Baseline and approach
Exhaustively traversing the predecessor graph is the baseline. Sort words by length and cache the best chain ending at each word.

## Why it works
When processing a word, every possible predecessor is shorter and has already been processed. Deleting each position enumerates all legal predecessors, and extending their best chain by one therefore finds the current optimum. Sorting equal-length words arbitrarily is harmless because they cannot precede one another.

## Complexity
Python: **O(W log W + W L²) expected time; O(W + L) auxiliary space**. W is word count and L the maximum length. Sorting costs O(W log W); each of W×L predecessor strings costs O(L) to copy/hash, giving expected O(WL²) additional work. Sorted references and cached original-word keys use O(W+L) auxiliary space.

## Pitfalls
Insertion may occur anywhere, not only at an endpoint. A substring test is insufficient. Duplicate input words do not lengthen a chain.

## Follow-up
How would you reconstruct a longest chain or count how many there are?

## Verification
Named fixtures and an independent generated-input oracle accompany this implementation. Official judge results are recorded separately in metadata.
