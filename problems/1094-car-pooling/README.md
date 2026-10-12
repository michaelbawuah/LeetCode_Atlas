# 1094 · Car Pooling

[Problem](https://leetcode.com/problems/car-pooling/) · Medium

## Idea and approaches

Aggregate pickup and drop-off changes at each location, then sweep east. Testing occupancy independently on every road segment is the baseline.

## Correctness invariant

After applying the net change at a location, load equals the passengers whose trip intervals cover the following segment. Combining same-location changes models drop-offs before pickups, avoiding a false temporary overload. Every possible load change occurs at an event coordinate, so checking all swept loads proves capacity compliance.

## Complexity

Python takes O(t log t) expected time and O(t) auxiliary space for t trips, including sorting distinct event keys. The input trips are preserved.

## Verification and pitfalls

The independent oracle directly totals all intervals covering each small integer road segment. Fixtures include nested trips, exact capacity, and drop-off/pickup at the same coordinate.

Trip intervals are half-open: passengers ending at a location do not overlap those starting there. Each individual count is positive.

**Follow-up:** How would the fixed 0..1000 location bound support a difference-array implementation?

## Python and C++23

C++ uses an ordered std::map, giving deterministic O(t log t) time and O(t) auxiliary storage, whereas Python hashes changes before sorting. Trips are passed by reference and preserved; occupancy is bounded by 100000 passengers under the trip/count limits. The JSON adapter owns decoded inputs; its conversion copies are outside the solution bounds.
