# 50. Pow(x, n)

[Problem on LeetCode](https://leetcode.com/problems/powx-n/) · Medium

## Approach, invariant, and complexity

Write the exponent in binary. Each squaring advances to the next bit, and set bits contribute the corresponding power to the result.

A baseline multiplies |n| times. Binary exponentiation takes O(log(|n| + 1)) multiplications and O(1) auxiliary space. After negative-exponent normalization, the mathematical invariant is accumulated result × current base raised to remaining exponent = desired power. Consuming a bit and squaring the base preserves it.

Floating-point rounding means the invariant holds mathematically rather than bit-for-bit in the machine representation. Comparisons therefore use the configured approximate checker. For negative n, invert the nonzero base first. Python's unbounded integer negation handles the minimum signed 32-bit exponent safely. x = 0 appears only with positive n in fixtures.

Follow-up: adapt the algorithm to modular exponentiation. When does a negative exponent have a modular inverse?

## Verification

Named fixtures and an independent generated-input reference cover behavior. Judge results are recorded separately in metadata.
