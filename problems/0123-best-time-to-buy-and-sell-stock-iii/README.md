# 123 · Best Time to Buy and Sell Stock III

[LeetCode problem](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/)

## Intuition
Track the best cash after the first buy, first sale, second buy, and second sale.

## Baseline and approach
Enumerating legal daily actions is exponential. Four rolling states represent all choices for at most two transactions.

## Why it works
Each state either retains the best earlier value or performs its next action at the current price. Buying the second share starts from first-sale cash; selling it starts from second-buy cash. The four states therefore cover all ordered buy/sell sequences with no overlapping holdings. Same-day transitions add only zero-profit boundaries and do not create an extra profitable trade.

## Complexity
Python: **O(n) time; O(1) auxiliary space**. n is the number of prices. Only four scalars are stored; no price-array slices are made and the input is preserved.

## Pitfalls
At most two trades permits doing none. Do not add independent best profits from overlapping date ranges. Prices may be zero.

## Follow-up
How does adding a cooldown day change the available states?

## Verification
Named fixtures and an independent generated-input oracle accompany this implementation. Official judge results are recorded separately in metadata.

## C++23 counterpart

Four int64_t state values implement at most two completed transactions and leave the input vector unchanged. Official prices are between 0 and 100000, so the returned profit is at most 200000 and narrowing to int is safe. Same-day transitions add no extra positive profit; the algorithm does not copy a price suffix.

C++: **O(n) time; O(1) space**. Named fixtures and 150 reproducible generated inputs compare this implementation with the Python track.
