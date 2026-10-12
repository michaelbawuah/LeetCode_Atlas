#include <algorithm>
#include <cstdint>
#include <unordered_map>
#include <utility>
#include <vector>
using std::vector;
class Solution {
public:
    int deleteAndEarn(vector<int>& nums) {
        std::unordered_map<int, int> frequencies;
        for (const int value : nums) {
            ++frequencies[value];
        }
        vector<std::pair<int, int>> ordered(frequencies.begin(), frequencies.end());
        std::sort(ordered.begin(), ordered.end());
        std::int64_t two_back = 0;
        std::int64_t one_back = 0;
        int previous = -1;
        for (const auto& [value, count] : ordered) {
            const std::int64_t earned = static_cast<std::int64_t>(value) * count;
            const auto following = value == previous + 1 ? std::max(one_back, two_back + earned) : one_back + earned;
            two_back = one_back;
            one_back = following;
            previous = value;
        }
        return static_cast<int>(one_back);
    }
};
