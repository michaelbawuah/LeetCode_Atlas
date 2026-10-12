#include <cstddef>
#include <queue>
#include <vector>
using std::vector;
class Solution {
  public:
    bool possibleBipartition(int n, vector<vector<int>> &dislikes) {
        vector<vector<int>> adjacent(static_cast<std::size_t>(n) + 1);
        vector<int> colors(static_cast<std::size_t>(n) + 1, 0);
        for (const auto &edge : dislikes) {
            adjacent[edge[0]].push_back(edge[1]);
            adjacent[edge[1]].push_back(edge[0]);
        }
        for (int start = 1; start <= n; ++start) {
            if (colors[start])
                continue;
            colors[start] = 1;
            std::queue<int> pending;
            pending.push(start);
            while (!pending.empty()) {
                int node = pending.front();
                pending.pop();
                for (int neighbor : adjacent[node]) {
                    if (colors[neighbor] == colors[node])
                        return false;
                    if (!colors[neighbor]) {
                        colors[neighbor] = -colors[node];
                        pending.push(neighbor);
                    }
                }
            }
        }
        return true;
    }
};
