#include <cstddef>
#include <numeric>
#include <vector>

using std::vector;

class Solution {
public:
    bool canPartition(vector<int>& nums) {
        const int total = std::accumulate(nums.begin(), nums.end(), 0);
        if (total % 2 != 0) {
            return false;
        }
        const int target = total / 2;
        vector<unsigned char> possible(static_cast<std::size_t>(target) + 1, 0);
        possible[0] = 1;
        for (const int value : nums) {
            for (int subtotal = target; subtotal >= value; --subtotal) {
                const auto index = static_cast<std::size_t>(subtotal);
                const auto previous = static_cast<std::size_t>(subtotal - value);
                possible[index] = static_cast<unsigned char>(possible[index] || possible[previous]);
            }
        }
        return possible[static_cast<std::size_t>(target)] != 0;
    }
};
