# 122 · Best Time to Buy and Sell Stock II

[Problem](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/) · Medium

## Idea and approaches

Collect each positive day-to-day price increase. A baseline enumerates transaction schedules; the unrestricted repeated-transaction setting lets rises be handled independently.

## Correctness invariant

A transaction from day a to b equals the sum of adjacent differences over that interval. Keeping every positive difference gives an upper bound on the profit of any schedule, since negative differences can only reduce it. Buying and selling along each increasing run attains exactly that bound while holding at most one share.

## Complexity

O(n) time and O(1) auxiliary space. Input prices are preserved; the Python sum consumes a generator rather than a copied difference list.

## Verification and pitfalls

The oracle enumerates legal cash/holding states across short price histories, independently of the greedy rise rule. Named cases include flat, falling, rising, and alternating high/low prices.

This reasoning relies on no transaction fee, cooldown, or transaction-count limit. Same-day trade permission does not add profit beyond the positive rises.

**Follow-up:** Which state variables are needed when each completed trade incurs a fee?

## Python and C++23

C++ scans the referenced price vector without mutation or copying. The official length and price bounds keep the summed profit within int; both versions use constant auxiliary space. The JSON adapter owns decoded inputs; its conversion copies are outside the solution bounds.
