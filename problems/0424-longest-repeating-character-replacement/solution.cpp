#include <algorithm>
#include <array>
#include <string>

class Solution {
public:
    int characterReplacement(std::string s, int k) {
        std::array<int, 26> counts{};
        int left = 0;
        int best = 0;
        const int size = static_cast<int>(s.size());
        for (int right = 0; right < size; ++right) {
            ++counts[s[right] - 'A'];
            while (right - left + 1 - *std::max_element(counts.begin(), counts.end()) > k) {
                --counts[s[left++] - 'A'];
            }
            best = std::max(best, right - left + 1);
        }
        return best;
    }
};
