#include <algorithm>
#include <cstddef>
#include <utility>
#include <vector>

class Solution {
    struct Frame {
        int node;
        int parent_edge;
        std::size_t offset;
    };

public:
    std::vector<std::vector<int>> criticalConnections(
        int n, std::vector<std::vector<int>>& connections) {
        std::vector<std::vector<std::pair<int, int>>> adjacent(n);
        for (std::size_t index = 0; index < connections.size(); ++index) {
            const auto& edge = connections[index];
            adjacent[edge[0]].emplace_back(edge[1], static_cast<int>(index));
            adjacent[edge[1]].emplace_back(edge[0], static_cast<int>(index));
        }
        std::vector<int> discovery(n, -1);
        std::vector<int> low(n, 0);
        std::vector<Frame> stack;
        stack.reserve(n);
        std::vector<std::vector<int>> bridges;
        int timer = 0;
        for (int start = 0; start < n; ++start) {
            if (discovery[start] != -1) {
                continue;
            }
            discovery[start] = low[start] = timer++;
            stack.push_back({start, -1, 0});
            while (!stack.empty()) {
                const int node = stack.back().node;
                const int parent_edge = stack.back().parent_edge;
                if (stack.back().offset < adjacent[node].size()) {
                    const auto [neighbor, edge] = adjacent[node][stack.back().offset++];
                    if (edge == parent_edge) {
                        continue;
                    }
                    if (discovery[neighbor] == -1) {
                        discovery[neighbor] = low[neighbor] = timer++;
                        stack.push_back({neighbor, edge, 0});
                    } else {
                        low[node] = std::min(low[node], discovery[neighbor]);
                    }
                } else {
                    stack.pop_back();
                    if (parent_edge != -1) {
                        const auto& edge = connections[parent_edge];
                        const int parent = edge[0] == node ? edge[1] : edge[0];
                        if (low[node] > discovery[parent]) {
                            bridges.push_back({parent, node});
                        }
                        low[parent] = std::min(low[parent], low[node]);
                    }
                }
            }
        }
        return bridges;
    }
};
