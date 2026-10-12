class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        ordered = sorted(nums)
        best = sum(ordered[:3])
        for anchor in range(len(ordered) - 2):
            left, right = anchor + 1, len(ordered) - 1
            while left < right:
                total = ordered[anchor] + ordered[left] + ordered[right]
                if abs(total - target) < abs(best - target):
                    best = total
                if total == target:
                    return total
                if total < target:
                    left += 1
                else:
                    right -= 1
        return best
