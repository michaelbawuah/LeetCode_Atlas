from collections import Counter


class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        counts = Counter(nums1)
        result: list[int] = []
        for value in nums2:
            if counts[value] > 0:
                result.append(value)
                counts[value] -= 1
        return result
