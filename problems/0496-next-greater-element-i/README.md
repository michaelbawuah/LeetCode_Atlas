# 496. Next Greater Element I

[Problem on LeetCode](https://leetcode.com/problems/next-greater-element-i/) · Easy

## Approach

Searching forward from each query can take O(nm). A decreasing stack resolves every earlier smaller value when its first greater value arrives.

## Invariant and correctness

Pending values have no greater value in their processed suffix. A new larger value is therefore the first greater value for every popped entry, while all unpopped entries remain unresolved.

## Complexity

Time: O(n + m) expected. Space: O(n) auxiliary; O(m) output.

## Boundaries and pitfalls

nums2 values are distinct and nums1 is its subset. Each stack entry is pushed and popped at most once; hash-map costs are expected.

## Follow-up

Handle duplicate values by indexing occurrences instead of using value keys.

## Verification

Named cases and an independent generated-input oracle or operation model accompany the source. Judge results are recorded separately in metadata.

## C++23 counterpart

[Source](solution.cpp) · [Local adapter](cpp_runner.cpp) · [Parity generator](parity.py)

Both versions preserve input unless the problem specifies mutation. C++ string arguments use const references; adapter-decoded inputs are separately owned and excluded from solution auxiliary space.

Time: O(n + m) expected. Space: O(n) auxiliary; O(m) output.
