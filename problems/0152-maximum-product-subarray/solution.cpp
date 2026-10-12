#include <algorithm>
#include <array>
#include <cstddef>
#include <vector>

using std::vector;

class Solution {
public:
    int maxProduct(vector<int>& nums) {
        long long low = nums.front();
        long long high = low;
        long long best = high;
        for (std::size_t index = 1; index < nums.size(); ++index) {
            const long long value = nums[index];
            const std::array<long long, 3> candidates = {value, value * low, value * high};
            const auto [smallest, largest] = std::minmax_element(candidates.begin(), candidates.end());
            low = *smallest;
            high = *largest;
            best = std::max(best, high);
        }
        return static_cast<int>(best);
    }
};
