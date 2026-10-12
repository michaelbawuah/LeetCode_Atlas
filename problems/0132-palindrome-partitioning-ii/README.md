# 132 · Palindrome Partitioning II

[LeetCode problem](https://leetcode.com/problems/palindrome-partitioning-ii/)

## Intuition
A palindrome ending at a position can finish an optimal partition of the preceding prefix.

## Baseline and approach
Enumerating all cut masks is exponential. Expand around each palindrome center and relax the cut count for its right endpoint.

## Why it works
For an interval [left,right] found by expansion, cuts[left] is already optimal: every palindrome ending before left has an earlier center and has been processed. Adding this palindrome needs cuts[left]+1 cuts. Every palindrome has an enumerated center, so all possible final pieces are considered. cuts[0]=−1 makes a whole-prefix palindrome require zero cuts.

## Complexity
Python: **O(n²) time; O(n) auxiliary space**. n is length. At most O(n²) palindromic expansions are checked and the prefix-cut array uses O(n) space; no quadratic palindrome table is allocated.

## Pitfalls
Count cuts, not pieces. Include even centers. Keep the empty-prefix state at −1 rather than zero.

## Follow-up
How would you reconstruct a minimum-cut partition from these relaxations?

## Verification
Named fixtures and an independent generated-input oracle accompany this implementation. Official judge results are recorded separately in metadata.

## C++23 counterpart

The center-expansion core stores O(n + 1) minimum prefix-cut states, and the by-value string also occupies O(n) bytes. A palindrome ending at right can extend the optimum before left by one part. The initial empty-prefix cut count is -1, which makes a whole-string palindrome require zero cuts. Official nonempty inputs keep the result defined.

C++: **O(n² + n) time; O(n) including string copy and prefix-cut states space**. Named fixtures and 150 reproducible generated inputs compare this implementation with the Python track.
