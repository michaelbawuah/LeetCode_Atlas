#include <cstdint>

class Solution {
public:
    int rangeBitwiseAnd(int left, int right) {
        auto lower = static_cast<std::uint32_t>(left);
        auto upper = static_cast<std::uint32_t>(right);
        unsigned int shifts = 0;
        while (lower != upper) {
            lower >>= 1;
            upper >>= 1;
            ++shifts;
        }
        // The nonnegative signed-input domain needs at most 31 shifts.
        return static_cast<int>(lower << shifts);
    }
};
