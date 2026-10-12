# 560 · Subarray Sum Equals K

[Problem](https://leetcode.com/problems/subarray-sum-equals-k/) · Medium · Prefix sums and frequency map

## Approach

**Baseline:** enumerate each start and extend a rolling sum across every end:
O(n²) time.
**Chosen approach:** at a current prefix sum P, count earlier prefixes equal
to `P - k`. Their differences identify subarrays summing to k.

## Invariant and correctness

Before processing an endpoint, the frequency map counts exactly the preceding
prefix sums, including the empty prefix zero. For every earlier prefix Q,
the intervening nonempty subarray sums to `P - Q`. Thus the frequency of `P - k`
counts all matches ending here, once each. Registering P only afterward prevents
counting an empty subarray when k is zero.

## Complexity and languages

Both solutions use O(n) expected time and O(n) auxiliary space, assuming expected
constant-time hash operations. They preserve input and C++ receives it by reference.
C++ uses `long long` prefix keys and an `int` count; the maximum number of matches
under the length bound fits the return type. JSON adapter copies are excluded.

## Verification and pitfalls

The independent oracle sums every short slice. Include negative targets, zeroes,
repeated prefix sums, and unmatched singletons. A sliding window that assumes
positive values is invalid here. Store frequencies rather than only prefix membership.

**Follow-up:** how does the map change when counting sums divisible by k?
