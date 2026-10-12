class Solution:
    def rob(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def linear_best(start: int, stop: int) -> int:
            two_back, one_back = 0, 0
            for index in range(start, stop):
                two_back, one_back = one_back, max(one_back, two_back + nums[index])
            return one_back

        return max(linear_best(0, len(nums) - 1), linear_best(1, len(nums)))
