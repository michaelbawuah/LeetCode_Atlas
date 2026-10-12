# 322 · Coin Change

[LeetCode problem](https://leetcode.com/problems/coin-change/)

## Intuition
For a subtotal, try which coin could be last. The previous subtotal already tells us the smallest number of coins needed before it.

## Baseline and approach
A search tree branches once per possible coin at every step. A table indexed by subtotal reuses those repeated states, giving an unbounded minimum-coin dynamic program.

## Why it works
Before processing subtotal s, every smaller subtotal already has its optimal count or the unreachable marker. Positive coin values make s−coin smaller than s. Removing a final coin from any valid solution gives one of these predecessor states; minimizing their counts plus one therefore finds the optimum.

## Complexity
For amount a and c denominations: **O(a × c) time, O(a) auxiliary space**.

## Pitfalls
Greedy largest-coin selection fails for denominations such as 1, 3, and 4 at amount 6. Amount zero needs no coins. The sentinel a+1 exceeds any feasible count because every coin is positive.

## Follow-up
How would the recurrence change if each denomination had a limited inventory?

## Python and C++23 comparison

Both versions tabulate the smallest coin count for every subtotal through amount a. C++ allocates a vector of a+1 integers, uses a+1 as the unreachable marker, and considers each of c denominations at every positive subtotal. Time is O(a c + a + 1), including table initialization; auxiliary space is O(a + 1) and output is one integer. The +1 terms include amount zero explicitly. Positive official coin values make every predecessor subtotal smaller, and the official amount bound keeps sentinel arithmetic within `int`. Neither coin list is changed.
