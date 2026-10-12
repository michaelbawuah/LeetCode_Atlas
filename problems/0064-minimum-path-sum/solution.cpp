#include <algorithm>
#include <cstddef>
#include <cstdint>
#include <limits>
#include <vector>
using std::vector;
class Solution {
public:
    int minPathSum(vector<vector<int>>& grid) {
        vector<std::int64_t> best(grid.front().size(), std::numeric_limits<std::int64_t>::max() / 4);
        best[0] = 0;
        for (const auto& row : grid) {
            for (std::size_t column = 0; column < row.size(); ++column) {
                best[column] = (column == 0 ? best[column] : std::min(best[column], best[column - 1])) + row[column];
            }
        }
        return static_cast<int>(best.back());
    }
};
