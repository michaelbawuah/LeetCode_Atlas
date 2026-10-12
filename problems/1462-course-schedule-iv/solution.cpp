#include <vector>

class Solution {
public:
    std::vector<bool> checkIfPrerequisite(int numCourses,
                                          std::vector<std::vector<int>>& prerequisites,
                                          std::vector<std::vector<int>>& queries) {
        std::vector<std::vector<bool>> reach(numCourses, std::vector<bool>(numCourses, false));
        for (const auto& edge : prerequisites) {
            reach[edge[0]][edge[1]] = true;
        }
        for (int via = 0; via < numCourses; ++via) {
            for (int first = 0; first < numCourses; ++first) {
                if (reach[first][via]) {
                    for (int last = 0; last < numCourses; ++last) {
                        reach[first][last] = reach[first][last] || reach[via][last];
                    }
                }
            }
        }
        std::vector<bool> answers;
        answers.reserve(queries.size());
        for (const auto& query : queries) {
            answers.push_back(reach[query[0]][query[1]]);
        }
        return answers;
    }
};
