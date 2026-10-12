class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        first, second, write = m - 1, n - 1, m + n - 1
        while second >= 0:
            if first >= 0 and nums1[first] > nums2[second]:
                nums1[write] = nums1[first]
                first -= 1
            else:
                nums1[write] = nums2[second]
                second -= 1
            write -= 1
