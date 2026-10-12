#include <cstddef>
#include <vector>

class Solution {
public:
    bool searchMatrix(std::vector<std::vector<int>>& matrix, int target) {
        const auto columns = matrix.front().size();
        std::size_t left = 0, end = matrix.size() * columns;
        while (left < end) {
            const auto middle = left + (end - left) / 2;
            const int value = matrix[middle / columns][middle % columns];
            if (value == target) return true;
            if (value < target) left = middle + 1;
            else end = middle;
        }
        return false;
    }
};
