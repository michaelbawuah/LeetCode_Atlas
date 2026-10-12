class Solution:
    def maximumGap(self, nums: list[int]) -> int:
        if len(nums) < 2:
            return 0
        smallest, largest = min(nums), max(nums)
        if smallest == largest:
            return 0
        width = max(1, (largest - smallest) // (len(nums) - 1))
        count = (largest - smallest) // width + 1
        minima: list[int | None] = [None] * count
        maxima: list[int | None] = [None] * count
        for value in nums:
            bucket = (value - smallest) // width
            if minima[bucket] is None:
                minima[bucket] = maxima[bucket] = value
            else:
                minima[bucket] = min(minima[bucket], value)
                maxima[bucket] = max(maxima[bucket], value)
        best, previous = 0, smallest
        for low, high in zip(minima, maxima, strict=True):
            if low is not None:
                best = max(best, low - previous)
                previous = high
        return best
