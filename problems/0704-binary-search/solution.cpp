#include <cstddef>
#include <vector>

class Solution {
public:
    int search(std::vector<int>& nums, int target) {
        int left = 0, right = static_cast<int>(nums.size()) - 1;
        while (left <= right) {
            const int middle = left + (right - left) / 2;
            const int value = nums[static_cast<std::size_t>(middle)];
            if (value == target) return middle;
            if (value < target) left = middle + 1;
            else right = middle - 1;
        }
        return -1;
    }
};
