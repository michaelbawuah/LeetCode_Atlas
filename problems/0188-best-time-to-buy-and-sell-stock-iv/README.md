# 188 · Best Time to Buy and Sell Stock IV

[LeetCode problem](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/)

## Intuition
Generalize buy and sell states to each allowed transaction count.

## Baseline and approach
Enumerating daily actions is exponential. Rolling held/cash arrays keep the best outcomes at each transaction budget. If the budget cannot bind, sum all positive adjacent gains.

## Why it works
For each budget, a sale extends its previous held state and a purchase extends the preceding budget’s cash state. Descending budget updates preserve earlier-day predecessors. The cash states allow fewer transactions, so their final maximum covers every legal sequence up to k trades. At least n/2 trades suffice for every profitable alternating buy/sell sequence, justifying the unlimited branch.

## Complexity
Python: **O(1 + n min(k, n)) time; O(k) general case; O(1) unlimited branch auxiliary space**. n is price count and k the budget. General processing uses O(k) states and O(nk) work. The unlimited branch uses O(n) time and O(1) storage, giving the stated bound.

## Pitfalls
The official public domain starts at k=1. Do not count a buy as a completed transaction. Avoid copying the price suffix in the unlimited branch.

## Follow-up
How would a transaction-dependent fee change the transitions?

## Verification
Named fixtures and an independent generated-input oracle accompany this implementation. Official judge results are recorded separately in metadata.
