# 518 · Coin Change II

[LeetCode problem](https://leetcode.com/problems/coin-change-ii/)

## Intuition
Process denominations in a fixed order so each multiset of coins is counted once, regardless of the order in which its coins could be arranged.

## Baseline and approach
Enumerating each denomination’s possible multiplicity is a brute-force baseline. The optimized one-dimensional DP adds combinations containing the current denomination to each reachable subtotal.

## Why it works
After processing a denomination, counts[s] is the number of multisets using processed denominations totaling s. An ascending update reads counts[s−coin] after the current coin is available, permitting unlimited reuse. Keeping coins as the outer loop assigns every multiset a unique construction order. counts[0] is one for choosing no coins.

## Complexity
For amount a and c denominations, Python uses **O(c(a+1)) arithmetic operations and O(a+1) integer states**. Intermediate Python integers can be much wider than the final result. C++ uses the same recurrence with bounded 64-bit additions and O(c(a+1)) time/O(a+1) space. Neither changes the denominations.

## Pitfalls
The official bound applies only to the final answer. Lower-subtotal counts can exceed even 64 bits when the requested amount is unreachable: the named fixture uses odd amount 4999 with 300 even denominations. C++ caps each nonnegative count at INT_MAX and widens both operands before addition. Saturation obeys min(cap, x+y) = min(cap, min(cap,x)+min(cap,y)); therefore every DP state equals the true count capped at that limit. A guaranteed-bounded final count remains exact.

## Follow-up
Why does switching the loop order count ordered sequences rather than unordered coin combinations?

## Verification
Named fixtures and independent generated-input references accompany the implementation. Official judge results are tracked separately in metadata.
