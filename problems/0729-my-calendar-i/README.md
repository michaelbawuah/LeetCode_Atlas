# 729. My Calendar I

[Problem on LeetCode](https://leetcode.com/problems/my-calendar-i/) · Medium

## Approach

Testing each existing interval is already a simple O(n) baseline and chosen implementation. A balanced ordered interval tree could improve lookup at added implementation cost.

## Invariant and correctness

Stored intervals are exactly the accepted nonoverlapping half-open bookings. A new interval is accepted only if it intersects none; rejection leaves state unchanged.

## Complexity

Time: O(n) per book. Space: O(n).

## Boundaries and pitfalls

Touching endpoints do not overlap. Use strict comparisons, and never retain a rejected booking.

## Follow-up

Store intervals in an ordered tree and check only immediate neighbors.

## Verification

Named cases and an independent generated-input oracle or operation model accompany the source. Judge results are recorded separately in metadata.
