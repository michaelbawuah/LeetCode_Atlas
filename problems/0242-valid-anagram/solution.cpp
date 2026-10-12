#include <array>
#include <cstddef>
#include <string>

using std::string;

class Solution {
public:
    bool isAnagram(const string& s, const string& t) {
        if (s.size() != t.size()) {
            return false;
        }
        std::array<int, 26> counts{};
        for (const char character : s) {
            ++counts[static_cast<std::size_t>(character - 'a')];
        }
        for (const char character : t) {
            --counts[static_cast<std::size_t>(character - 'a')];
        }
        for (const int count : counts) {
            if (count != 0) {
                return false;
            }
        }
        return true;
    }
};
