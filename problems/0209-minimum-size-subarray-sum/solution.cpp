#include <algorithm>
#include <cstdint>
#include <vector>

using std::vector;

class Solution {
public:
    int minSubArrayLen(int target, vector<int>& nums) {
        const int size = static_cast<int>(nums.size());
        int left = 0;
        int best = size + 1;
        std::int64_t total = 0;
        for (int right = 0; right < size; ++right) {
            total += nums[right];
            while (total >= target) {
                best = std::min(best, right - left + 1);
                total -= nums[left++];
            }
        }
        return best > size ? 0 : best;
    }
};
