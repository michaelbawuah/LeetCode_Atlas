# 87 · Scramble String

[LeetCode problem](https://leetcode.com/problems/scramble-string/)

## Intuition
At a split, corresponding halves either remain in order or swap their positions.

## Baseline and approach
Enumerating every recursively scrambled string is the baseline. Memoize whether a pair of equally sized intervals can match, and reject intervals with different character multisets.

## Why it works
Every recursive scramble chooses a nonempty first split. Trying all split lengths in both orientations covers that choice; recursively correct children establish the parent. Equal interval text is immediately feasible, while unequal multisets cannot become equal through reordering.

## Complexity
Python: **O(n⁴) expected time; O(n³) cached states; O(n²) recursive substring storage auxiliary space**. n is the shared length. There are O(n³) interval-pair states and O(n) split work per state. Slice comparisons and Counter construction also cost O(n) per state. Memoization uses O(n³) states; retained slices along recursion can use O(n²) additional characters.

## Pitfalls
An anagram need not be a scramble. Both inputs have equal nonzero length. Cache interval indices and length rather than entire substring pairs.

## Follow-up
How could prefix frequency tables remove repeated multiset construction?

## Verification
Named fixtures and an independent generated-input oracle accompany this implementation. Official judge results are recorded separately in metadata.
