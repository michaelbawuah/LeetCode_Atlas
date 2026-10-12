#include <cstddef>
#include <cstdint>
#include <vector>

class NumMatrix {
    std::vector<std::vector<std::int64_t>> prefix_;

public:
    explicit NumMatrix(std::vector<std::vector<int>>& matrix)
        : prefix_(matrix.size() + 1, std::vector<std::int64_t>(matrix.front().size() + 1, 0)) {
        for (std::size_t row = 0; row < matrix.size(); ++row) {
            for (std::size_t column = 0; column < matrix.front().size(); ++column) {
                prefix_[row + 1][column + 1] = matrix[row][column] + prefix_[row][column + 1]
                    + prefix_[row + 1][column] - prefix_[row][column];
            }
        }
    }
    int sumRegion(int row1, int col1, int row2, int col2) {
        const auto top = static_cast<std::size_t>(row1);
        const auto left = static_cast<std::size_t>(col1);
        const auto bottom = static_cast<std::size_t>(row2) + 1;
        const auto right = static_cast<std::size_t>(col2) + 1;
        return static_cast<int>(prefix_[bottom][right] - prefix_[top][right]
            - prefix_[bottom][left] + prefix_[top][left]);
    }
};
