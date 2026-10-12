#include <algorithm>
#include <cstddef>
#include <cstdint>
#include <limits>
#include <string>
#include <vector>

class Solution {
public:
    int numDistinct(std::string s, std::string t) {
        if (t.size() > s.size()) {
            return 0;
        }
        constexpr std::int64_t cap = std::numeric_limits<int>::max();
        std::vector<int> counts(t.size() + 1, 0);
        counts[0] = 1;
        for (char letter : s) {
            for (std::size_t length = t.size(); length > 0; --length) {
                if (letter == t[length - 1]) {
                    const std::int64_t sum =
                        static_cast<std::int64_t>(counts[length]) + counts[length - 1];
                    counts[length] = static_cast<int>(std::min(sum, cap));
                }
            }
        }
        return counts.back();
    }
};
