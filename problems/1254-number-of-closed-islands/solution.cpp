#include <array>
#include <utility>
#include <vector>

class Solution {
public:
    int closedIsland(std::vector<std::vector<int>>& grid) {
        const int rows = static_cast<int>(grid.size());
        const int cols = static_cast<int>(grid.front().size());
        constexpr std::array<int, 5> delta{-1, 0, 1, 0, -1};
        std::vector<std::vector<bool>> seen(rows, std::vector<bool>(cols, false));
        std::vector<std::pair<int, int>> pending;
        int closed = 0;
        for (int row = 0; row < rows; ++row) {
            for (int col = 0; col < cols; ++col) {
                if (grid[row][col] != 0 || seen[row][col]) {
                    continue;
                }
                seen[row][col] = true;
                pending.emplace_back(row, col);
                bool touches_border = false;
                while (!pending.empty()) {
                    const auto [r, c] = pending.back();
                    pending.pop_back();
                    touches_border = touches_border || r == 0 || r == rows - 1 ||
                                     c == 0 || c == cols - 1;
                    for (int side = 0; side < 4; ++side) {
                        const int nr = r + delta[side];
                        const int nc = c + delta[side + 1];
                        if (0 <= nr && nr < rows && 0 <= nc && nc < cols &&
                            grid[nr][nc] == 0 && !seen[nr][nc]) {
                            seen[nr][nc] = true;
                            pending.emplace_back(nr, nc);
                        }
                    }
                }
                if (!touches_border) {
                    ++closed;
                }
            }
        }
        return closed;
    }
};
