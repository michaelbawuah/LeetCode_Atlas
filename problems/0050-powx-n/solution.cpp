#include <cstdint>

class Solution {
public:
    double myPow(double x, int n) {
        std::int64_t exponent = n;
        if (exponent < 0) {
            x = 1.0 / x;
            exponent = -exponent;
        }
        double result = 1.0;
        while (exponent != 0) {
            if ((exponent & 1) != 0) {
                result *= x;
            }
            exponent >>= 1;
            if (exponent != 0) {
                x *= x;
            }
        }
        return result;
    }
};
