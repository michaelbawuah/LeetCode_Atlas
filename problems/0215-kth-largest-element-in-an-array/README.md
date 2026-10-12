# 215. Kth Largest Element in an Array

[Problem on LeetCode](https://leetcode.com/problems/kth-largest-element-in-an-array/) · Medium

## Intuition
Only the largest k values seen so far can affect the answer. A min-heap lets the smallest of those retained values sit at the top.

## Approaches
- **Baseline:** sort all values and select rank k: O(n log n) time, O(n) space for a sorted copy.
- **Optimized:** heapify the first k values, then push each remaining value while removing the heap's smallest value.

## Correctness invariant
After each processed prefix, the heap holds its largest k values, counting duplicates separately. Adding a value and discarding the smallest preserves that set of ranks. The smallest retained value is therefore the kth largest when the whole input has been processed.

## Complexity
O(n log(k + 1)) time, including O(k) initial heap construction, and O(k) extra space. Writing log(k + 1) includes the O(n) k = 1 case explicitly.

## Edge cases and pitfalls
Rank is over elements, not distinct values. k = 1 asks for the maximum; k = n asks for the minimum. The input remains unchanged because the heap starts from a copied prefix.

## Follow-up
Compare this heap approach with randomized quickselect, including expected time, worst-case time, and mutation of the input.

## Verification
Named fixtures and an independent generated-input reference accompany this implementation. Official judge results are tracked separately in metadata.

## Python and C++23 comparison

Python maintains a copied min-heap of the largest k elements: O(n log(k + 1)) time and O(k) auxiliary space while preserving the input. C++ instead applies `std::nth_element` with descending comparison and returns position k−1. It partitions the supplied vector in place, changing the caller's element order without fully sorting either side. The STL contract gives average O(n) comparisons, not a worst-case linear guarantee. Its internal auxiliary storage is implementation-dependent; this source allocates no separate heap or full input copy. Output is a single integer. Local adapters create independent vectors for shared cases, so the mutation cannot affect later evaluations.
