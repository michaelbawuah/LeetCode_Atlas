class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        candidate = votes = 0
        for value in nums:
            if votes == 0:
                candidate = value
            votes += 1 if value == candidate else -1
        return candidate
