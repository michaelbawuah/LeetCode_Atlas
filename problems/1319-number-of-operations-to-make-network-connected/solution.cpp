#include <cstddef>
#include <numeric>
#include <utility>
#include <vector>
using std::vector;
class Solution {
  public:
    int makeConnected(int n, vector<vector<int>> &connections) {
        if (connections.size() < static_cast<std::size_t>(n - 1))
            return -1;
        vector<int> parent(static_cast<std::size_t>(n)), size(static_cast<std::size_t>(n), 1);
        std::iota(parent.begin(), parent.end(), 0);
        int components = n;
        for (const auto &edge : connections) {
            int first = root(parent, edge[0]), last = root(parent, edge[1]);
            if (first != last) {
                if (size[first] < size[last])
                    std::swap(first, last);
                parent[last] = first;
                size[first] += size[last];
                --components;
            }
        }
        return components - 1;
    }

  private:
    static int root(vector<int> &parent, int node) {
        while (parent[node] != node) {
            parent[node] = parent[parent[node]];
            node = parent[node];
        }
        return node;
    }
};
