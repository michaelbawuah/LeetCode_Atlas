#include <cstddef>
#include <vector>

class Solution {
public:
    bool searchMatrix(std::vector<std::vector<int>>& matrix, int target) {
        std::size_t row = 0;
        int column = static_cast<int>(matrix.front().size()) - 1;
        while (row < matrix.size() && column >= 0) {
            const int value = matrix[row][static_cast<std::size_t>(column)];
            if (value == target) {
                return true;
            }
            if (value > target) {
                --column;
            } else {
                ++row;
            }
        }
        return false;
    }
};
