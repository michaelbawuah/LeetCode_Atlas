# 350 · Intersection of Two Arrays II

[Problem](https://leetcode.com/problems/intersection-of-two-arrays-ii/) · Easy

## Idea and approaches

Count the first array and consume one available copy per matching second-array value. A baseline compares all pairs while tracking consumed positions; a frequency map avoids repeated searches.

## Correctness invariant

Before processing a second-array value, its count represents unmatched occurrences remaining in the first array. A positive count permits one match and is decremented exactly once. No match can use a first-array occurrence twice. After all second values are processed, each value appears the minimum of its two input frequencies.

## Complexity

O(n + m) expected time, O(u) auxiliary space for u distinct first-array values, and up to O(min(n, m)) output. Inputs are preserved.

## Verification and pitfalls

The independent oracle sorts both inputs and performs a two-pointer multiset merge. Named cases verify unequal frequencies, zeroes, and disjoint arrays.

Unlike problem 349, repeated intersection values matter. A set would lose valid matches.

**Follow-up:** How would you choose which input to count when their sizes differ greatly?
