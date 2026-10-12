#include <algorithm>
#include <limits>
#include <vector>

class Solution {
public:
    int findCheapestPrice(int n, std::vector<std::vector<int>>& flights,
                          int src, int dst, int k) {
        constexpr int unreachable = std::numeric_limits<int>::max();
        std::vector<int> costs(n, unreachable);
        costs[src] = 0;
        for (int layer = 0; layer <= k; ++layer) {
            auto next = costs;
            for (const auto& flight : flights) {
                if (costs[flight[0]] != unreachable) {
                    // Official bounds allow at most 100 edges priced at most 10,000.
                    next[flight[1]] = std::min(next[flight[1]], costs[flight[0]] + flight[2]);
                }
            }
            costs.swap(next);
        }
        return costs[dst] == unreachable ? -1 : costs[dst];
    }
};
