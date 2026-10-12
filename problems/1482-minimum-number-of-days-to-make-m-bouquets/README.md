# 1482 · Minimum Number of Days to Make m Bouquets

[Problem](https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/) · Medium

## Idea and approaches

Binary-search the first day on which enough disjoint adjacent flower groups exist. Enumerating bouquet placements at each candidate bloom day is the baseline.

## Correctness invariant

For a fixed day, unavailable flowers divide the garden into separate available runs. A run of length r can form exactly floor(r/k) disjoint bouquets; consuming each earliest group of k achieves that maximum. Availability only increases over time, making feasibility monotone. Search therefore finds its first true day, after rejecting m*k greater than the total flower count.

## Complexity

O(n log(D + 1)) time with D = max(bloomDay) - min(bloomDay), and O(1) auxiliary space. The initial scans and singleton-day case remain linear. Input is preserved.

## Verification and pitfalls

The independent oracle enumerates disjoint valid bouquet starting positions at each distinct bloom day. Cases distinguish sufficient flower count from sufficient adjacency.

Reset a run at every unbloomed flower and after consuming k flowers. A count of available flowers alone ignores adjacency.

**Follow-up:** What changes when bouquet sizes vary instead of sharing one fixed k?
