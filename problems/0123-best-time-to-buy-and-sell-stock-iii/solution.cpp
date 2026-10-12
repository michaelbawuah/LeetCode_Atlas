#include <algorithm>
#include <cstdint>
#include <vector>

class Solution {
public:
    int maxProfit(std::vector<int>& prices) {
        std::int64_t first_buy = -static_cast<std::int64_t>(prices[0]);
        std::int64_t second_buy = first_buy;
        std::int64_t first_sell = 0;
        std::int64_t second_sell = 0;
        for (int value : prices) {
            const std::int64_t price = value;
            first_buy = std::max(first_buy, -price);
            first_sell = std::max(first_sell, first_buy + price);
            second_buy = std::max(second_buy, first_sell - price);
            second_sell = std::max(second_sell, second_buy + price);
        }
        return static_cast<int>(second_sell);
    }
};
