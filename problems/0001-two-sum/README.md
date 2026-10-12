# 1 · Two Sum

[Problem](https://leetcode.com/problems/two-sum/) · Easy · Hash map

## Idea

For a value `x`, the only possible partner is `target - x`. Remember earlier
values and their indices so that partner lookup is fast.

**Baseline:** compare every pair of distinct indices: O(n²) time and O(1) space.
**Chosen approach:** scan once, look for the complement, then store the current
value. For `[3, 2, 4]` with target `6`, the first `3` cannot match itself; `4`
eventually finds the earlier `2` and returns `[1, 2]`.

## Why it works

Before iteration `i`, the map contains only indices smaller than `i`. Any match
therefore uses distinct indices and sums to the target. When the later member
of the guaranteed pair is reached, its earlier partner is already in the map.

## Complexity

O(n) expected time and O(n) auxiliary space, assuming expected constant-time
dictionary operations. Hash tables do not promise constant-time worst-case lookup.

## Tests and pitfalls

Cases cover equal values, zeroes, negative complements, and large magnitudes.
Checking before insertion prevents reusing the same element. The generated test
enumerates valid index pairs; it also exercises inputs with multiple witnesses
to verify that a returned pair is valid rather than requiring one arbitrary order.
The named-case checker also permits either order of the two returned indices,
as LeetCode does; it preserves duplicates so a repeated index cannot pass.

**Follow-up:** if the array is sorted, how do two pointers trade extra memory for
a stronger input assumption?
