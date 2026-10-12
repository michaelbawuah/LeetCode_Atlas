class Solution:
    def climbStairs(self, n: int) -> int:
        two_back, one_back = 1, 1
        for _ in range(2, n + 1):
            two_back, one_back = one_back, two_back + one_back
        return one_back
