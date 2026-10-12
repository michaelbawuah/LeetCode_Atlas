#include <algorithm>
#include <cstddef>
#include <string>
#include <vector>
using std::string;
class Solution {
public:
    int longestValidParentheses(const string& s) {
        std::vector<int> boundaries{-1};
        int best = 0;
        for (std::size_t position = 0; position < s.size(); ++position) {
            const int index = static_cast<int>(position);
            if (s[position] == '(') {
                boundaries.push_back(index);
            } else {
                boundaries.pop_back();
                if (boundaries.empty()) {
                    boundaries.push_back(index);
                } else {
                    best = std::max(best, index - boundaries.back());
                }
            }
        }
        return best;
    }
};
