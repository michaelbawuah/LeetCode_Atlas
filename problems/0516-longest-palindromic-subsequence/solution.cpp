#include <algorithm>
#include <cstddef>
#include <string>
#include <vector>
using std::string;
class Solution {
public:
    int longestPalindromeSubseq(const string& s) {
        std::vector<int> best(s.size(), 0);
        for (std::size_t left = s.size(); left-- > 0;) {
            best[left] = 1;
            int diagonal = 0;
            for (std::size_t right = left + 1; right < s.size(); ++right) {
                const int above = best[right];
                best[right] = s[left] == s[right] ? diagonal + 2 : std::max(best[right], best[right - 1]);
                diagonal = above;
            }
        }
        return best.back();
    }
};
