#include <queue>
#include <vector>

class Solution {
public:
    std::vector<int> findOrder(int numCourses,
                               std::vector<std::vector<int>>& prerequisites) {
        std::vector<std::vector<int>> dependents(numCourses);
        std::vector<int> indegrees(numCourses, 0);
        for (const auto& edge : prerequisites) {
            dependents[edge[1]].push_back(edge[0]);
            ++indegrees[edge[0]];
        }
        std::queue<int> ready;
        for (int node = 0; node < numCourses; ++node) {
            if (indegrees[node] == 0) {
                ready.push(node);
            }
        }
        std::vector<int> ordering;
        ordering.reserve(numCourses);
        while (!ready.empty()) {
            const int node = ready.front();
            ready.pop();
            ordering.push_back(node);
            for (const int next : dependents[node]) {
                if (--indegrees[next] == 0) {
                    ready.push(next);
                }
            }
        }
        if (static_cast<int>(ordering.size()) != numCourses) {
            return {};
        }
        return ordering;
    }
};
