#include <algorithm>
#include <array>
#include <cstddef>
#include <string>

using std::string;

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        // Store one past each byte's latest position; zero means unseen.
        std::array<std::size_t, 256> next_start{};
        std::size_t left = 0;
        std::size_t best = 0;
        for (std::size_t right = 0; right < s.size(); ++right) {
            const auto character = static_cast<unsigned char>(s[right]);
            left = std::max(left, next_start[character]);
            best = std::max(best, right - left + 1);
            next_start[character] = right + 1;
        }
        return static_cast<int>(best);
    }
};
