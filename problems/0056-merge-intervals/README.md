# 56 · Merge Intervals

[Problem](https://leetcode.com/problems/merge-intervals/) · Medium · Sorting and intervals

## Idea

Sort by start so an incoming interval can overlap only the last merged interval.
Their union extends its end rather than introducing a new output interval.

**Baseline:** repeatedly search pairs for overlaps and merge them until none
remain. Repeated scans can be expensive.
**Chosen approach:** sort once and scan, extending the last end whenever
`start <= last_end`. Otherwise, append a fresh interval.

## Why it works

After each step, the output is the sorted disjoint union of all processed intervals.
The next start is no earlier than any processed start. If it exceeds the last
output end, there is a gap and a new component is necessary. Otherwise, it belongs
to the last component, whose new end is the maximum of the two ends. Earlier
components remain disjoint, maintaining the invariant.

## Complexity

Python: O(n log n) time and O(n) auxiliary space for `sorted` and its workspace,
plus O(n) output in the worst case. Output rows are new lists; input rows are
not mutated.

## Tests and pitfalls

Include nested, identical, unsorted, point, and touching intervals. The property
oracle marks integer and half-integer points to rebuild independent coverage
components. Half-integers distinguish adjacent disjoint intervals such as
`[1, 2]` and `[3, 4]`. Touching endpoints are merged for this problem.

**Follow-up:** how would endpoint conventions change for half-open intervals?

## Python and C++23 comparison

Python scans `sorted(intervals)`, allocating a sorted copy and leaving the caller's input unchanged. C++ instead calls `std::sort` on the supplied vector, changing its order, and copies merged intervals into a separate result. Both take O(n log n) time and up to O(n) output space. The C++ sort's internal auxiliary storage depends on the standard-library implementation; there is no extra full input copy in this source. The local adapter supplies a fresh vector for each test call. The shared checker accepts arbitrary order between output intervals while preserving `[start, end]` endpoint order, as this problem permits.
