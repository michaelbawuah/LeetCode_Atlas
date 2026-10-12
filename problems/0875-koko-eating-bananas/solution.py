from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        while left < right:
            middle = left + (right - left) // 2
            hours = sum((pile + middle - 1) // middle for pile in piles)
            if hours <= h:
                right = middle
            else:
                left = middle + 1
        return left
