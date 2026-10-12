#include <cstddef>
#include <string>
#include <vector>

class Solution {
public:
    bool isMatch(std::string s, std::string p) {
        std::vector<bool> previous(p.size() + 1, false);
        previous[0] = true;
        for (std::size_t column = 2; column <= p.size(); ++column) {
            if (p[column - 1] == '*') {
                previous[column] = previous[column - 2];
            }
        }
        for (char letter : s) {
            std::vector<bool> current(p.size() + 1, false);
            for (std::size_t column = 1; column <= p.size(); ++column) {
                if (p[column - 1] == '*') {
                    const char atom = p[column - 2];
                    const bool matches = atom == '.' || atom == letter;
                    current[column] = current[column - 2] || (matches && previous[column]);
                } else {
                    const bool matches = p[column - 1] == '.' || p[column - 1] == letter;
                    current[column] = previous[column - 1] && matches;
                }
            }
            previous.swap(current);
        }
        return previous.back();
    }
};
