#include <algorithm>
#include <cstddef>
#include <cstdint>
#include <vector>
using std::vector;
class Solution {
public:
    int minimumTotal(vector<vector<int>>& triangle) {
        vector<std::int64_t> best(triangle.back().begin(), triangle.back().end());
        for (std::size_t remaining = triangle.size() - 1; remaining > 0; --remaining) {
            const auto& row = triangle[remaining - 1];
            for (std::size_t column = 0; column < row.size(); ++column) {
                best[column] = row[column] + std::min(best[column], best[column + 1]);
            }
        }
        return static_cast<int>(best.front());
    }
};
