# 1137 · N-th Tribonacci Number

[LeetCode problem](https://leetcode.com/problems/n-th-tribonacci-number/)

## Intuition
The next term needs only the previous three values.

## Baseline and approach
Expanding the recurrence recursively repeats subproblems. Three rolling values avoid both repeated work and a full table.

## Why it works
Before each iteration the three states are consecutive Tribonacci terms. Adding them computes the next term, and shifting preserves that invariant. Separate initial cases establish T0=0, T1=1, and T2=1.

## Complexity
Python: **O(n + 1) time; O(1) auxiliary space**. n≤37 makes the output fit a signed 32-bit integer. C++ stores all states in int64_t before addition. Both versions use O(n+1) time/O(1) space; the independent oracle counts compositions by multinomial coefficients.

## Pitfalls
Do not use Fibonacci’s two-state update. n=0 is valid, and n=37 exercises the largest official answer.

## Follow-up
How would a three-by-three transition matrix compute much larger indices?

## C++23 counterpart
**O(n + 1) time; O(1) auxiliary space**. The implementation uses the same recurrence and preserves its inputs. JSON adaptation costs are separate from the submission method.

## Verification
Named fixtures and an independent generated-input oracle accompany this implementation. Official judge results are recorded separately in metadata.
