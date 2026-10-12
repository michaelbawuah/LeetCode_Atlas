from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        following, pending = {}, []
        for value in nums2:
            while pending and pending[-1] < value:
                following[pending.pop()] = value
            pending.append(value)
        return [following.get(value, -1) for value in nums1]
