#include <cstdint>
class Solution {
public:
    int tribonacci(int n) {
        if (n < 2) {
            return n;
        }
        std::int64_t first = 0;
        std::int64_t second = 1;
        std::int64_t third = 1;
        for (int index = 3; index <= n; ++index) {
            const auto following = first + second + third;
            first = second;
            second = third;
            third = following;
        }
        return static_cast<int>(third);
    }
};
