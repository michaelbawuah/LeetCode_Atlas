#include <algorithm>
#include <cstddef>
#include <cstdint>
#include <limits>
#include <string>

class Solution {
public:
    int numDecodings(std::string s) {
        constexpr std::int64_t cap = std::numeric_limits<int>::max();
        int two_back = 1;
        int one_back = s[0] != '0' ? 1 : 0;
        for (std::size_t index = 1; index < s.size(); ++index) {
            std::int64_t ways = s[index] != '0' ? one_back : 0;
            const int pair = (s[index - 1] - '0') * 10 + (s[index] - '0');
            if (pair >= 10 && pair <= 26) {
                ways += two_back;
            }
            two_back = one_back;
            one_back = static_cast<int>(std::min(ways, cap));
        }
        return one_back;
    }
};
