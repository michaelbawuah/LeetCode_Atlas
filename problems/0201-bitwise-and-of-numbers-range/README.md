# 201 · Bitwise AND of Numbers Range

[LeetCode problem](https://leetcode.com/problems/bitwise-and-of-numbers-range/)

## Intuition
Only the shared high-bit prefix of the endpoints can remain set throughout the entire interval.

## Baseline and approach
Applying AND to every integer costs O(right−left+1). Shift both endpoints until they match, then restore their common prefix with zeroed low bits.

## Why it works
When two endpoints first differ at a bit, the interval crosses a boundary that forces that bit and all lower bits to be zero somewhere in the range. Shared higher bits remain unchanged in every value. Shifting removes exactly the nonshared suffix; shifting the common value back therefore yields the range AND.

## Complexity
For word width w, **O(w) time and O(1) space** under the fixed nonnegative signed 32-bit domain; at most 31 shifts are needed. C++ performs shifts on uint32_t values before returning the bounded int result. Neither implementation enumerates the range.

## Pitfalls
An interval can have two adjacent numbers and still cross a high power-of-two boundary. Equal endpoints return that value, including zero. Avoid signed-shift assumptions in portable C++.

## Follow-up
How does repeatedly clearing the lowest set bit of right provide an alternative algorithm?

## Verification
Named fixtures and independent generated-input references accompany the implementation. Official judge results are tracked separately in metadata.
