class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        slow = fast = nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        entry = nums[0]
        while entry != slow:
            entry = nums[entry]
            slow = nums[slow]
        return entry
