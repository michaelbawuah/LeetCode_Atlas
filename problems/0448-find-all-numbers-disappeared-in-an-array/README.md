# 448 · Find All Numbers Disappeared in an Array

[Problem](https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/) · Easy · Index marking

## Approach

**Baseline:** put values into a set and subtract from the range 1 through n,
requiring O(n) extra storage.
**Chosen approach:** use the sign of slot `value - 1` as a presence marker.
After marking, positive slots identify missing values.

## Invariant and correctness

Every input value lies in 1 through n, so its marker slot is valid. Negating a
positive marker records presence, while leaving an already-negative marker
unchanged preserves earlier evidence. Absolute values recover original values
even when a slot was marked before being read. At the end, slot i is negative
exactly when i + 1 occurred; positive slots are therefore exactly the missing numbers.

## Complexity

O(n) time and O(1) auxiliary space excluding up to O(n) output. This implementation
intentionally changes signs in the caller's input; it does not restore the array.
The fixture adapter copies input before evaluation.

## Verification and pitfalls

The oracle uses set difference and checks that absolute values at every position
remain unchanged. Cover repeated marks, complete ranges, and a singleton.
Negating a marker unconditionally would toggle repeated values back to positive.

**Follow-up:** how would you restore input signs before returning while keeping constant space?
