class Solution:
    def jump(self, nums: list[int]) -> int:
        jumps = 0
        layer_end = furthest = 0
        for index in range(len(nums) - 1):
            furthest = max(furthest, index + nums[index])
            if index == layer_end:
                jumps += 1
                layer_end = furthest
        return jumps
