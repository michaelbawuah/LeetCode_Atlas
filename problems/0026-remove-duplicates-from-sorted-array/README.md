# 26 · Remove Duplicates from Sorted Array

[Problem](https://leetcode.com/problems/remove-duplicates-from-sorted-array/) · Easy

## Idea and approaches

Read the sorted values while compacting a prefix containing one copy of each distinct value. A baseline builds a set and a new sorted list, using O(n) extra storage. The chosen two-pointer scan reuses the input array.

## Correctness invariant

Before each read, the written prefix is the sorted unique list of values already processed. A value different from its final element begins a new run and is written once. Equal values add nothing. Writing only at or behind the read position preserves unread input.

## Complexity

O(n) time and O(1) auxiliary space. The method mutates only the meaningful prefix and returns its length k; the remaining tail has no specified contents.

## Verification and pitfalls

Tests invoke the actual method and check both k and nums[:k] against a sorted-set oracle, plus object identity and array length. A correct count alone does not prove correct compaction.

Compare with the last written value rather than an arbitrary modified tail slot. Input is nonempty and sorted under the contract.

**Follow-up:** How would a run-length representation retain the count of every distinct value?
