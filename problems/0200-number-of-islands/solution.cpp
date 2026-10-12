#include <array>
#include <utility>
#include <vector>

class Solution {
public:
    int numIslands(std::vector<std::vector<char>>& grid) {
        const int rows = static_cast<int>(grid.size());
        const int cols = static_cast<int>(grid.front().size());
        constexpr std::array<int, 5> delta{-1, 0, 1, 0, -1};
        std::vector<std::pair<int, int>> pending;
        int islands = 0;
        for (int row = 0; row < rows; ++row) {
            for (int col = 0; col < cols; ++col) {
                if (grid[row][col] != '1') {
                    continue;
                }
                ++islands;
                grid[row][col] = '0';
                pending.emplace_back(row, col);
                while (!pending.empty()) {
                    const auto [r, c] = pending.back();
                    pending.pop_back();
                    for (int side = 0; side < 4; ++side) {
                        const int nr = r + delta[side];
                        const int nc = c + delta[side + 1];
                        if (0 <= nr && nr < rows && 0 <= nc && nc < cols &&
                            grid[nr][nc] == '1') {
                            grid[nr][nc] = '0';
                            pending.emplace_back(nr, nc);
                        }
                    }
                }
            }
        }
        return islands;
    }
};
