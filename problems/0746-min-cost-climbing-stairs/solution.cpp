#include <algorithm>
#include <cstddef>
#include <cstdint>
#include <vector>

using std::vector;

class Solution {
public:
    int minCostClimbingStairs(vector<int>& cost) {
        std::int64_t two_back = 0;
        std::int64_t one_back = 0;
        for (std::size_t step = 2; step <= cost.size(); ++step) {
            const auto following = std::min(one_back + cost[step - 1], two_back + cost[step - 2]);
            two_back = one_back;
            one_back = following;
        }
        return static_cast<int>(one_back);
    }
};
