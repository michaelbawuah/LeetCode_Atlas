# 853. Car Fleet

[Problem on LeetCode](https://leetcode.com/problems/car-fleet/) · Medium

## Intuition
Work backward from the car closest to the target. A car behind joins the fleet in front if its free arrival time is no later than that fleet's arrival time.

## Approaches
- **Baseline:** sort cars and compare each free arrival time with every car ahead: O(n²) time after sorting, O(n) space.
- **Optimized:** scan positions in descending order and retain only the latest front fleet's arrival-time ratio. A strictly later arrival starts another fleet.

## Correctness invariant
After a prefix of the descending-position scan, the fleet count is correct for those cars and the retained ratio is the arrival time of their rearmost fleet. A faster car behind catches that fleet at or before the target and cannot pass it. A slower arrival remains separate and becomes the new rearmost fleet. Equality merges because meeting at the target counts as a fleet.

## Complexity
O(n log n) time for sorting and O(n) extra space for sorted car pairs. The scan itself is O(n).

## Edge cases and pitfalls
Positions are distinct but input order is arbitrary. Compare ratios by cross multiplication, avoiding floating-point equality issues. Each distance and speed is positive under the input contract; Python integers keep the comparison exact.

## Follow-up
Return the members of each fleet, or compute the first collision time for every car rather than only the fleet count.

## Verification
Named fixtures and an independent generated-input reference accompany this implementation. Official judge results are tracked separately in metadata.
