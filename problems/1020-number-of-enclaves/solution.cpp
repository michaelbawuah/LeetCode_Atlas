#include <array>
#include <cstddef>
#include <utility>
#include <vector>
using std::vector;
class Solution {
  public:
    int numEnclaves(vector<vector<int>> &grid) {
        int rows = static_cast<int>(grid.size()), cols = static_cast<int>(grid[0].size());
        vector<vector<unsigned char>> escaped(rows, vector<unsigned char>(cols, 0));
        vector<std::pair<int, int>> pending;
        for (int r = 0; r < rows; ++r)
            for (int c = 0; c < cols; ++c)
                if (grid[r][c] && (r == 0 || r == rows - 1 || c == 0 || c == cols - 1)) {
                    escaped[r][c] = 1;
                    pending.emplace_back(r, c);
                }
        const std::array<std::pair<int, int>, 4> moves{{{-1, 0}, {1, 0}, {0, -1}, {0, 1}}};
        while (!pending.empty()) {
            auto [r, c] = pending.back();
            pending.pop_back();
            for (auto [dr, dc] : moves) {
                int nr = r + dr, nc = c + dc;
                if (nr >= 0 && nr < rows && nc >= 0 && nc < cols && grid[nr][nc] &&
                    !escaped[nr][nc]) {
                    escaped[nr][nc] = 1;
                    pending.emplace_back(nr, nc);
                }
            }
        }
        int count = 0;
        for (int r = 0; r < rows; ++r)
            for (int c = 0; c < cols; ++c)
                if (grid[r][c] && !escaped[r][c])
                    ++count;
        return count;
    }
};
