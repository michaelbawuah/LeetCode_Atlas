#include <cstddef>
#include <string>
#include <utility>
#include <vector>

class Solution {
public:
    bool isInterleave(std::string s1, std::string s2, std::string s3) {
        if (s1.size() + s2.size() != s3.size()) {
            return false;
        }
        if (s1.size() < s2.size()) {
            s1.swap(s2);
        }
        std::vector<bool> possible(s2.size() + 1, false);
        possible[0] = true;
        for (std::size_t column = 1; column <= s2.size(); ++column) {
            possible[column] = possible[column - 1] && s2[column - 1] == s3[column - 1];
        }
        for (std::size_t row = 1; row <= s1.size(); ++row) {
            possible[0] = possible[0] && s1[row - 1] == s3[row - 1];
            for (std::size_t column = 1; column <= s2.size(); ++column) {
                const char newest = s3[row + column - 1];
                possible[column] = (possible[column] && s1[row - 1] == newest) ||
                                   (possible[column - 1] && s2[column - 1] == newest);
            }
        }
        return possible.back();
    }
};
