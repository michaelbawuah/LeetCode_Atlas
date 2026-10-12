#include <algorithm>
#include <cstddef>
#include <numeric>
#include <string>
#include <vector>

using std::string;

class Solution {
public:
    int minDistance(const string& word1, const string& word2) {
        const string& longer = word1.size() >= word2.size() ? word1 : word2;
        const string& shorter = word1.size() >= word2.size() ? word2 : word1;
        std::vector<int> previous(shorter.size() + 1);
        std::iota(previous.begin(), previous.end(), 0);
        for (std::size_t row = 1; row <= longer.size(); ++row) {
            std::vector<int> current(shorter.size() + 1);
            current[0] = static_cast<int>(row);
            for (std::size_t column = 1; column <= shorter.size(); ++column) {
                current[column] = longer[row - 1] == shorter[column - 1]
                    ? previous[column - 1]
                    : 1 + std::min({previous[column], current[column - 1], previous[column - 1]});
            }
            previous.swap(current);
        }
        return previous.back();
    }
};
