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

## C++23 counterpart

Python scans an unsorted list in O(n) per booking; C++ stores accepted half-open intervals in std::map. lower_bound finds the successor, and only it and its predecessor can overlap because accepted intervals are disjoint. Check both before insertion so rejection preserves state. Strict comparisons allow touching endpoints. n counts accepted bookings.

Time: book O(log(n + 1)). Space: O(n) stored; O(1) auxiliary per book.

The JSON adapter creates fresh state per case. Named fixtures and 150 deterministic generated inputs compare the two language implementations; existing independent Python oracles supply a separate behavioral reference.
