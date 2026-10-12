# 714 · Best Time to Buy and Sell Stock with Transaction Fee

[LeetCode problem](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/)

## Intuition
Retain the best cash while owning no share and while owning one share.

## Baseline and approach
Enumerating legal daily buy/sell/skip actions is exponential. Two rolling states maximize profit for each holding status.

## Why it works
A cash state either keeps earlier cash or sells a previously held share, paying the fee once. A held state either keeps that share or buys using previous cash. Simultaneous updates preserve earlier-day predecessors and cover every legal nonoverlapping trading sequence.

## Complexity
Python: **O(n) time; O(1) auxiliary space**. n is price count. Both versions keep two states and use O(n) time/O(1) space. Prices are preserved. C++ cash states are int64_t before additions and the bounded final int conversion.

## Pitfalls
Charge the fee once per completed transaction. Compare against doing nothing, especially when every trade loses money. Avoid a prices[1:] copy if claiming constant auxiliary space.

## Follow-up
How would an additional cooldown day change the purchase predecessor?

## C++23 counterpart
**O(n) time; O(1) auxiliary space**. The implementation uses the same recurrence and preserves its inputs. JSON adaptation costs are separate from the submission method.

## Verification
Named fixtures and an independent generated-input oracle accompany this implementation. Official judge results are recorded separately in metadata.
