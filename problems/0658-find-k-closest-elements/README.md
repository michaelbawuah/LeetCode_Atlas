# 658 · Find K Closest Elements

[Problem](https://leetcode.com/problems/find-k-closest-elements/) · Medium

## Idea and approaches

The k closest values form a contiguous sorted window. A full distance sort is an O(n log n) baseline; binary-search its starting position instead.

## Correctness invariant

For candidate windows starting at i and i + 1, their shared middle values cancel. Compare x - arr[i] with arr[i + k] - x: if the left endpoint is farther, shifting right is better; otherwise the left window is better, including ties favoring the smaller value. Sorted order makes this preference monotone, so binary search finds an optimal start.

## Complexity

O(log(n - k + 1) + k) time and O(1) auxiliary space excluding O(k) output. Both languages copy just the selected output window and preserve input.

## Verification and pitfalls

The independent oracle sorts values by (absolute distance, value), takes k, then restores ascending output order. Fixtures cover ties, duplicate boundaries, and targets outside the array.

Use a strict greater-than comparison so ties stay left. k is at most the array length.

**Follow-up:** Which two-pointer trimming method provides a simpler O(n - k) alternative?

## Python and C++23

C++ builds only the selected result vector from an iterator range. The input is passed by reference and preserved; legal values and x keep the endpoint differences within int. The JSON adapter owns decoded inputs; its conversion copies are outside the solution bounds.
