#include <array>
#include <queue>
#include <utility>
#include <vector>

class Solution {
public:
    int shortestBridge(std::vector<std::vector<int>>& grid) {
        const int n = static_cast<int>(grid.size());
        constexpr std::array<int, 5> delta{-1, 0, 1, 0, -1};
        std::vector<std::vector<bool>> seen(n, std::vector<bool>(n, false));
        std::vector<std::pair<int, int>> pending;
        std::queue<std::pair<int, int>> wave;
        for (int row = 0; row < n && pending.empty(); ++row) {
            for (int col = 0; col < n; ++col) {
                if (grid[row][col] == 1) {
                    seen[row][col] = true;
                    pending.emplace_back(row, col);
                    break;
                }
            }
        }
        while (!pending.empty()) {
            const auto [row, col] = pending.back();
            pending.pop_back();
            wave.emplace(row, col);
            for (int side = 0; side < 4; ++side) {
                const int nr = row + delta[side];
                const int nc = col + delta[side + 1];
                if (0 <= nr && nr < n && 0 <= nc && nc < n && grid[nr][nc] == 1 &&
                    !seen[nr][nc]) {
                    seen[nr][nc] = true;
                    pending.emplace_back(nr, nc);
                }
            }
        }
        int distance = 0;
        while (!wave.empty()) {
            const std::size_t layer_size = wave.size();
            for (std::size_t index = 0; index < layer_size; ++index) {
                const auto [row, col] = wave.front();
                wave.pop();
                for (int side = 0; side < 4; ++side) {
                    const int nr = row + delta[side];
                    const int nc = col + delta[side + 1];
                    if (0 <= nr && nr < n && 0 <= nc && nc < n && !seen[nr][nc]) {
                        if (grid[nr][nc] == 1) {
                            return distance;
                        }
                        seen[nr][nc] = true;
                        wave.emplace(nr, nc);
                    }
                }
            }
            ++distance;
        }
        return -1;
    }
};
