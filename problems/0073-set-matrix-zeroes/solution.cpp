#include <algorithm>
#include <vector>

using std::vector;

class Solution {
public:
    void setZeroes(vector<vector<int>>& matrix) {
        const int rows = static_cast<int>(matrix.size());
        const int columns = static_cast<int>(matrix[0].size());
        const bool first_row_zero = std::any_of(matrix[0].begin(), matrix[0].end(), [](int value) { return value == 0; });
        bool first_column_zero = false;
        for (const auto& row : matrix) {
            first_column_zero = first_column_zero || row[0] == 0;
        }
        for (int row = 1; row < rows; ++row) {
            for (int column = 1; column < columns; ++column) {
                if (matrix[row][column] == 0) {
                    matrix[row][0] = matrix[0][column] = 0;
                }
            }
        }
        for (int row = 1; row < rows; ++row) {
            for (int column = 1; column < columns; ++column) {
                if (matrix[row][0] == 0 || matrix[0][column] == 0) {
                    matrix[row][column] = 0;
                }
            }
        }
        if (first_row_zero) {
            std::fill(matrix[0].begin(), matrix[0].end(), 0);
        }
        if (first_column_zero) {
            for (auto& row : matrix) {
                row[0] = 0;
            }
        }
    }
};
