#include <cstddef>
#include <vector>

class Solution {
public:
    std::vector<int> getRow(int rowIndex) {
        std::vector<int> result;
        result.reserve(static_cast<std::size_t>(rowIndex) + 1);
        long long coefficient = 1;
        result.push_back(1);
        for (int column = 1; column <= rowIndex; ++column) {
            coefficient = coefficient * (rowIndex - column + 1) / column;
            result.push_back(static_cast<int>(coefficient));
        }
        return result;
    }
};
