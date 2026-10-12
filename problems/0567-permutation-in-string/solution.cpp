#include <array>
#include <string>

class Solution {
public:
    bool checkInclusion(std::string s1, std::string s2) {
        const int width = static_cast<int>(s1.size());
        const int size = static_cast<int>(s2.size());
        if (width > size) {
            return false;
        }
        std::array<int, 26> required{};
        std::array<int, 26> window{};
        for (char value : s1) {
            ++required[value - 'a'];
        }
        for (int right = 0; right < size; ++right) {
            ++window[s2[right] - 'a'];
            if (right >= width) {
                --window[s2[right - width] - 'a'];
            }
            if (right >= width - 1 && window == required) {
                return true;
            }
        }
        return false;
    }
};
