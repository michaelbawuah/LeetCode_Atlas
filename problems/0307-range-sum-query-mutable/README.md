# 307. Range Sum Query - Mutable

[Problem on LeetCode](https://leetcode.com/problems/range-sum-query-mutable/) · Medium

## Approach, invariant, and complexity

A Fenwick tree summarizes overlapping power-of-two blocks. Point changes touch O(log n) blocks; a prefix query combines O(log n) disjoint blocks.

A baseline directly sums the requested slice, O(n) worst-case query time, with O(1) updates. Here tree entry i stores the sum ending at one-based i over a block of length its lowest set bit. The linear constructor propagates each completed block to its parent. An update adds the same value difference to every containing block. Prefix traversal removes the lowest set bit to partition the prefix into the stored blocks, so subtracting two prefix sums gives an inclusive range.

Construction takes O(n) time, each update/query O(log n), and stored space O(n), including a copied value array for update differences. A prefix endpoint is exclusive while the public range's right endpoint is inclusive.

Repeated updates require the difference from the current value, not from the original value. Negative numbers are valid. The constructor preserves its input.

Follow-up: support adding a value to an entire range. Which pair of Fenwick trees can answer range sums?

## Verification

Named fixtures and an independent generated-input reference cover behavior. Judge results are recorded separately in metadata.

## C++23 counterpart

[Source](solution.cpp) · [Local adapter](cpp_runner.cpp)

Both implementations copy the initial values and build a Fenwick tree in linear time. C++ uses long long intermediate sums; returned sums fit int under the problem constraints.

Time: constructor O(n); update/sumRange O(log n). Space: O(n). The local adapter constructs a fresh object for each fixture and owns any converted inputs.
