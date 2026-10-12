# 525 · Contiguous Array

[Problem](https://leetcode.com/problems/contiguous-array/) · Medium

## Idea and approaches

Map zero to -1 and one to +1, then find repeated prefix balances. Enumerating and counting every slice is the quadratic-or-worse baseline.

## Correctness invariant

Equal prefix balances mean the intervening subarray has total zero, so it contains equally many zeroes and ones. For a current balance, its earliest preceding occurrence yields the longest such subarray ending here. Keeping only the first occurrence and checking every endpoint therefore finds the global maximum.

## Complexity

O(n) expected time and O(n) auxiliary space for the earliest-index map. Input is preserved.

## Verification and pitfalls

The independent oracle counts zeroes and ones in every short slice. Fixtures cover a balanced whole array, one value only, and repeated balances.

Initialize balance zero at index -1 so balanced prefixes are included. Never overwrite an earlier index with a later occurrence.

**Follow-up:** How would the prefix signature track equal counts of three different values?

## Python and C++23

C++ retains the earliest balance index in an unordered_map, reserves linear capacity, and preserves its referenced vector. Balances, indices, and lengths fit int under the input length bound. The JSON adapter owns decoded inputs; its conversion copies are outside the solution bounds.
