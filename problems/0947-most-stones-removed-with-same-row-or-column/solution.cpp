#include <cstddef>
#include <unordered_map>
#include <unordered_set>
#include <utility>
#include <vector>
using std::vector;
class Solution {
  public:
    int removeStones(vector<vector<int>> &stones) {
        std::unordered_map<int, int> identities;
        vector<int> parent, size;
        auto index = [&](int key) {
            auto [position, inserted] = identities.emplace(key, static_cast<int>(parent.size()));
            if (inserted) {
                parent.push_back(static_cast<int>(parent.size()));
                size.push_back(1);
            }
            return position->second;
        };
        for (const auto &stone : stones) {
            int first = root(parent, index(stone[0] * 2)),
                last = root(parent, index(stone[1] * 2 + 1));
            if (first != last) {
                if (size[first] < size[last])
                    std::swap(first, last);
                parent[last] = first;
                size[first] += size[last];
            }
        }
        std::unordered_set<int> components;
        for (const auto &stone : stones)
            components.insert(root(parent, identities.at(stone[0] * 2)));
        return static_cast<int>(stones.size() - components.size());
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
