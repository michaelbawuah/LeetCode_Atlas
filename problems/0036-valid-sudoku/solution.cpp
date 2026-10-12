#include <array>
#include <vector>

using std::vector;

class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        std::array<std::array<bool, 9>, 9> rows{};
        std::array<std::array<bool, 9>, 9> columns{};
        std::array<std::array<bool, 9>, 9> boxes{};
        for (int row = 0; row < 9; ++row) {
            for (int column = 0; column < 9; ++column) {
                const char value = board[row][column];
                if (value == '.') {
                    continue;
                }
                const int digit = value - '1';
                const int box = (row / 3) * 3 + column / 3;
                if (rows[row][digit] || columns[column][digit] || boxes[box][digit]) {
                    return false;
                }
                rows[row][digit] = columns[column][digit] = boxes[box][digit] = true;
            }
        }
        return true;
    }
};
