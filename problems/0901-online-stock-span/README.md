# 901. Online Stock Span

[Problem on LeetCode](https://leetcode.com/problems/online-stock-span/) · Medium

## Approach

Scanning backward after every price can take O(n²) total time. Compress each resolved run into a price/span stack entry.

## Invariant and correctness

Stack prices strictly decrease, and each entry span summarizes its consecutive absorbed days. A new price absorbs every trailing run whose maximum is no greater, then stops at the nearest strictly larger price.

## Complexity

Time: next O(1) amortized; O(n) worst case. Space: O(n).

## Boundaries and pitfalls

Equality belongs in the span. Every entry is pushed once and popped at most once, proving amortized constant time; one call can still pop n entries.

## Follow-up

Maintain the same statistic over a fixed recent-day window.

## Verification

Named cases and an independent generated-input oracle or operation model accompany the source. Judge results are recorded separately in metadata.

## C++23 counterpart

[Source](solution.cpp) · [Local adapter](cpp_runner.cpp) · [Parity generator](parity.py)

The C++ design uses standard-container ownership and a fresh local object per fixture. Constructor output is null; these public operations return their integer or Boolean results. Amortized bounds account for container growth/removal; no object persists between fixtures.

Time: next O(1) amortized; O(n) worst case. Space: O(n).
