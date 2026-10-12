# 50. Pow(x, n)

[Problem on LeetCode](https://leetcode.com/problems/powx-n/) · Medium

## Approach, invariant, and complexity

Write the exponent in binary. Each squaring advances to the next bit, and set bits contribute the corresponding power to the result.

A baseline multiplies |n| times. Binary exponentiation takes O(log(|n| + 1)) multiplications and O(1) auxiliary space. After negative-exponent normalization, the mathematical invariant is accumulated result × current base raised to remaining exponent = desired power. Consuming a bit and squaring the base preserves it.

Floating-point rounding means the invariant holds mathematically rather than bit-for-bit in the machine representation. Comparisons therefore use the configured approximate checker. For negative n, invert the nonzero base first. Python's unbounded integer negation handles the minimum signed 32-bit exponent safely. x = 0 appears only with positive n in fixtures.

Follow-up: adapt the algorithm to modular exponentiation. When does a negative exponent have a modular inverse?

## Verification

Named fixtures and an independent generated-input reference cover behavior. Judge results are recorded separately in metadata.

## C++23 counterpart

The exponent is converted to int64_t before negating it, so n = INT_MIN is defined. Negative exponents invert the nonzero base first. An unused final squaring is skipped; rounding is compared with the existing approximate checker. Generators include signed exponent limits with unit bases and keep all pairs within the official finite result bounds. Zero bases occur only with positive exponents.

C++: **O(log(|n| + 1)) time; O(1) space**. Named fixtures and 150 reproducible generated inputs compare this implementation with the Python track.
