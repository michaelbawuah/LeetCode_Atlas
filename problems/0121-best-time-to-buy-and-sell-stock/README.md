# 121. Best Time to Buy and Sell Stock

[Problem on LeetCode](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/) · Easy

## Intuition
For a sale today, only the cheapest price on an earlier day matters. Keep that price and the best profit seen so far.

## Approaches
- **Baseline:** try every buy/sell pair with the buy before the sale: O(n²) time, O(1) extra space.
- **Optimized:** scan left to right, update the best sale using the previous minimum, then include today's price in that minimum.

## Correctness invariant
Before each iteration, `cheapest` is the minimum of all earlier prices and `best` is the best legal trade among earlier days. Selling at the current price checks the best trade ending today. Updating the minimum preserves the invariant for the next day. A starting profit of zero permits no trade when every trade loses money.

## Complexity
O(n) time and O(1) extra space. Index iteration avoids allocating an input slice.

## Edge cases and pitfalls
A single day, equal prices, and descending prices all return zero. Do not use a future minimum for an earlier sale. A zero price is a valid buy price.

## Follow-up
How would the state change if two transactions were allowed, or each sale charged a fee?

## Verification
Named local cases and an independent generated-input oracle accompany this solution. No official judge result is recorded.
