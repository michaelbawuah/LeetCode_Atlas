#include <algorithm>
#include <cstddef>
#include <cstdint>
#include <limits>
#include <vector>

class Solution {
public:
    int combinationSum4(std::vector<int>& nums, int target) {
        constexpr std::int64_t cap = std::numeric_limits<int>::max();
        std::vector<int> counts(static_cast<std::size_t>(target) + 1, 0);
        counts[0] = 1;
        for (int total = 1; total <= target; ++total) {
            int count = 0;
            for (int value : nums) {
                if (value <= total) {
                    const std::int64_t sum =
                        static_cast<std::int64_t>(count) + counts[static_cast<std::size_t>(total - value)];
                    count = static_cast<int>(std::min(sum, cap));
                }
            }
            counts[static_cast<std::size_t>(total)] = count;
        }
        return counts.back();
    }
};
