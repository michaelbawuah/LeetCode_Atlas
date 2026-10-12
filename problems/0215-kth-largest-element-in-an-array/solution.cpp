#include <algorithm>
#include <cstddef>
#include <functional>
#include <stdexcept>
#include <vector>

using std::vector;

class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        if (k < 1 || static_cast<std::size_t>(k) > nums.size()) {
            throw std::invalid_argument("k must be a valid one-based array position");
        }
        const auto index = static_cast<std::size_t>(k - 1);
        const auto position = nums.begin() + static_cast<vector<int>::difference_type>(index);
        // nth_element gives average linear comparison complexity, not a worst-case guarantee.
        std::nth_element(nums.begin(), position, nums.end(), std::greater<int>{});
        return nums[index];
    }
};
