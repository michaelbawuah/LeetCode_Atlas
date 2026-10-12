#include <algorithm>
#include <cstddef>
#include <numeric>
#include <vector>

using std::vector;

class Solution {
public:
    vector<int> findRedundantConnection(vector<vector<int>>& edges) {
        int largest_label = 0;
        for (const auto& edge : edges) {
            largest_label = std::max(largest_label, std::max(edge[0], edge[1]));
        }
        const auto count = static_cast<std::size_t>(largest_label) + 1;
        vector<int> parent(count);
        vector<int> size(count, 1);
        std::iota(parent.begin(), parent.end(), 0);
        for (const auto& edge : edges) {
            int first = find_root(parent, edge[0]);
            int second = find_root(parent, edge[1]);
            if (first == second) {
                return edge;
            }
            if (size[static_cast<std::size_t>(first)] < size[static_cast<std::size_t>(second)]) {
                std::swap(first, second);
            }
            parent[static_cast<std::size_t>(second)] = first;
            size[static_cast<std::size_t>(first)] += size[static_cast<std::size_t>(second)];
        }
        return {};
    }

private:
    static int find_root(vector<int>& parent, int node) {
        while (parent[static_cast<std::size_t>(node)] != node) {
            const int ancestor = parent[static_cast<std::size_t>(node)];
            parent[static_cast<std::size_t>(node)] = parent[static_cast<std::size_t>(ancestor)];
            node = parent[static_cast<std::size_t>(node)];
        }
        return node;
    }
};
