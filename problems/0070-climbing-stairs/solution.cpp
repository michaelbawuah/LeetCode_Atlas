#include <cstdint>

class Solution {
public:
    int climbStairs(int n) {
        std::int64_t two_back = 1;
        std::int64_t one_back = 1;
        for (int height = 2; height <= n; ++height) {
            const auto following = two_back + one_back;
            two_back = one_back;
            one_back = following;
        }
        return static_cast<int>(one_back);
    }
};
