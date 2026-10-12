#include <algorithm>
#include <cstddef>
#include <vector>

class Solution {
public:
    void nextPermutation(std::vector<int>& nums) {
        int pivot = static_cast<int>(nums.size()) - 2;
        while (pivot >= 0 && nums[static_cast<std::size_t>(pivot)] >= nums[static_cast<std::size_t>(pivot + 1)]) {
            --pivot;
        }
        if (pivot >= 0) {
            std::size_t successor = nums.size() - 1;
            while (nums[successor] <= nums[static_cast<std::size_t>(pivot)]) {
                --successor;
            }
            std::swap(nums[static_cast<std::size_t>(pivot)], nums[successor]);
        }
        std::reverse(nums.begin() + (pivot + 1), nums.end());
    }
};
