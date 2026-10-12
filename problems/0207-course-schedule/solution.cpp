#include <cstddef>
#include <queue>
#include <vector>

using std::vector;

class Solution {
public:
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        const auto count = static_cast<std::size_t>(numCourses);
        vector<vector<int>> dependents(count);
        vector<int> indegree(count, 0);
        for (const auto& prerequisite : prerequisites) {
            dependents[static_cast<std::size_t>(prerequisite[1])].push_back(prerequisite[0]);
            ++indegree[static_cast<std::size_t>(prerequisite[0])];
        }
        std::queue<int> ready;
        for (int course = 0; course < numCourses; ++course) {
            if (indegree[static_cast<std::size_t>(course)] == 0) {
                ready.push(course);
            }
        }
        int completed = 0;
        while (!ready.empty()) {
            const int course = ready.front();
            ready.pop();
            ++completed;
            for (const int dependent : dependents[static_cast<std::size_t>(course)]) {
                if (--indegree[static_cast<std::size_t>(dependent)] == 0) {
                    ready.push(dependent);
                }
            }
        }
        return completed == numCourses;
    }
};
