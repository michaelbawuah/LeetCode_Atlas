#include <algorithm>
#include <cstddef>
#include <vector>

class Solution {
public:
    int maxProfit(std::vector<int>& prices) {
        int profit = 0;
        for (std::size_t index = 1; index < prices.size(); ++index) {
            profit += std::max(0, prices[index] - prices[index - 1]);
        }
        return profit;
    }
};
