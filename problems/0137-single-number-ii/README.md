# 137 · Single Number II

[Problem](https://leetcode.com/problems/single-number-ii/) · Medium

## Idea and approaches

Track each bit count modulo three with two bit masks. A frequency map is a linear-time baseline using O(n) memory; the masks encode all bit counters in constant space.

## Correctness invariant

For each bit, the state cycles from absent to seen once to seen twice and back to absent when that bit is encountered. The first assignment forms the new once mask, excluding bits already in twice; the second forms the new twice mask while excluding new once bits. Triplicates therefore cancel, leaving exactly the singleton bit pattern.

## Complexity

O(n) time and O(1) auxiliary space for bounded signed 32-bit inputs. Python bitwise operations preserve signed cancellation without per-number storage.

## Verification and pitfalls

Properties generate shuffled valid triplicates plus one singleton and use an independent occurrence counter. Named tests include both signed endpoints and negative singletons.

The update order matters because twice uses the new once mask. Ordinary XOR cancels pairs rather than groups of three.

**Follow-up:** How would you construct a bit-state machine when other values occur five times?

## Python and C++23

C++ uses uint32_t masks and bit_cast to recover the signed int32_t singleton, avoiding out-of-range signed narrowing. It reads the vector by reference and preserves it. Python handles signed bitwise states directly. The JSON adapter owns decoded inputs; its conversion copies are outside the solution bounds.
