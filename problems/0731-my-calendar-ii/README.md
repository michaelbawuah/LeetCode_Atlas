# 731. My Calendar II

[Problem on LeetCode](https://leetcode.com/problems/my-calendar-ii/) · Medium

## Approach

A fresh endpoint sweep for every proposal costs O(n log n). Retain existing bookings and their double-covered intersections to detect triple coverage directly.

## Invariant and correctness

The doubles list contains every pairwise accepted-booking intersection. Intersecting any such region creates forbidden triple coverage. Otherwise the intersections of the new booking with existing bookings are exactly its new double-covered regions.

## Complexity

Time: O(n + d) per book. Space: O(n + d).

## Boundaries and pitfalls

n is accepted bookings and d retained double intervals; both lists are explicitly counted. Existing double regions have disjoint interiors because triple overlap is forbidden, bounding d linearly. Reject before adding intersections. Endpoints are half-open.

## Follow-up

Maintain an ordered endpoint-delta map and roll back a proposed change when the sweep exceeds two.

## Verification

Named cases and an independent generated-input oracle or operation model accompany the source. Judge results are recorded separately in metadata.
