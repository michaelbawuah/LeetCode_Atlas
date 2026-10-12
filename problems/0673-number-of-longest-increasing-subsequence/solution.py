class Solution:
    def findNumberOfLIS(self, nums: list[int]) -> int:
        lengths = [1] * len(nums)
        counts = [1] * len(nums)
        for end in range(len(nums)):
            for previous in range(end):
                if nums[previous] < nums[end]:
                    candidate = lengths[previous] + 1
                    if candidate > lengths[end]:
                        lengths[end] = candidate
                        counts[end] = counts[previous]
                    elif candidate == lengths[end]:
                        counts[end] += counts[previous]
        longest = max(lengths)
        return sum(
            count for length, count in zip(lengths, counts, strict=True) if length == longest
        )
