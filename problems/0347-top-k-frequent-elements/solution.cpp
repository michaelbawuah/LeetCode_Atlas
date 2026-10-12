#include <cstddef>
#include <unordered_map>
#include <vector>

using std::vector;

class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        std::unordered_map<int, int> counts;
        counts.reserve(nums.size());
        for (const int value : nums) {
            ++counts[value];
        }
        vector<vector<int>> buckets(nums.size() + 1);
        for (const auto& [value, frequency] : counts) {
            buckets[static_cast<std::size_t>(frequency)].push_back(value);
        }
        vector<int> result;
        result.reserve(static_cast<std::size_t>(k));
        for (std::size_t frequency = nums.size(); frequency > 0; --frequency) {
            for (const int value : buckets[frequency]) {
                result.push_back(value);
                if (result.size() == static_cast<std::size_t>(k)) {
                    return result;
                }
            }
        }
        return result;
    }
};
