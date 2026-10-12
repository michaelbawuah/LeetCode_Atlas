class Solution:
    def numTilings(self, n: int) -> int:
        if n < 3:
            return (1, 1, 2)[n]
        first, second, third = 1, 1, 2
        modulus = 1_000_000_007
        for _ in range(3, n + 1):
            first, second, third = second, third, (2 * third + first) % modulus
        return third
