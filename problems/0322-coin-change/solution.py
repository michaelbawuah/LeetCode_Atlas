class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        unreachable = amount + 1
        best = [0] + [unreachable] * amount
        for subtotal in range(1, amount + 1):
            for coin in coins:
                if coin <= subtotal:
                    best[subtotal] = min(best[subtotal], best[subtotal - coin] + 1)
        return best[amount] if best[amount] != unreachable else -1
