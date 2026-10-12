class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        ordered = sorted(nums)
        result: list[list[int]] = []
        for anchor in range(len(ordered) - 2):
            if ordered[anchor] > 0:
                break
            if anchor and ordered[anchor] == ordered[anchor - 1]:
                continue
            left, right = anchor + 1, len(ordered) - 1
            while left < right:
                total = ordered[anchor] + ordered[left] + ordered[right]
                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    result.append([ordered[anchor], ordered[left], ordered[right]])
                    left += 1
                    right -= 1
                    while left < right and ordered[left] == ordered[left - 1]:
                        left += 1
                    while left < right and ordered[right] == ordered[right + 1]:
                        right -= 1
        return result
