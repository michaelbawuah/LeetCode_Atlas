#include <cstddef>
#include <string>

class Solution {
public:
    std::string longestPalindrome(std::string s) {
        const int size = static_cast<int>(s.size());
        int best_start = 0;
        int best_length = 1;
        for (int center = 0; center < size; ++center) {
            for (int gap = 0; gap <= 1; ++gap) {
                int left = center;
                int right = center + gap;
                while (left >= 0 && right < size &&
                       s[static_cast<std::size_t>(left)] == s[static_cast<std::size_t>(right)]) {
                    const int length = right - left + 1;
                    if (length > best_length) {
                        best_start = left;
                        best_length = length;
                    }
                    --left;
                    ++right;
                }
            }
        }
        return s.substr(static_cast<std::size_t>(best_start), static_cast<std::size_t>(best_length));
    }
};
