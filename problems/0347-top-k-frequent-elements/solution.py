from collections import Counter


class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        counts = Counter(nums)
        buckets: list[list[int]] = [[] for _ in range(len(nums) + 1)]
        for value, frequency in counts.items():
            buckets[frequency].append(value)
        result: list[int] = []
        for frequency in range(len(nums), 0, -1):
            for value in buckets[frequency]:
                result.append(value)
                if len(result) == k:
                    return result
        return result
