#include <algorithm>
#include <cstddef>
#include <cstdint>
#include <vector>

class Solution {
public:
    int uniquePaths(int m, int n) {
        const int width = std::min(m, n);
        const int height = std::max(m, n);
        std::vector<std::int64_t> counts(static_cast<std::size_t>(width), 1);
        for (int row = 1; row < height; ++row) {
            for (int column = 1; column < width; ++column) {
                const auto index = static_cast<std::size_t>(column);
                counts[index] += counts[index - 1];
            }
        }
        // Every partial-cell count is at most the guaranteed-bounded final count.
        return static_cast<int>(counts.back());
    }
};
