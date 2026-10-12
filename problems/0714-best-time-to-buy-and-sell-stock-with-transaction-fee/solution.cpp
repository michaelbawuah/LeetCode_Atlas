#include <algorithm>
#include <cstddef>
#include <cstdint>
#include <vector>
using std::vector;
class Solution {
public:
    int maxProfit(vector<int>& prices, int fee) {
        std::int64_t cash = 0;
        std::int64_t held = -static_cast<std::int64_t>(prices.front());
        for (std::size_t index = 1; index < prices.size(); ++index) {
            const auto following_cash = std::max(cash, held + prices[index] - fee);
            held = std::max(held, cash - prices[index]);
            cash = following_cash;
        }
        return static_cast<int>(cash);
    }
};
