#include <array>
#include <queue>
#include <utility>
#include <vector>

class Solution {
public:
    int longestIncreasingPath(std::vector<std::vector<int>>& matrix) {
        const int rows = static_cast<int>(matrix.size());
        const int cols = static_cast<int>(matrix.front().size());
        constexpr std::array<int, 5> delta{-1, 0, 1, 0, -1};
        std::vector<std::vector<int>> degree(rows, std::vector<int>(cols, 0));
        std::queue<std::pair<int, int>> pending;
        for (int row = 0; row < rows; ++row) {
            for (int col = 0; col < cols; ++col) {
                for (int side = 0; side < 4; ++side) {
                    const int nr = row + delta[side];
                    const int nc = col + delta[side + 1];
                    if (0 <= nr && nr < rows && 0 <= nc && nc < cols &&
                        matrix[nr][nc] > matrix[row][col]) {
                        ++degree[row][col];
                    }
                }
                if (degree[row][col] == 0) {
                    pending.emplace(row, col);
                }
            }
        }
        int length = 0;
        while (!pending.empty()) {
            ++length;
            const std::size_t layer_size = pending.size();
            for (std::size_t index = 0; index < layer_size; ++index) {
                const auto [row, col] = pending.front();
                pending.pop();
                for (int side = 0; side < 4; ++side) {
                    const int nr = row + delta[side];
                    const int nc = col + delta[side + 1];
                    if (0 <= nr && nr < rows && 0 <= nc && nc < cols &&
                        matrix[nr][nc] < matrix[row][col] && --degree[nr][nc] == 0) {
                        pending.emplace(nr, nc);
                    }
                }
            }
        }
        return length;
    }
};
