#include <algorithm>
#include <cstddef>
#include <queue>
#include <utility>
#include <vector>
using std::vector;
class Solution {
  public:
    int snakesAndLadders(vector<vector<int>> &board) {
        int n = static_cast<int>(board.size()), finish = n * n;
        vector<unsigned char> seen(static_cast<std::size_t>(finish) + 1, 0);
        seen[1] = 1;
        std::queue<std::pair<int, int>> pending;
        pending.emplace(1, 0);
        while (!pending.empty()) {
            auto [node, rolls] = pending.front();
            pending.pop();
            if (node == finish)
                return rolls;
            for (int next = node + 1; next <= std::min(finish, node + 6); ++next) {
                int below = (next - 1) / n, col = (next - 1) % n;
                if (below % 2)
                    col = n - 1 - col;
                int value = board[n - 1 - below][col];
                int destination = value == -1 ? next : value;
                if (!seen[destination]) {
                    seen[destination] = 1;
                    pending.emplace(destination, rolls + 1);
                }
            }
        }
        return -1;
    }
};
