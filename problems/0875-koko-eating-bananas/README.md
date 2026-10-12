# 875. Koko Eating Bananas

[Problem on LeetCode](https://leetcode.com/problems/koko-eating-bananas/) · Medium

## Intuition
If a speed finishes on time, every faster speed also finishes on time. Search for the first feasible speed instead of trying them all.

## Approaches
- **Baseline:** test speeds from 1 through the largest pile: O(nM) time, O(1) extra space.
- **Optimized:** binary search that range using the total number of whole hours required at a proposed speed.

## Correctness invariant
The minimum feasible speed stays inside `[left, right]`, and right is feasible. A feasible middle allows discarding every larger candidate while retaining middle. An infeasible middle rules out itself and all smaller speeds. When the bounds meet, that sole remaining candidate is the minimum feasible speed.

## Complexity
O(n log M) time for n piles and maximum pile size M, with O(n) work for the feasibility check. O(1) extra space because the sum consumes a generator.

## Edge cases and pitfalls
Each pile consumes a whole number of hours, so use integer ceiling division. Piles cannot be combined within one hour. The problem guarantees at least one hour per pile, making the largest pile a feasible upper bound.

## Follow-up
Change the schedule so one hour may consume bananas from several piles. How does the feasibility predicate change?

## Verification
Named fixtures and an independent generated-input reference accompany this implementation. Official judge results are tracked separately in metadata.

## Python and C++23 comparison

Both sources binary-search the first feasible speed and compute each pile's hours with integer ceiling division. C++ widens before `pile + speed - 1` and accumulates hours in `long long`; it can stop a feasibility scan as soon as the budget h is exceeded. Python's sum evaluates all piles for each candidate speed. These differ in early stopping but retain O(n log(M + 1)) worst-case time for n piles and maximum size M, including the initial maximum scan. Both use O(1) auxiliary storage and return one integer without modifying piles.
