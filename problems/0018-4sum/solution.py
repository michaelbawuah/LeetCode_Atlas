class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        ordered = sorted(nums)
        result: list[list[int]] = []
        for first in range(len(ordered) - 3):
            if first and ordered[first] == ordered[first - 1]:
                continue
            for second in range(first + 1, len(ordered) - 2):
                if second > first + 1 and ordered[second] == ordered[second - 1]:
                    continue
                left, right = second + 1, len(ordered) - 1
                while left < right:
                    total = ordered[first] + ordered[second] + ordered[left] + ordered[right]
                    if total < target:
                        left += 1
                    elif total > target:
                        right -= 1
                    else:
                        result.append(
                            [ordered[first], ordered[second], ordered[left], ordered[right]]
                        )
                        left += 1
                        right -= 1
                        while left < right and ordered[left] == ordered[left - 1]:
                            left += 1
                        while left < right and ordered[right] == ordered[right + 1]:
                            right -= 1
        return result
