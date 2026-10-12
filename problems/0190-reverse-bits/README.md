# 190 · Reverse Bits

[LeetCode problem](https://leetcode.com/problems/reverse-bits/)

## Intuition
Repeatedly remove the input’s lowest bit and append it at the output’s right edge. Running exactly 32 steps includes leading zeros.

## Baseline and approach
Formatting a padded binary string and reversing it is a simple baseline. The submitted solution uses integer shifts and masks to avoid a temporary string.

## Why it works
After k iterations, result is the reversed order of the k least significant input bits, and the shifted input still contains the unprocessed bits. Shifting result left and adding the next low bit preserves this invariant. After 32 iterations every position in the fixed-width word has been transferred.

## Complexity
For a fixed 32-bit word: **O(1) time, O(1) auxiliary space**. For a generalized width w, time is O(w).

## Pitfalls
Stopping when the input becomes zero drops required leading-zero positions. The current judge domain uses even, nonnegative inputs up to 2³¹−2. Named fixtures follow that domain; a separately named robustness property checks all unsigned 32-bit values, including odd and high-bit inputs.

## Follow-up
If called repeatedly, how could a lookup table for reversed bytes reduce the work per call?
