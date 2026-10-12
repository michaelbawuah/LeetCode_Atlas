# 1220 · Count Vowels Permutation

[LeetCode problem](https://leetcode.com/problems/count-vowels-permutation/)

## Intuition
Count strings by their final vowel, using the allowed preceding vowels for each next state.

## Baseline and approach
Enumerating vowel strings is exponential. Five rolling counts aggregate all strings that share a final vowel.

## Why it works
Every legal string of the next length has a unique previous final vowel and a legal transition to its new final vowel. Summing those predecessor counts covers each string exactly once. Starting every vowel at one counts the five single-letter strings; the final state sum counts all endpoints.

## Complexity
Python: **O(n) time; O(1) auxiliary space**. n is length. Five bounded modular states use O(n) time/O(1) space. C++ uses int64_t operands before three-way additions and the final sum. The oracle independently exponentiates the adjacency matrix.

## Pitfalls
Use incoming transitions rather than accidentally reversing the rules. In particular i can follow e or o, while i may itself precede four different vowels. Apply the required modulus.

## Follow-up
How would adjacency-matrix exponentiation reduce the dependence on n?

## C++23 counterpart
**O(n) time; O(1) auxiliary space**. The implementation uses the same recurrence and preserves its inputs. JSON adaptation costs are separate from the submission method.

## Verification
Named fixtures and an independent generated-input oracle accompany this implementation. Official judge results are recorded separately in metadata.
