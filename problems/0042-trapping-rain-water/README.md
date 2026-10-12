# 42 · Trapping Rain Water

[Problem](https://leetcode.com/problems/trapping-rain-water/) · Hard · Two pointers

## Approach

**Baseline:** for each bar, independently scan both sides for their tallest bars:
O(n²) time. Prefix/suffix maxima reduce that to O(n) time with O(n) storage.
**Chosen approach:** process inward from the shorter current endpoint while
maintaining the largest processed height on each side.

## Invariant and correctness

Each processed bar's capacity is finalized, and both peaks summarize their
processed sides. When the left endpoint is shorter, a right boundary at least
that high exists. Any earlier left peak higher than that right boundary could
only have been processed while an equally high right boundary existed, so the
processed left peak safely determines capacity at this position. The symmetric
argument applies on the right. Adding `peak - height` counts each finalized bar's
water once; the final meeting boundary has no uncounted capacity.

## Complexity and languages

Both implementations use O(n) time and O(1) auxiliary space, without changing input.
C++ accepts the vector by reference and accumulates volume in `long long` before
returning the bounded `int` result. Adapter-created JSON/vector copies are outside
the solution's auxiliary-space accounting.

## Verification and pitfalls

Properties use independent per-bar maxima, reversal, and height scaling. Fixtures
include a low outer wall, monotone bars, and multiple basins. Capacity depends on
the shorter bounding wall, not the tallest wall in the entire input.

**Follow-up:** how does a monotonic-stack solution identify and count basins?
