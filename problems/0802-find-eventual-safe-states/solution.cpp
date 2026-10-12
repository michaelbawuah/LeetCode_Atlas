#include <cstddef>
#include <queue>
#include <vector>
using std::vector;
class Solution {
  public:
    vector<int> eventualSafeNodes(vector<vector<int>> &graph) {
        vector<vector<int>> parents(graph.size());
        vector<int> degree(graph.size());
        std::queue<int> pending;
        for (std::size_t node = 0; node < graph.size(); ++node) {
            degree[node] = static_cast<int>(graph[node].size());
            if (degree[node] == 0)
                pending.push(static_cast<int>(node));
            for (int neighbor : graph[node])
                parents[neighbor].push_back(static_cast<int>(node));
        }
        while (!pending.empty()) {
            int node = pending.front();
            pending.pop();
            for (int parent : parents[node])
                if (--degree[parent] == 0)
                    pending.push(parent);
        }
        vector<int> answers;
        for (std::size_t node = 0; node < graph.size(); ++node)
            if (degree[node] == 0)
                answers.push_back(static_cast<int>(node));
        return answers;
    }
};
