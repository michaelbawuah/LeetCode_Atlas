# 703. Kth Largest Element in a Stream

[Problem on LeetCode](https://leetcode.com/problems/kth-largest-element-in-a-stream/) · Easy

## Intuition
Values below the largest k can never improve the kth-largest rank. Keep only those k values in a min-heap.

## Approaches
- **Baseline:** append each value and sort the entire stream for every query: O(s log s) time per addition for current stream size s, O(s) space.
- **Optimized:** retain at most k values. Add while under capacity; afterward replace the smallest retained value only when the new value is larger.

## Correctness invariant
The heap stores the largest min(k, s) values seen so far, with duplicates counted as separate elements. A value no larger than the heap minimum cannot enter the largest k after capacity is reached. Otherwise replacing that minimum preserves the largest-k set. Once at least k values exist, the heap minimum is exactly the requested rank.

## Complexity
For n initial values, construction takes O(n log(k + 1)) time. Each `add` takes O(log(k + 1)) worst-case heap work and O(1) when it discards a value after capacity is reached. Stored space is O(k).

## Edge cases and pitfalls
An empty initial stream is valid with k = 1. The input contract ensures that an externally queried addition has at least k values available. Duplicates affect rank; do not deduplicate. The constructor does not mutate its input list.

## Follow-up
Support changing k after construction. Which discarded values would have to be retained to answer arbitrary future ranks?

## Verification
Named fixtures and an independent generated-input reference accompany this implementation. Official judge results are tracked separately in metadata.
