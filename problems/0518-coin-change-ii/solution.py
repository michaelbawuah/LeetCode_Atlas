class Solution:
    def change(self, amount: int, coins: list[int]) -> int:
        counts = [1] + [0] * amount
        for coin in coins:
            for subtotal in range(coin, amount + 1):
                counts[subtotal] += counts[subtotal - coin]
        return counts[amount]
