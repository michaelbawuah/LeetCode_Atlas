class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        short, long = len(nums1), len(nums2)
        half = (short + long + 1) // 2
        low, high = 0, short
        while low <= high:
            cut1 = (low + high) // 2
            cut2 = half - cut1
            left1 = nums1[cut1 - 1] if cut1 else float("-inf")
            right1 = nums1[cut1] if cut1 < short else float("inf")
            left2 = nums2[cut2 - 1] if cut2 else float("-inf")
            right2 = nums2[cut2] if cut2 < long else float("inf")
            if left1 <= right2 and left2 <= right1:
                if (short + long) % 2:
                    return float(max(left1, left2))
                return (max(left1, left2) + min(right1, right2)) / 2
            if left1 > right2:
                high = cut1 - 1
            else:
                low = cut1 + 1
        raise ValueError("Inputs must be sorted and have a nonempty combined length")
