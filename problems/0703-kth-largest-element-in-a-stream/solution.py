from heapq import heappush, heapreplace
from typing import List


class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self._k = k
        self._largest = []
        for value in nums:
            self.add(value)

    def add(self, val: int) -> int:
        if len(self._largest) < self._k:
            heappush(self._largest, val)
        elif val > self._largest[0]:
            heapreplace(self._largest, val)
        return self._largest[0]
