#include <algorithm>
#include <cstddef>
#include <string>
#include <vector>
using std::string;
class Solution {
public:
    int minDistance(const string& word1, const string& word2) {
        const string& longer = word1.size() >= word2.size() ? word1 : word2;
        const string& shorter = word1.size() >= word2.size() ? word2 : word1;
        std::vector<int> best(shorter.size() + 1, 0);
        for (const char first : longer) {
            int diagonal = 0;
            for (std::size_t column = 1; column <= shorter.size(); ++column) {
                const int above = best[column];
                best[column] = first == shorter[column - 1] ? diagonal + 1 : std::max(best[column], best[column - 1]);
                diagonal = above;
            }
        }
        return static_cast<int>(word1.size() + word2.size()) - 2 * best.back();
    }
};
