# 622. Design Circular Queue

[Problem on LeetCode](https://leetcode.com/problems/design-circular-queue/) · Medium

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

## C++23 counterpart

[Source](solution.cpp) · [Local adapter](cpp_runner.cpp) · [Parity generator](parity.py)

The C++ design uses standard-container ownership and a fresh local object per fixture. Constructor output is null; these public operations return their integer or Boolean results. Amortized bounds account for container growth/removal; no object persists between fixtures.

Time: constructor O(k); operations O(1). Space: O(k).
