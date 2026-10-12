from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cheapest = prices[0]
        best = 0
        for index in range(1, len(prices)):
            price = prices[index]
            best = max(best, price - cheapest)
            cheapest = min(cheapest, price)
        return best
