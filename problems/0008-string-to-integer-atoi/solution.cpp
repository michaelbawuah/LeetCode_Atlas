#include <cstddef>
#include <cstdint>
#include <limits>
#include <string>

class Solution {
public:
    int myAtoi(std::string s) {
        std::size_t index = 0;
        while (index < s.size() && s[index] == ' ') ++index;
        bool negative = false;
        if (index < s.size() && (s[index] == '+' || s[index] == '-')) {
            negative = s[index] == '-';
            ++index;
        }
        const auto positive_limit = static_cast<std::uint32_t>(std::numeric_limits<int>::max());
        const std::uint32_t limit = positive_limit + (negative ? 1U : 0U);
        std::uint32_t magnitude = 0;
        while (index < s.size() && s[index] >= '0' && s[index] <= '9') {
            const auto digit = static_cast<std::uint32_t>(s[index] - '0');
            // Test before multiplication: even a very long prefix never overflows.
            if (magnitude > (limit - digit) / 10U) {
                return negative ? std::numeric_limits<int>::min() : std::numeric_limits<int>::max();
            }
            magnitude = magnitude * 10U + digit;
            ++index;
        }
        const std::int64_t signed_value = negative ? -static_cast<std::int64_t>(magnitude)
                                                   : static_cast<std::int64_t>(magnitude);
        return static_cast<int>(signed_value);
    }
};
