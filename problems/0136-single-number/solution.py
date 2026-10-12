class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        answer = 0
        for value in nums:
            answer ^= value
        return answer
