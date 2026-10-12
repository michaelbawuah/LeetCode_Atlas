# 31 · Next Permutation

[Problem](https://leetcode.com/problems/next-permutation/) · Medium

## Idea and approaches

Increase the sequence at the rightmost position where an increase remains possible, then make its suffix minimal. A baseline enumerates and sorts all permutations, which is factorial.

## Correctness invariant

The suffix after the pivot is nonincreasing, so it is already maximal for its fixed prefix. Replacing the pivot with the smallest larger suffix value makes the smallest possible prefix increase. That suffix remains nonincreasing after the swap; reversing it supplies its smallest order. If no pivot exists, reversing the whole sequence wraps to the minimum.

## Complexity

O(n) time and O(1) auxiliary space. Mutate the existing list and return None; metadata serializes argument zero.

## Verification and pitfalls

The oracle enumerates distinct permutations of small multisets, chooses the next lexicographic one with wraparound, and verifies list identity. Named cases include duplicate successors and a descending input.

Find the successor from the right, and reverse only the suffix after the pivot. Duplicate values do not create distinct repeated answers.

**Follow-up:** How could you compute the kth lexicographic permutation without applying this step k times?

## Python and C++23

C++ uses std::reverse for the suffix and scalar indices. The vector is passed by reference, so there is no input parameter copy. Python uses explicit swaps; both have the same mutation and complexity. The JSON adapter owns decoded inputs; its conversion copies are outside the solution bounds.
