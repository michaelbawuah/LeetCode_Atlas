#include <algorithm>
#include <cstddef>
#include <vector>

using std::vector;

class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        if (nums.empty()) {
            return 0;
        }
        long long ending_here = nums.front();
        long long best = ending_here;
        for (std::size_t index = 1; index < nums.size(); ++index) {
            ending_here = std::max(static_cast<long long>(nums[index]), ending_here + nums[index]);
            best = std::max(best, ending_here);
        }
        return static_cast<int>(best);
    }
};
