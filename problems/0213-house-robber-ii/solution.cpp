#include <algorithm>
#include <cstddef>
#include <cstdint>
#include <vector>

using std::vector;

class Solution {
public:
    int rob(vector<int>& nums) {
        if (nums.size() == 1) {
            return nums[0];
        }
        const auto linear_best = [&nums](std::size_t start, std::size_t stop) {
            std::int64_t two_back = 0;
            std::int64_t one_back = 0;
            for (std::size_t index = start; index < stop; ++index) {
                const auto following = std::max(one_back, two_back + nums[index]);
                two_back = one_back;
                one_back = following;
            }
            return one_back;
        };
        return static_cast<int>(std::max(linear_best(0, nums.size() - 1), linear_best(1, nums.size())));
    }
};
