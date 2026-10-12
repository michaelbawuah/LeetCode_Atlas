#include <array>
#include <utility>
#include <vector>

class Solution {
public:
    void solve(std::vector<std::vector<char>>& board) {
        const int rows = static_cast<int>(board.size());
        const int cols = static_cast<int>(board.front().size());
        std::vector<std::pair<int, int>> pending;
        const auto protect = [&](int row, int col) {
            if (board[row][col] == 'O') {
                board[row][col] = '#';
                pending.emplace_back(row, col);
            }
        };
        for (int row = 0; row < rows; ++row) {
            protect(row, 0);
            protect(row, cols - 1);
        }
        for (int col = 0; col < cols; ++col) {
            protect(0, col);
            protect(rows - 1, col);
        }
        constexpr std::array<int, 5> delta{-1, 0, 1, 0, -1};
        while (!pending.empty()) {
            const auto [row, col] = pending.back();
            pending.pop_back();
            for (int side = 0; side < 4; ++side) {
                const int nr = row + delta[side];
                const int nc = col + delta[side + 1];
                if (0 <= nr && nr < rows && 0 <= nc && nc < cols) {
                    protect(nr, nc);
                }
            }
        }
        for (auto& row : board) {
            for (char& cell : row) {
                if (cell == '#') {
                    cell = 'O';
                } else if (cell == 'O') {
                    cell = 'X';
                }
            }
        }
    }
};
