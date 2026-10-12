#include <queue>
#include <vector>

class Solution {
public:
    bool isBipartite(std::vector<std::vector<int>>& graph) {
        std::vector<int> colors(graph.size(), 0);
        for (std::size_t start = 0; start < graph.size(); ++start) {
            if (colors[start] != 0) {
                continue;
            }
            colors[start] = 1;
            std::queue<int> pending;
            pending.push(static_cast<int>(start));
            while (!pending.empty()) {
                const int node = pending.front();
                pending.pop();
                for (const int neighbor : graph[node]) {
                    if (colors[neighbor] == colors[node]) {
                        return false;
                    }
                    if (colors[neighbor] == 0) {
                        colors[neighbor] = -colors[node];
                        pending.push(neighbor);
                    }
                }
            }
        }
        return true;
    }
};
