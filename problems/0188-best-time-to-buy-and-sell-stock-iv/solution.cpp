#include <algorithm>
#include <cstddef>
#include <cstdint>
#include <limits>
#include <vector>

class Solution {
public:
    int maxProfit(int k, std::vector<int>& prices) {
        if (static_cast<std::size_t>(k) >= prices.size() / 2) {
            std::int64_t profit = 0;
            for (std::size_t day = 1; day < prices.size(); ++day) {
                const std::int64_t delta =
                    static_cast<std::int64_t>(prices[day]) - prices[day - 1];
                profit += std::max<std::int64_t>(0, delta);
            }
            return static_cast<int>(profit);
        }
        const auto states = static_cast<std::size_t>(k) + 1;
        std::vector<std::int64_t> cash(states, 0);
        std::vector<std::int64_t> held(
            states, std::numeric_limits<std::int64_t>::lowest() / 4);
        for (int value : prices) {
            const std::int64_t price = value;
            for (int completed = k; completed > 0; --completed) {
                const auto index = static_cast<std::size_t>(completed);
                cash[index] = std::max(cash[index], held[index] + price);
                held[index] = std::max(held[index], cash[index - 1] - price);
            }
        }
        return static_cast<int>(cash.back());
    }
};
