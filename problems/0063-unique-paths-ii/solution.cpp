#include <algorithm>
#include <cstddef>
#include <cstdint>
#include <vector>
using std::vector;
class Solution {
public:
    int uniquePathsWithObstacles(vector<vector<int>>& obstacleGrid) {
        const std::int64_t cap = 2'000'000'000LL;
        vector<std::int64_t> paths(obstacleGrid.front().size(), 0);
        paths[0] = 1;
        for (const auto& row : obstacleGrid) {
            for (std::size_t column = 0; column < row.size(); ++column) {
                if (row[column] != 0) {
                    paths[column] = 0;
                } else if (column != 0) {
                    // Both operands are 64-bit and capped before this addition.
                    paths[column] = std::min(cap, paths[column] + paths[column - 1]);
                }
            }
        }
        // Nonnegative addition and obstacle resets commute with saturation.
        // The final answer is guaranteed <= cap, so its saturated value is exact.
        return static_cast<int>(paths.back());
    }
};
