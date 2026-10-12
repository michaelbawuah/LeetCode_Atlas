class Solution:
    def checkPossibility(self, nums: list[int]) -> bool:
        previous = nums[0]
        changes = 0
        for index in range(1, len(nums)):
            value = nums[index]
            if previous <= value:
                previous = value
                continue
            changes += 1
            if changes > 1:
                return False
            if index < 2 or nums[index - 2] <= value:
                previous = value
        return True
