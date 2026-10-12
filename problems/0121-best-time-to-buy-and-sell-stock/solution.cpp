#include <algorithm>
#include <cstddef>
#include <vector>

using std::vector;

class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int cheapest = prices.front();
        int best = 0;
        for (std::size_t index = 1; index < prices.size(); ++index) {
            best = std::max(best, prices[index] - cheapest);
            cheapest = std::min(cheapest, prices[index]);
        }
        return best;
    }
};
