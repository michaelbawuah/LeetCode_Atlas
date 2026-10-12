# 295. Find Median from Data Stream

[Problem on LeetCode](https://leetcode.com/problems/find-median-from-data-stream/) · Hard

## Intuition
The median lies between the lower and upper halves of sorted values. Keep only their boundary values quickly accessible with two heaps.

## Approaches
- **Baseline:** store all values and sort on each median query: O(1) amortized insertion, O(n log n) query, O(n) space.
- **Optimized:** keep a max-heap for the lower half and a min-heap for the upper half, balanced so the lower half has either equal size or one extra element.

## Correctness invariant
Every value in the lower heap is at most every value in the upper heap, and their sizes differ by at most one with the lower heap never smaller. Push into the lower heap, transfer its largest value to the upper heap, and transfer back if the upper heap becomes larger. These moves preserve the partition and restore the size rule. The lower boundary is the odd-length median; averaging both boundaries gives the even-length median.

## Complexity
`addNum` takes O(log n) time, `findMedian` takes O(1) time, and both heaps together store O(n) values. Python list-backed heap operations have the usual amortized allocation cost.

## Edge cases and pitfalls
Duplicate and negative values require no special cases. Negation implements the lower max-heap. Always return a float, including an odd-length median. Queries are only made after at least one value has been added.

## Follow-up
If the value range is very small and fixed, replace the heaps with frequency counts. How would that change insertion and query costs?

## Verification
Named fixtures and an independent generated-input reference accompany this implementation. Official judge results are tracked separately in metadata.
