#include <algorithm>
#include <cstddef>
#include <string>
class Solution {
public:
    std::string addBinary(const std::string& a, const std::string& b) {
        int left = static_cast<int>(a.size()) - 1, right = static_cast<int>(b.size()) - 1, carry = 0;
        std::string result;
        while (left >= 0 || right >= 0 || carry != 0) {
            int total = carry;
            if (left >= 0) total += a[static_cast<std::size_t>(left--)] - '0';
            if (right >= 0) total += b[static_cast<std::size_t>(right--)] - '0';
            result.push_back(static_cast<char>('0' + total % 2)); carry = total / 2;
        }
        std::reverse(result.begin(), result.end()); return result;
    }
};
