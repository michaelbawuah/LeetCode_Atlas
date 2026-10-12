class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        two_back, one_back = 0, 0
        for step in range(2, len(cost) + 1):
            best = min(one_back + cost[step - 1], two_back + cost[step - 2])
            two_back, one_back = one_back, best
        return one_back
