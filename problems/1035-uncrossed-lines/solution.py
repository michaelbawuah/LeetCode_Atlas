class Solution:
    def maxUncrossedLines(self, nums1: list[int], nums2: list[int]) -> int:
        if len(nums1) < len(nums2):
            nums1, nums2 = nums2, nums1
        best = [0] * (len(nums2) + 1)
        for first in nums1:
            diagonal = 0
            for column, second in enumerate(nums2, start=1):
                above = best[column]
                best[column] = (
                    diagonal + 1 if first == second else max(best[column], best[column - 1])
                )
                diagonal = above
        return best[-1]
