#include <algorithm>
#include <cstddef>
#include <vector>

using std::vector;

class Solution {
public:
    bool canJump(vector<int>& nums) {
        std::size_t furthest = 0;
        for (std::size_t index = 0; index < nums.size(); ++index) {
            if (index > furthest) {
                return false;
            }
            furthest = std::max(furthest, index + static_cast<std::size_t>(nums[index]));
            if (furthest >= nums.size() - 1) {
                return true;
            }
        }
        return true;
    }
};
