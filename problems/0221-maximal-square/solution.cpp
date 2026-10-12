#include <algorithm>
#include <cstddef>
#include <vector>
using std::vector;
class Solution {
public:
    int maximalSquare(vector<vector<char>>& matrix) {
        vector<int> sides(matrix.front().size() + 1, 0);
        int largest = 0;
        for (const auto& row : matrix) {
            int diagonal = 0;
            for (std::size_t column = 1; column <= row.size(); ++column) {
                const int above = sides[column];
                if (row[column - 1] == '1') {
                    sides[column] = 1 + std::min({sides[column], sides[column - 1], diagonal});
                    largest = std::max(largest, sides[column]);
                } else {
                    sides[column] = 0;
                }
                diagonal = above;
            }
        }
        return largest * largest;
    }
};
