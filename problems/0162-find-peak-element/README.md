# 162 · Find Peak Element

[Problem](https://leetcode.com/problems/find-peak-element/) · Medium

## Idea and approaches

Use the slope between neighboring midpoint values to choose a half containing a peak. A full scan is the O(n) baseline; slope search halves the range.

## Correctness invariant

The current interval contains a peak under the virtual negative-infinity endpoint convention. On an upward slope, moving right eventually finds a descent or the right endpoint, both giving a peak; on a downward slope, the analogous peak lies on the left. Retaining the appropriate half preserves that existence guarantee until one index remains.

## Complexity

O(log n) time and O(1) auxiliary space. Any strict peak is valid, and the input is preserved.

## Verification and pitfalls

The peak_index fixture checker validates the returned index against the original array rather than insisting on one index. The generated oracle enumerates all valid peaks. Endpoint and multiple-peak cases are included.

Adjacent values must differ under the contract. Compare middle with middle + 1 only while left < right, which keeps that neighbor in bounds.

**Follow-up:** Why can equal adjacent values invalidate the strict-peak slope argument?
