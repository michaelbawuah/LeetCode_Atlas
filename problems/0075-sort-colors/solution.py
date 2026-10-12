class Solution:
    def sortColors(self, nums: list[int]) -> None:
        low = scan = 0
        high = len(nums) - 1
        while scan <= high:
            if nums[scan] == 0:
                nums[low], nums[scan] = nums[scan], nums[low]
                low += 1
                scan += 1
            elif nums[scan] == 2:
                nums[scan], nums[high] = nums[high], nums[scan]
                high -= 1
            else:
                scan += 1
