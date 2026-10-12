#include <algorithm>
#include <cstddef>
#include <cstdint>
#include <limits>
#include <vector>

class Solution {
public:
    int findNumberOfLIS(std::vector<int>& nums) {
        constexpr std::int64_t cap = std::numeric_limits<int>::max();
        std::vector<int> lengths(nums.size(), 1);
        std::vector<int> counts(nums.size(), 1);
        for (std::size_t end = 0; end < nums.size(); ++end) {
            for (std::size_t previous = 0; previous < end; ++previous) {
                if (nums[previous] < nums[end]) {
                    const int candidate = lengths[previous] + 1;
                    if (candidate > lengths[end]) {
                        lengths[end] = candidate;
                        counts[end] = counts[previous];
                    } else if (candidate == lengths[end]) {
                        const std::int64_t sum =
                            static_cast<std::int64_t>(counts[end]) + counts[previous];
                        counts[end] = static_cast<int>(std::min(sum, cap));
                    }
                }
            }
        }
        const int longest = *std::max_element(lengths.begin(), lengths.end());
        int answer = 0;
        for (std::size_t index = 0; index < nums.size(); ++index) {
            if (lengths[index] == longest) {
                const std::int64_t sum = static_cast<std::int64_t>(answer) + counts[index];
                answer = static_cast<int>(std::min(sum, cap));
            }
        }
        return answer;
    }
};
