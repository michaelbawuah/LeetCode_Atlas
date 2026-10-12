# 134 · Gas Station

[Problem](https://leetcode.com/problems/gas-station/) · Medium

## Idea

Accumulate net fuel. If a candidate start reaches a negative balance at station i, discard every possible start in that failing segment and continue from i+1.

**Baseline:** simulate a full circuit from every station, taking O(n²) time. Greedy candidate resets eliminate whole failing segments together.

## Why it works

Before the failure, every earlier prefix of the current segment had nonnegative balance. Starting later inside that segment removes a nonnegative prefix and cannot rescue its negative total at i, so none of those starts can work. The final candidate works exactly when the overall net fuel is nonnegative: the discarded prefixes have negative totals, which the surviving segment can cover on the wraparound.

## Complexity

O(n) time and O(1) auxiliary state, with scalar output. Gas and cost arrays are not modified.

## Counterexample and checks

Choosing the station with the largest individual surplus ignores the order of deficits. Fixed fixtures follow the unique-answer contract. Generated circuits also include multiple valid starts; their oracle simulates every station and accepts any feasible witness rather than an arbitrary preferred index. The semantic fixture checker validates the returned circular route.

**Follow-up:** list every valid starting station efficiently using doubled prefix sums and a sliding-window minimum.

## Python and C++23 comparison

Both versions discard a failing candidate segment and test total net fuel. C++ widens before subtracting cost from gas and keeps running totals in `long long`; Python uses unbounded integers. Both run in O(n) time with O(1) auxiliary state and preserve both input arrays. The shared checker simulates the returned circular witness, allowing broader generated cases with more than one feasible start.
