class Solution:
    def findLength(self, nums1: list[int], nums2: list[int]) -> int:
        if len(nums1) < len(nums2):
            nums1, nums2 = nums2, nums1
        best = [0] * (len(nums2) + 1)
        longest = 0
        for first in nums1:
            for column in range(len(nums2), 0, -1):
                best[column] = best[column - 1] + 1 if first == nums2[column - 1] else 0
                longest = max(longest, best[column])
        return longest
