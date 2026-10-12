# 47 · Permutations II

[LeetCode problem](https://leetcode.com/problems/permutations-ii/)

## Intuition
Track remaining multiplicities rather than assigning labels to equal positions. Every distinct next value creates one branch.

## Baseline and approach
The baseline generates all position permutations and deduplicates them. Frequency-based backtracking directly produces distinct value arrangements.

## Why it works
At each call, path plus the remaining counts contains exactly the original multiset. Choosing a positive-count value decrements one occurrence; restoring it after recursion preserves the sibling state. A completed path is a permutation, and its next-value sequence uniquely identifies its branch, so duplicate permutations cannot be emitted.

## Complexity
For n values, U distinct values, and P output permutations, **O(n+U log U+nUP)** is a conservative time bound: there are at most nP prefix nodes and each scans U values. Auxiliary space is **O(n+U)**; output uses **O(nP)**. Inputs are unchanged.

## Pitfalls
Do not recurse on exhausted counts. Restore the count and path after every branch. The checker permits outer row reordering while keeping each permutation’s element order.

## Follow-up
How would lexicographic ranking let you retrieve one unique permutation without enumerating all of them?

## Verification
Named fixtures and independent generated-input references accompany the implementation. Official judge results are tracked separately in metadata.

## C++23 counterpart

C++ uses std::map to keep U distinct values ordered, so frequency construction costs O(n log(U+1)); Python uses a Counter and then sorts its distinct keys. Both scan U choices per prefix and copy each length-n output. Counts are decremented and restored without inserting or erasing map entries during recursion.

Time: O(n log(U + 1) + n U P) conservative bound. Space: O(n + U) auxiliary; O(n P) output.

The JSON adapter creates fresh state per case. Named fixtures and 150 deterministic generated inputs compare the two language implementations; existing independent Python oracles supply a separate behavioral reference.
