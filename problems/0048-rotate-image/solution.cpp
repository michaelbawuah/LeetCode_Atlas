#include <algorithm>
#include <vector>

using std::vector;

class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {
        const int size = static_cast<int>(matrix.size());
        for (int row = 0; row < size; ++row) {
            for (int column = row + 1; column < size; ++column) {
                std::swap(matrix[row][column], matrix[column][row]);
            }
        }
        for (auto& row : matrix) {
            std::reverse(row.begin(), row.end());
        }
    }
};
