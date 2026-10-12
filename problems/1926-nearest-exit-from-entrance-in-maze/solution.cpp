#include <array>
#include <cstddef>
#include <queue>
#include <utility>
#include <vector>
using std::vector;
class Solution {
  public:
    int nearestExit(vector<vector<char>> &maze, vector<int> &entrance) {
        int rows = static_cast<int>(maze.size()), cols = static_cast<int>(maze[0].size());
        vector<vector<unsigned char>> seen(rows, vector<unsigned char>(cols, 0));
        seen[entrance[0]][entrance[1]] = 1;
        std::queue<std::array<int, 3>> pending;
        pending.push({entrance[0], entrance[1], 0});
        const std::array<std::pair<int, int>, 4> moves{{{-1, 0}, {1, 0}, {0, -1}, {0, 1}}};
        while (!pending.empty()) {
            auto [r, c, distance] = pending.front();
            pending.pop();
            for (auto [dr, dc] : moves) {
                int nr = r + dr, nc = c + dc;
                if (nr >= 0 && nr < rows && nc >= 0 && nc < cols && maze[nr][nc] == '.' &&
                    !seen[nr][nc]) {
                    if (nr == 0 || nr == rows - 1 || nc == 0 || nc == cols - 1)
                        return distance + 1;
                    seen[nr][nc] = 1;
                    pending.push({nr, nc, distance + 1});
                }
            }
        }
        return -1;
    }
};
