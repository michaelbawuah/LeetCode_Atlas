# 80 · Remove Duplicates from Sorted Array II

[Problem](https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/) · Medium

## Idea and approaches

Compact sorted runs while permitting two copies of each value. Counting every value and rebuilding is a baseline with O(n) storage; two write/read positions suffice here.

## Correctness invariant

Before reading a value, the retained prefix is sorted and each processed value appears at most twice. Once two output slots exist, equality with the value two slots back means the new occurrence would be a third copy. Otherwise retaining it maintains the invariant. Writes never reach an unread position.

## Complexity

O(n) time and O(1) auxiliary space. Return k; only the first k mutated entries define the answer.

## Verification and pitfalls

Tests call the actual method and compare both k and its prefix against independently capped occurrence counts. Cases include singleton, two copies, long duplicate runs, and negatives.

The comparison is against nums[write - 2], not nums[read - 2], because removed copies change output positions.

**Follow-up:** How would the same invariant support an arbitrary allowed multiplicity t?
