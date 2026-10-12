#include <algorithm>
#include <array>
#include <queue>
#include <utility>
#include <vector>

class Solution {
public:
    int maxDistance(std::vector<std::vector<int>>& grid) {
        const int n = static_cast<int>(grid.size());
        constexpr std::array<int, 5> delta{-1, 0, 1, 0, -1};
        std::vector<std::vector<int>> distances(n, std::vector<int>(n, -1));
        std::queue<std::pair<int, int>> pending;
        for (int row = 0; row < n; ++row) {
            for (int col = 0; col < n; ++col) {
                if (grid[row][col] == 1) {
                    distances[row][col] = 0;
                    pending.emplace(row, col);
                }
            }
        }
        if (pending.empty() || pending.size() == grid.size() * grid.size()) {
            return -1;
        }
        int farthest = 0;
        while (!pending.empty()) {
            const auto [row, col] = pending.front();
            pending.pop();
            for (int side = 0; side < 4; ++side) {
                const int nr = row + delta[side];
                const int nc = col + delta[side + 1];
                if (0 <= nr && nr < n && 0 <= nc && nc < n && distances[nr][nc] == -1) {
                    distances[nr][nc] = distances[row][col] + 1;
                    farthest = std::max(farthest, distances[nr][nc]);
                    pending.emplace(nr, nc);
                }
            }
        }
        return farthest;
    }
};
