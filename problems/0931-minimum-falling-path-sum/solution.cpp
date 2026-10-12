#include <algorithm>
#include <cstddef>
#include <vector>
using std::vector;
class Solution {
public:
    int minFallingPathSum(vector<vector<int>>& matrix) {
        vector<int> previous = matrix.front();
        for (std::size_t row = 1; row < matrix.size(); ++row) {
            vector<int> current(previous.size());
            for (std::size_t column = 0; column < previous.size(); ++column) {
                int predecessor = previous[column];
                if (column > 0) {
                    predecessor = std::min(predecessor, previous[column - 1]);
                }
                if (column + 1 < previous.size()) {
                    predecessor = std::min(predecessor, previous[column + 1]);
                }
                current[column] = matrix[row][column] + predecessor;
            }
            previous.swap(current);
        }
        return *std::min_element(previous.begin(), previous.end());
    }
};
