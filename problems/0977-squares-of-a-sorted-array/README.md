# 977 · Squares of a Sorted Array

[Problem](https://leetcode.com/problems/squares-of-a-sorted-array/) · Easy

## Idea and approaches

The largest remaining square comes from an endpoint of the sorted signed array. Squaring and general sorting is an O(n log n) baseline; fill output backward with two pointers.

## Correctness invariant

The unprocessed input interval remains sorted, so its greatest absolute value lies at one of its ends. Choosing that endpoint supplies the largest remaining square. Writing it into the final unfilled output position maintains a sorted completed suffix until all entries have been placed.

## Complexity

O(n) time and O(1) auxiliary space excluding O(n) output. Input is preserved; legal absolute values at most 10^4 yield squares at most 10^8.

## Verification and pitfalls

The oracle squares all values then fully sorts them. Cases cover all-negative, all-positive, repeated magnitudes, and numeric bounds.

Compare absolute values or squares, not the signed endpoints themselves. Fill from right to left so the greatest values are placed first.

**Follow-up:** How could you merge the squared negative and nonnegative halves in forward order?
