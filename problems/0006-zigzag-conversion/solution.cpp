#include <cstddef>
#include <string>
#include <vector>

class Solution {
public:
    std::string convert(std::string s, int numRows) {
        if (numRows == 1 || static_cast<std::size_t>(numRows) >= s.size()) return s;
        std::vector<std::string> rows(static_cast<std::size_t>(numRows));
        int row = 0;
        int direction = 1;
        for (char letter : s) {
            rows[static_cast<std::size_t>(row)].push_back(letter);
            if (row == 0) direction = 1;
            else if (row == numRows - 1) direction = -1;
            row += direction;
        }
        std::string result;
        result.reserve(s.size());
        for (const auto& values : rows) result += values;
        return result;
    }
};
