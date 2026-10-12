#include <array>
#include <cstddef>
#include <queue>
#include <utility>
#include <vector>
using std::vector;
class Solution {
  public:
    vector<vector<int>> updateMatrix(vector<vector<int>> &mat) {
        int rows = static_cast<int>(mat.size()), cols = static_cast<int>(mat[0].size());
        vector<vector<int>> distance(rows, vector<int>(cols, -1));
        std::queue<std::pair<int, int>> pending;
        for (int r = 0; r < rows; ++r)
            for (int c = 0; c < cols; ++c)
                if (mat[r][c] == 0) {
                    distance[r][c] = 0;
                    pending.emplace(r, c);
                }
        const std::array<std::pair<int, int>, 4> moves{{{-1, 0}, {1, 0}, {0, -1}, {0, 1}}};
        while (!pending.empty()) {
            auto [r, c] = pending.front();
            pending.pop();
            for (auto [dr, dc] : moves) {
                int nr = r + dr, nc = c + dc;
                if (nr >= 0 && nr < rows && nc >= 0 && nc < cols && distance[nr][nc] == -1) {
                    distance[nr][nc] = distance[r][c] + 1;
                    pending.emplace(nr, nc);
                }
            }
        }
        return distance;
    }
};
