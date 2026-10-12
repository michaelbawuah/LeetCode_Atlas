class Solution:
    def findMaxLength(self, nums: list[int]) -> int:
        earliest = {0: -1}
        balance = best = 0
        for index, value in enumerate(nums):
            balance += 1 if value else -1
            if balance in earliest:
                best = max(best, index - earliest[balance])
            else:
                earliest[balance] = index
        return best
