#include <algorithm>
#include <cstddef>
#include <cstdlib>
#include <limits>
#include <vector>

using std::vector;

class Solution {
public:
    int minCostConnectPoints(vector<vector<int>>& points) {
        const std::size_t count = points.size();
        vector<long long> closest(count, std::numeric_limits<long long>::max());
        vector<bool> included(count, false);
        closest[0] = 0;
        long long total = 0;
        for (std::size_t step = 0; step < count; ++step) {
            std::size_t chosen = count;
            for (std::size_t index = 0; index < count; ++index) {
                if (!included[index] && (chosen == count || closest[index] < closest[chosen])) {
                    chosen = index;
                }
            }
            included[chosen] = true;
            total += closest[chosen];
            for (std::size_t index = 0; index < count; ++index) {
                if (!included[index]) {
                    const long long distance =
                        std::llabs(static_cast<long long>(points[chosen][0]) - points[index][0]) +
                        std::llabs(static_cast<long long>(points[chosen][1]) - points[index][1]);
                    closest[index] = std::min(closest[index], distance);
                }
            }
        }
        return static_cast<int>(total);
    }
};
