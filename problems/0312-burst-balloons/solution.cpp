#include <algorithm>
#include <cstddef>
#include <cstdint>
#include <vector>

class Solution {
public:
    int maxCoins(std::vector<int>& nums) {
        const std::size_t size = nums.size();
        std::vector<int> values;
        values.reserve(size + 2);
        values.push_back(1);
        values.insert(values.end(), nums.begin(), nums.end());
        values.push_back(1);
        std::vector<std::vector<std::int64_t>> best(
            size + 2, std::vector<std::int64_t>(size + 2, 0));
        for (std::size_t length = 1; length <= size; ++length) {
            for (std::size_t left = 1; left + length - 1 <= size; ++left) {
                const std::size_t right = left + length - 1;
                for (std::size_t last = left; last <= right; ++last) {
                    const std::int64_t product =
                        static_cast<std::int64_t>(values[left - 1]) * values[last] * values[right + 1];
                    best[left][right] = std::max(
                        best[left][right], best[left][last - 1] + product + best[last + 1][right]);
                }
            }
        }
        return static_cast<int>(best[1][size]);
    }
};
