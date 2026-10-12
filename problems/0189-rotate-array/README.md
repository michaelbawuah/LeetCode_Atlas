# 189 · Rotate Array

[Problem](https://leetcode.com/problems/rotate-array/) · Medium · In-place reversal

## Approach

**Baseline:** construct `last k values + first n - k values`, requiring O(n)
temporary space.
**Chosen approach:** reduce k modulo n, reverse the entire array, then reverse
the first k and remaining n - k values independently.

## Invariant and correctness

Write the original array as `A B`, with B containing its last k values. Whole-array
reversal produces `reverse(B) reverse(A)`. Reversing the two pieces restores each
piece's internal order, producing `B A`, exactly a right rotation by k.
Reducing k modulo n removes complete revolutions without changing the result.

## Complexity

O(n) time and O(1) auxiliary space. The reversal helper uses index swaps rather
than copied slices. The method mutates the original list and returns `None`;
fixture evaluation serializes mutated argument zero.

## Verification and pitfalls

Properties compare with modular coordinate mapping and composition of rotations.
Cases include k = 0, k = n, k > n, a singleton, and signed integer limits.
Normalize k before defining reversal ranges. Rebinding the parameter to a new
list would fail to update the caller's list.

**Follow-up:** how do greatest-common-divisor cycles implement the same mapping?
