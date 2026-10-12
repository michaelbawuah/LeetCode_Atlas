#include <cstddef>
#include <vector>

using std::vector;

class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        vector<int> result(nums.size(), 1);
        long long prefix = 1;
        for (std::size_t index = 0; index < nums.size(); ++index) {
            result[index] = static_cast<int>(prefix);
            // The problem guarantees prefix, suffix and answer products fit int.
            if (index + 1 < nums.size()) {
                prefix *= nums[index];
            }
        }
        long long suffix = 1;
        for (std::size_t end = nums.size(); end > 0; --end) {
            const std::size_t index = end - 1;
            result[index] = static_cast<int>(static_cast<long long>(result[index]) * suffix);
            if (index > 0) {
                suffix *= nums[index];
            }
        }
        return result;
    }
};
