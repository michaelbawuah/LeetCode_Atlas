class Solution:
    def fourSumCount(
        self, nums1: list[int], nums2: list[int], nums3: list[int], nums4: list[int]
    ) -> int:
        counts: dict[int, int] = {}
        for first in nums1:
            for second in nums2:
                total = first + second
                counts[total] = counts.get(total, 0) + 1
        answer = 0
        for third in nums3:
            for fourth in nums4:
                answer += counts.get(-third - fourth, 0)
        return answer
