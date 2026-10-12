class Solution:
    def trap(self, height: list[int]) -> int:
        left, right = 0, len(height) - 1
        left_peak = right_peak = water = 0
        while left < right:
            if height[left] <= height[right]:
                left_peak = max(left_peak, height[left])
                water += left_peak - height[left]
                left += 1
            else:
                right_peak = max(right_peak, height[right])
                water += right_peak - height[right]
                right -= 1
        return water
