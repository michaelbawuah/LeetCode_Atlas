#include <algorithm>
#include <cstdint>
#include <queue>
#include <vector>

class Solution {
public:
    int minimumTime(int n, std::vector<std::vector<int>>& relations,
                    std::vector<int>& time) {
        std::vector<std::vector<int>> adjacent(n);
        std::vector<int> degree(n, 0);
        for (const auto& edge : relations) {
            adjacent[edge[0] - 1].push_back(edge[1] - 1);
            ++degree[edge[1] - 1];
        }
        std::vector<std::int64_t> completed(time.begin(), time.end());
        std::queue<int> pending;
        for (int node = 0; node < n; ++node) {
            if (degree[node] == 0) {
                pending.push(node);
            }
        }
        while (!pending.empty()) {
            const int node = pending.front();
            pending.pop();
            for (const int neighbor : adjacent[node]) {
                completed[neighbor] = std::max(completed[neighbor], completed[node] + time[neighbor]);
                if (--degree[neighbor] == 0) {
                    pending.push(neighbor);
                }
            }
        }
        // Official n <= 50,000 and time[i] <= 10,000 imply a result <= 500,000,000.
        return static_cast<int>(*std::max_element(completed.begin(), completed.end()));
    }
};
