# 57 · Insert Interval

[Problem](https://leetcode.com/problems/insert-interval/) · Medium · Intervals

## Idea

The existing intervals are sorted and disjoint. Split them into intervals before
the new interval, intervals overlapping it, and intervals after its merged span.

**Baseline:** append the new interval, sort everything, and run interval merging:
O(n log n) time.
**Chosen approach:** make one forward pass in three phases, without sorting.
The overlap phase continually expands the new span's endpoints.

## Why it works

An interval ending before the new start is safely before the result and can be
copied unchanged. Every next interval starting at or before the growing end
belongs to its connected union; updating minimum start and maximum end preserves
that union. Once an interval starts after the end, sorted disjoint input ensures
all later intervals also come after it. Emitting that span between the copied
prefix and suffix therefore preserves order and disjointness.

## Complexity

Python: O(n) time and O(1) auxiliary space excluding O(n) output. Each interval
is visited once. Output rows are copied in constant-size steps, avoiding both
input mutation and a temporary suffix slice.

## Tests and pitfalls

Cases cover empty input, before/after insertion, containment, point intervals,
and a new interval touching both neighbors. The generated oracle reconstructs
coverage on a doubled integer grid. Endpoints that touch must merge. Remember
that the growing end can reach additional intervals beyond the first overlap.

**Follow-up:** what data structure would help support many insertions efficiently?

## Python and C++23 comparison

Both versions copy intervals into a new result while scanning the already sorted, disjoint input. C++ reserves room for at most n+1 output intervals and keeps the merged endpoints in scalar variables. Its result rows own their copied values; the input intervals and `newInterval` are not modified. Time is O(n), with O(1) auxiliary state apart from O(n) output. Unlike Merge Intervals, this problem requires the returned intervals to remain sorted by start.
