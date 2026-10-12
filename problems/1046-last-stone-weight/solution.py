from heapq import heapify, heappop, heappush
from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        remaining = [-stone for stone in stones]
        heapify(remaining)
        while len(remaining) > 1:
            heavier = -heappop(remaining)
            lighter = -heappop(remaining)
            if heavier != lighter:
                heappush(remaining, -(heavier - lighter))
        return -remaining[0] if remaining else 0
