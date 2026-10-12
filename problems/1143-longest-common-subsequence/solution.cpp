#include <algorithm>
#include <cstddef>
#include <string>
#include <vector>

class Solution {
public:
    int longestCommonSubsequence(std::string text1, std::string text2) {
        if (text1.size() < text2.size()) {
            text1.swap(text2);
        }
        std::vector<int> previous(text2.size() + 1, 0);
        for (char first : text1) {
            std::vector<int> current(text2.size() + 1, 0);
            for (std::size_t column = 1; column <= text2.size(); ++column) {
                current[column] = first == text2[column - 1]
                                      ? previous[column - 1] + 1
                                      : std::max(previous[column], current[column - 1]);
            }
            previous.swap(current);
        }
        return previous.back();
    }
};
