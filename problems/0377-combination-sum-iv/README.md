# 377 · Combination Sum IV

[LeetCode problem](https://leetcode.com/problems/combination-sum-iv/)

## Intuition
Each ordered sequence ends with one of the allowed positive values.

## Baseline and approach
Enumerating sequences is exponential. Increasing-total DP counts every possible final value using the previously computed prefix total.

## Why it works
Removing a sequence’s final value leaves exactly one smaller subtotal and an already counted prefix sequence. Summing over final values therefore counts every ordered sequence once. The empty sequence is the single way to total zero.

## Complexity
Python: **O(n T) arithmetic operations time; O(T) integer states auxiliary space**. n is number count and T the target. O(nT) counts arithmetic operations, not bit complexity; intermediate integer widths can grow. Storage is O(T) integer states.

## Pitfalls
Order matters here, unlike Coin Change II. Only the final answer is bounded: the odd-target regression with even values can have huge lower-subtotal counts. Python arbitrary-precision integers preserve them correctly.

## Follow-up
What extra restriction is necessary if zero or negative values are permitted?

## Verification
Named fixtures and an independent generated-input oracle accompany this implementation. Official judge results are recorded separately in metadata.

## C++23 counterpart

Every count update uses only nonnegative addition and copying. Clamping each count to INT_MAX commutes with these operations: min(M, min(M, a) + min(M, b)) = min(M, a + b). Each sum is widened to int64_t before addition and then clamped. The guaranteed final answer fits int, so its clamped value remains exact even when unrelated intermediate counts exceed 64 bits. Positivity ensures every predecessor subtotal is smaller and all transitions remain nonnegative. The odd target with even allowed values is unreachable despite huge counts at even subtotals; it specifically exercises the saturation rule. The core holds T + 1 fixed-width states and reads the input vector by reference.

C++: **O(n T) time; O(T + 1) fixed-width integer states space**. Named fixtures and 150 reproducible generated inputs compare this implementation with the Python track.
