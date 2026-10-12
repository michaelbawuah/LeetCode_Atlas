# 567. Permutation in String

[Problem on LeetCode](https://leetcode.com/problems/permutation-in-string/) · Medium

## Intuition
The order of a permutation may change, but its letter frequencies cannot. Compare s1 with every window of the same length in s2.

## Approaches
- **Baseline:** sort s1 and every length-m candidate substring: O(n m log m) time in the worst case, O(m) extra space, where m = len(s1) and n = len(s2).
- **Optimized:** add the entering letter and remove the leaving letter from a fixed-width frequency window; compare two 26-entry arrays.

## Correctness invariant
After processing an index, `window` counts exactly the last min(m, processed length) letters. Once its width reaches m, equality with the required counts is equivalent to being a permutation of s1. The scan visits every possible length-m substring.

## Complexity
O(m + n) time for the fixed 26-letter alphabet, including array comparisons. O(1) extra space. For a variable alphabet of size a, the comparisons cost O(a) per candidate.

## Edge cases and pitfalls
s1 longer than s2 immediately fails. Duplicate letters require matching multiplicities, not merely matching a set. Remove the old character before comparing a full window.

## Follow-up
Return all starting indexes of matching windows instead of stopping at the first match.

## Verification
Named local cases and an independent generated-input oracle accompany this solution. No official judge result is recorded.

## C++23 counterpart

C++ compares two 26-entry `std::array` frequency tables and removes the leaving character before checking a full window. Inputs are nonempty lowercase a–z strings; duplicates remain counted individually. The algorithm uses O(m + n) time and O(1) auxiliary state. Its standard by-value string parameters may copy O(m + n) input storage, which is excluded from that auxiliary bound.
