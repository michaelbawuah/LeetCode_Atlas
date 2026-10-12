class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        values = set(nums)
        best = 0
        for start in values:
            if start - 1 in values:
                continue
            end = start
            while end + 1 in values:
                end += 1
            best = max(best, end - start + 1)
        return best
