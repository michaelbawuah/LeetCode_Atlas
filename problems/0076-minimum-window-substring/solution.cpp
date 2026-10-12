#include <array>
#include <cstddef>
#include <string>

using std::string;

class Solution {
public:
    string minWindow(string s, string t) {
        if (t.empty() || s.size() < t.size()) {
            return "";
        }
        std::array<int, 256> needed{};
        for (const char character : t) {
            ++needed[static_cast<unsigned char>(character)];
        }
        std::size_t missing = t.size();
        std::size_t left = 0;
        std::size_t best_start = 0;
        std::size_t best_length = string::npos;
        for (std::size_t right = 0; right < s.size(); ++right) {
            const auto incoming = static_cast<unsigned char>(s[right]);
            if (needed[incoming] > 0) {
                --missing;
            }
            --needed[incoming];
            while (missing == 0) {
                const std::size_t length = right - left + 1;
                if (length < best_length) {
                    best_length = length;
                    best_start = left;
                }
                const auto outgoing = static_cast<unsigned char>(s[left++]);
                if (++needed[outgoing] > 0) {
                    ++missing;
                }
            }
        }
        return best_length == string::npos ? "" : s.substr(best_start, best_length);
    }
};
