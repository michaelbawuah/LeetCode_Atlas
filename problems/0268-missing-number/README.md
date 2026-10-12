# 268 · Missing Number

[Problem](https://leetcode.com/problems/missing-number/) · Easy · XOR cancellation

## Approach

**Baseline:** store the input in a set and scan the range 0 through n,
requiring O(n) auxiliary space.
**Chosen approach:** XOR all expected values with all provided values. Initialize
with n, then combine each index from 0 through n - 1 and its input value.

## Invariant and correctness

After each iteration, the accumulator contains the XOR of the expected values
processed so far and the provided prefix. At completion it represents every
value in 0 through n together with every input value. Every present value appears
twice and cancels; the missing value appears once and remains. This includes zero,
whose disappearance still produces the correct zero accumulator.

## Complexity

O(n) time and O(1) auxiliary space under the bounded-integer input model.
The method does not mutate the input or use a potentially large arithmetic sum.

## Verification and pitfalls

Generated valid ranges remove one value, permute the rest, and compare against
the independent arithmetic sum difference. Cases cover missing zero, missing n,
and a singleton. XOR both the index and value; forgetting the initial n omits
the range's final expected element.

**Follow-up:** how would you detect both a duplicated value and a missing value?
