#include <cstddef>
#include <string>
#include <vector>

class Solution {
public:
    bool isMatch(std::string s, std::string p) {
        std::vector<bool> previous(p.size() + 1, false);
        previous[0] = true;
        for (std::size_t column = 1; column <= p.size(); ++column) {
            previous[column] = previous[column - 1] && p[column - 1] == '*';
        }
        for (char letter : s) {
            std::vector<bool> current(p.size() + 1, false);
            for (std::size_t column = 1; column <= p.size(); ++column) {
                if (p[column - 1] == '*') {
                    current[column] = current[column - 1] || previous[column];
                } else {
                    current[column] = previous[column - 1] &&
                                      (p[column - 1] == '?' || p[column - 1] == letter);
                }
            }
            previous.swap(current);
        }
        return previous.back();
    }
};
