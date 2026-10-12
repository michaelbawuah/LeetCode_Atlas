# 228 · Summary Ranges

[Problem](https://leetcode.com/problems/summary-ranges/) · Easy

## Idea and approaches

Scan each maximal consecutive run in the sorted distinct input and format its endpoints. A baseline checks every possible pair of endpoints; one forward traversal is enough.

## Correctness invariant

The inner scan extends exactly while the next value is the current value plus one. Stopping therefore identifies a maximal run. Emitting one range covers that run once, and restarting at the next value covers all remaining values in order without overlap.

## Complexity

O(n) time and O(1) auxiliary space excluding O(n) output, using bounded-width input integers and therefore bounded-length endpoint strings. Input is preserved.

## Verification and pitfalls

Structural tests decode every emitted range to exactly the original values and require neighboring ranges to have a gap. Fixtures include empty input, singleton runs, negatives, and signed endpoints.

Use a single number for a one-element run. Avoid subtraction or increment overflow in languages with fixed-width integers.

**Follow-up:** How would run formatting change for unsorted data containing duplicates?
