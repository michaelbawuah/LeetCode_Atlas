#include <limits>
class Solution {
public:
    int reverse(int x) {
        int result = 0;
        constexpr int maximum = std::numeric_limits<int>::max();
        constexpr int minimum = std::numeric_limits<int>::min();
        while (x != 0) {
            const int digit = x % 10;
            x /= 10;
            if (result > maximum / 10 || (result == maximum / 10 && digit > maximum % 10) || result < minimum / 10 || (result == minimum / 10 && digit < minimum % 10)) return 0;
            result = result * 10 + digit;
        }
        return result;
    }
};
