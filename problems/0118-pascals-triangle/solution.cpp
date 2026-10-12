#include <cstddef>
#include <vector>

class Solution {
public:
    std::vector<std::vector<int>> generate(int numRows) {
        std::vector<std::vector<int>> result;
        result.reserve(static_cast<std::size_t>(numRows));
        for (std::size_t length = 1; length <= static_cast<std::size_t>(numRows); ++length) {
            result.emplace_back(length, 1);
            for (std::size_t column = 1; column + 1 < length; ++column) {
                result.back()[column] = result[length - 2][column - 1] + result[length - 2][column];
            }
        }
        return result;
    }
};
