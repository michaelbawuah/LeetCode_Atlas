from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        candidates: deque[int] = deque()
        result: list[int] = []
        for index, value in enumerate(nums):
            if candidates and candidates[0] <= index - k:
                candidates.popleft()
            while candidates and nums[candidates[-1]] <= value:
                candidates.pop()
            candidates.append(index)
            if index >= k - 1:
                result.append(nums[candidates[0]])
        return result
