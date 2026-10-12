#include <cstddef>
#include <vector>

using std::vector;

class Solution {
public:
    int findCircleNum(vector<vector<int>>& isConnected) {
        const std::size_t count = isConnected.size();
        vector<bool> seen(count, false);
        int provinces = 0;
        for (std::size_t start = 0; start < count; ++start) {
            if (seen[start]) {
                continue;
            }
            ++provinces;
            seen[start] = true;
            vector<std::size_t> pending{start};
            while (!pending.empty()) {
                const std::size_t city = pending.back();
                pending.pop_back();
                for (std::size_t neighbor = 0; neighbor < count; ++neighbor) {
                    if (isConnected[city][neighbor] && !seen[neighbor]) {
                        seen[neighbor] = true;
                        pending.push_back(neighbor);
                    }
                }
            }
        }
        return provinces;
    }
};
