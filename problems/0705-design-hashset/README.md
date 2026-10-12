# 705. Design HashSet

[Problem on LeetCode](https://leetcode.com/problems/design-hashset/) · Easy

## Approach

A compact list of entries requires O(n) lookup. The fixed key range permits direct addressing without a built-in hash table.

## Invariant and correctness

Slot key stores exactly the current membership/value for that key. Adding/writing changes that slot; removing resets it. Other keys are unaffected, so every lookup reads the exact current state.

## Complexity

Time: constructor O(U); each operation O(1). Space: O(U), U = 1000001.

## Boundaries and pitfalls

The official keys are in 0..1000000, trading fixed O(U) initialization/storage for constant-time operations. HashMap values are nonnegative, making -1 an unambiguous missing sentinel.

## Follow-up

Use separate-chaining buckets to save memory when the bounded key range is sparse.

## Verification

Named cases and an independent generated-input oracle or operation model accompany the source. Judge results are recorded separately in metadata.
