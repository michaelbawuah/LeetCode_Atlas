#include <algorithm>
#include <array>
#include <cstdlib>
#include <functional>
#include <limits>
#include <queue>
#include <tuple>
#include <utility>
#include <vector>
using std::vector;
class Solution {
  public:
    int minimumEffortPath(vector<vector<int>> &heights) {
        int rows = static_cast<int>(heights.size()), cols = static_cast<int>(heights[0].size());
        vector<vector<int>> effort(rows, vector<int>(cols, std::numeric_limits<int>::max()));
        effort[0][0] = 0;
        using Entry = std::tuple<int, int, int>;
        std::priority_queue<Entry, vector<Entry>, std::greater<Entry>> pending;
        pending.emplace(0, 0, 0);
        const std::array<std::pair<int, int>, 4> moves{{{-1, 0}, {1, 0}, {0, -1}, {0, 1}}};
        while (!pending.empty()) {
            auto [cost, r, c] = pending.top();
            pending.pop();
            if (cost != effort[r][c])
                continue;
            if (r == rows - 1 && c == cols - 1)
                return cost;
            for (auto [dr, dc] : moves) {
                int nr = r + dr, nc = c + dc;
                if (nr >= 0 && nr < rows && nc >= 0 && nc < cols) {
                    int next = std::max(cost, std::abs(heights[r][c] - heights[nr][nc]));
                    if (next < effort[nr][nc]) {
                        effort[nr][nc] = next;
                        pending.emplace(next, nr, nc);
                    }
                }
            }
        }
        return 0;
    }
};
