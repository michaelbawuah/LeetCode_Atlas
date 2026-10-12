# 136 · Single Number

[Problem](https://leetcode.com/problems/single-number/) · Easy · XOR cancellation

## Approach

**Baseline:** count occurrences using a frequency map and select the unique one,
requiring O(n) extra space.
**Chosen approach:** XOR every value into a running accumulator starting at zero.

## Invariant and correctness

XOR is associative and commutative, with `x XOR x = 0` and `x XOR 0 = x`.
After each step the accumulator is the XOR of the processed prefix. Across the
whole array, every paired value cancels regardless of order; the one unpaired
value remains. Signed Python integers obey the same cancellation identities.

## Complexity

O(n) time and O(1) auxiliary space under the problem's bounded-integer model.
The input is preserved and no sorting or extra collection is needed.

## Verification and pitfalls

Properties generate valid pairs plus one singleton, shuffle them, and compare
with an independent occurrence counter. Appending a new pair must leave the
answer unchanged. Fixtures include negative and zero singletons. The technique
relies on every other value appearing exactly twice; it does not recover an
arbitrary one-occurrence value from unrestricted frequencies.

**Follow-up:** which bit-counting approach handles other values occurring three times?
