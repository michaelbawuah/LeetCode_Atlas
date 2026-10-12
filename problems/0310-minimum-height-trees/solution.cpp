#include <cstddef>
#include <queue>
#include <vector>
using std::vector;
class Solution {
  public:
    vector<int> findMinHeightTrees(int n, vector<vector<int>> &edges) {
        if (n <= 2) {
            vector<int> result;
            for (int i = 0; i < n; ++i)
                result.push_back(i);
            return result;
        }
        vector<vector<int>> adjacent(static_cast<std::size_t>(n));
        for (const auto &edge : edges) {
            adjacent[edge[0]].push_back(edge[1]);
            adjacent[edge[1]].push_back(edge[0]);
        }
        vector<int> degree(static_cast<std::size_t>(n));
        std::queue<int> leaves;
        for (int i = 0; i < n; ++i) {
            degree[i] = static_cast<int>(adjacent[i].size());
            if (degree[i] == 1)
                leaves.push(i);
        }
        int remaining = n;
        while (remaining > 2) {
            const auto width = leaves.size();
            remaining -= static_cast<int>(width);
            for (std::size_t i = 0; i < width; ++i) {
                int node = leaves.front();
                leaves.pop();
                for (int neighbor : adjacent[node])
                    if (--degree[neighbor] == 1)
                        leaves.push(neighbor);
            }
        }
        vector<int> result;
        while (!leaves.empty()) {
            result.push_back(leaves.front());
            leaves.pop();
        }
        return result;
    }
};
