from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        two_back, one_back = 0, 0
        for amount in nums:
            best = max(one_back, two_back + amount)
            two_back, one_back = one_back, best
        return one_back
