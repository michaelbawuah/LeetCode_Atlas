class Solution:
    def countVowelPermutation(self, n: int) -> int:
        a = e = i = o = u = 1
        modulus = 1_000_000_007
        for _ in range(2, n + 1):
            a, e, i, o, u = (
                (e + i + u) % modulus,
                (a + i) % modulus,
                (e + o) % modulus,
                i,
                (i + o) % modulus,
            )
        return (a + e + i + o + u) % modulus
