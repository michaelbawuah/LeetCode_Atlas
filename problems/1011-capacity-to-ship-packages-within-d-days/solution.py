class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        left, right = max(weights), sum(weights)
        while left < right:
            capacity = (left + right) // 2
            used, load = 1, 0
            for weight in weights:
                if load + weight > capacity:
                    used += 1
                    load = 0
                load += weight
            if used <= days:
                right = capacity
            else:
                left = capacity + 1
        return left
