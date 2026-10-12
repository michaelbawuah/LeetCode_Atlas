#include <algorithm>
#include <cstddef>
#include <vector>

using std::vector;

class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {
        const int unreachable = amount + 1;
        vector<int> minimum(static_cast<std::size_t>(amount) + 1, unreachable);
        minimum[0] = 0;
        for (int current = 1; current <= amount; ++current) {
            for (const int coin : coins) {
                if (coin > 0 && coin <= current) {
                    minimum[static_cast<std::size_t>(current)] =
                        std::min(minimum[static_cast<std::size_t>(current)],
                                 minimum[static_cast<std::size_t>(current - coin)] + 1);
                }
            }
        }
        const int answer = minimum[static_cast<std::size_t>(amount)];
        return answer == unreachable ? -1 : answer;
    }
};
