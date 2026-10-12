# 641. Design Circular Deque

[Problem on LeetCode](https://leetcode.com/problems/design-circular-deque/) · Medium

## Approach

A list that shifts entries after front removal costs O(k). A fixed circular array changes only head and size.

## Invariant and correctness

The logical ith value is stored at (head+i) modulo capacity for 0<=i<size. Insertion writes the next logical slot; removal adjusts the boundary without shifting stored values. Size distinguishes full and empty states.

## Complexity

Time: constructor O(k); operations O(1). Space: O(k).

## Boundaries and pitfalls

Capacity is positive. Failed full insertions and empty deletions leave state unchanged. Empty endpoint queries return -1. Test wraparound and capacity one.

## Follow-up

Resize the buffer while preserving logical order.

## Verification

Named cases and an independent generated-input oracle or operation model accompany the source. Judge results are recorded separately in metadata.
