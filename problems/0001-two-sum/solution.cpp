#include <cstddef>
#include <unordered_map>
#include <vector>

using std::vector;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        // Widen the subtraction before computing the complement.
        std::unordered_map<long long, int> seen;
        seen.reserve(nums.size());
        for (std::size_t index = 0; index < nums.size(); ++index) {
            const long long value = nums[index];
            const auto match = seen.find(static_cast<long long>(target) - value);
            if (match != seen.end()) {
                return {match->second, static_cast<int>(index)};
            }
            seen.emplace(value, static_cast<int>(index));
        }
        return {};
    }
};
