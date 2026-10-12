class Solution:
    def maxProfit(self, k: int, prices: list[int]) -> int:
        if k == 0:
            return 0
        if k >= len(prices) // 2:
            return sum(max(0, prices[index] - prices[index - 1]) for index in range(1, len(prices)))
        cash = [0] * (k + 1)
        held = [float("-inf")] * (k + 1)
        for price in prices:
            for completed in range(k, 0, -1):
                cash[completed] = max(cash[completed], held[completed] + price)
                held[completed] = max(held[completed], cash[completed - 1] - price)
        return cash[-1]
