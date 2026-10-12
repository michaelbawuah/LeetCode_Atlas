#include <vector>

using std::vector;

class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        int top = 0;
        int bottom = static_cast<int>(matrix.size()) - 1;
        int left = 0;
        int right = static_cast<int>(matrix[0].size()) - 1;
        vector<int> result;
        result.reserve(matrix.size() * matrix[0].size());
        while (top <= bottom && left <= right) {
            for (int column = left; column <= right; ++column) {
                result.push_back(matrix[top][column]);
            }
            ++top;
            for (int row = top; row <= bottom; ++row) {
                result.push_back(matrix[row][right]);
            }
            --right;
            if (top <= bottom) {
                for (int column = right; column >= left; --column) {
                    result.push_back(matrix[bottom][column]);
                }
                --bottom;
            }
            if (left <= right) {
                for (int row = bottom; row >= top; --row) {
                    result.push_back(matrix[row][left]);
                }
                ++left;
            }
        }
        return result;
    }
};
