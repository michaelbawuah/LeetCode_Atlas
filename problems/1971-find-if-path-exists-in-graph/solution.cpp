#include <cstddef>
#include <numeric>
#include <utility>
#include <vector>
using std::vector;
class Solution {
  public:
    bool validPath(int n, vector<vector<int>> &edges, int source, int destination) {
        vector<int> parent(static_cast<std::size_t>(n)), size(static_cast<std::size_t>(n), 1);
        std::iota(parent.begin(), parent.end(), 0);
        for (const auto &edge : edges) {
            int first = root(parent, edge[0]), last = root(parent, edge[1]);
            if (first != last) {
                if (size[first] < size[last])
                    std::swap(first, last);
                parent[last] = first;
                size[first] += size[last];
            }
        }
        return root(parent, source) == root(parent, destination);
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
