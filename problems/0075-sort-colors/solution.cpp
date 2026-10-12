#include <algorithm>
#include <cstddef>
#include <vector>

class Solution {
public:
    void sortColors(std::vector<int>& nums) {
        int low = 0;
        int scan = 0;
        int high = static_cast<int>(nums.size()) - 1;
        while (scan <= high) {
            const auto current = static_cast<std::size_t>(scan);
            if (nums[current] == 0) {
                std::swap(nums[static_cast<std::size_t>(low)], nums[current]);
                ++low;
                ++scan;
            } else if (nums[current] == 2) {
                std::swap(nums[current], nums[static_cast<std::size_t>(high)]);
                --high;
            } else {
                ++scan;
            }
        }
    }
};
