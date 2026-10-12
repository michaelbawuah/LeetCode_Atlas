from heapq import heapify, heappushpop
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        largest = nums[:k]
        heapify(largest)
        for index in range(k, len(nums)):
            heappushpop(largest, nums[index])
        return largest[0]
