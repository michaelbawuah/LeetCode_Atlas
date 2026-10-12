# 152 · Maximum Product Subarray

[Problem](https://leetcode.com/problems/maximum-product-subarray/) · Medium · Dynamic programming

## Approach

**Baseline:** enumerate nonempty subarrays with rolling products: O(n²) time.
**Chosen approach:** keep both the smallest and largest products ending at the
previous position. A negative value can turn the smallest product into the largest.

## Invariant and correctness

Every nonempty subarray ending at the current value either starts here or extends
a previous ending subarray. Multiplication by a positive value preserves ordering;
a negative value reverses it; zero collapses all extended products. Therefore
the extrema come from the singleton, the previous minimum times the value, or
the previous maximum times it. Updating both extrema from their old values
preserves the invariant; the largest maximum across endpoints is the answer.

## Complexity and languages

Both implementations use O(n) time and O(1) auxiliary space and preserve input.
C++ passes the vector by reference and evaluates the three candidates in `long long`.
The official constraints bound every subarray product to signed 32-bit range;
Python's integer arithmetic is consequently also bounded for this analysis.

## Verification and pitfalls

The oracle multiplies every nonempty slice. Tests cover zero-separated runs,
negative singletons, and sign flips. Initialize from the first element, and
compute both new extrema before replacing either old value.

**Follow-up:** which bookkeeping recovers the winning subarray's endpoints?
