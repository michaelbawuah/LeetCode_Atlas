#include <cstddef>
#include <vector>

using std::vector;

class Solution {
public:
    int search(vector<int>& nums, int target) {
        // [left, end) avoids an unsigned -1 when the input is empty.
        std::size_t left = 0;
        std::size_t end = nums.size();
        while (left < end) {
            const std::size_t middle = left + (end - left) / 2;
            if (nums[middle] == target) {
                return static_cast<int>(middle);
            }
            if (nums[left] <= nums[middle]) {
                if (nums[left] <= target && target < nums[middle]) {
                    end = middle;
                } else {
                    left = middle + 1;
                }
            } else {
                if (nums[middle] < target && target <= nums[end - 1]) {
                    left = middle + 1;
                } else {
                    end = middle;
                }
            }
        }
        return -1;
    }
};
