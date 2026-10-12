class Solution:
    def maxProfit(self, prices: list[int], fee: int) -> int:
        cash, held = 0, -prices[0]
        for index in range(1, len(prices)):
            price = prices[index]
            cash, held = max(cash, held + price - fee), max(held, cash - price)
        return cash
