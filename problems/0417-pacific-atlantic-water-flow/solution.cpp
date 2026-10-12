#include <array>
#include <utility>
#include <vector>

class Solution {
public:
    std::vector<std::vector<int>> pacificAtlantic(std::vector<std::vector<int>>& heights) {
        const int rows = static_cast<int>(heights.size());
        const int cols = static_cast<int>(heights.front().size());
        constexpr std::array<int, 5> delta{-1, 0, 1, 0, -1};
        const auto reachable = [&](bool pacific) {
            std::vector<std::vector<bool>> seen(rows, std::vector<bool>(cols, false));
            std::vector<std::pair<int, int>> pending;
            const auto add = [&](int row, int col) {
                if (!seen[row][col]) {
                    seen[row][col] = true;
                    pending.emplace_back(row, col);
                }
            };
            for (int row = 0; row < rows; ++row) {
                add(row, pacific ? 0 : cols - 1);
            }
            for (int col = 0; col < cols; ++col) {
                add(pacific ? 0 : rows - 1, col);
            }
            while (!pending.empty()) {
                const auto [row, col] = pending.back();
                pending.pop_back();
                for (int side = 0; side < 4; ++side) {
                    const int nr = row + delta[side];
                    const int nc = col + delta[side + 1];
                    if (0 <= nr && nr < rows && 0 <= nc && nc < cols &&
                        heights[nr][nc] >= heights[row][col]) {
                        add(nr, nc);
                    }
                }
            }
            return seen;
        };
        const auto pacific = reachable(true);
        const auto atlantic = reachable(false);
        std::vector<std::vector<int>> result;
        for (int row = 0; row < rows; ++row) {
            for (int col = 0; col < cols; ++col) {
                if (pacific[row][col] && atlantic[row][col]) {
                    result.push_back({row, col});
                }
            }
        }
        return result;
    }
};
