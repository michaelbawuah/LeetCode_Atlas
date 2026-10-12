#include <algorithm>
#include <cstddef>
#include <string>
#include <vector>
using std::string;
class Solution {
public:
    int minimumDeleteSum(const string& s1, const string& s2) {
        const string& longer = s1.size() >= s2.size() ? s1 : s2;
        const string& shorter = s1.size() >= s2.size() ? s2 : s1;
        std::vector<int> previous(shorter.size() + 1, 0);
        for (std::size_t column = 1; column <= shorter.size(); ++column) {
            previous[column] = previous[column - 1] + static_cast<unsigned char>(shorter[column - 1]);
        }
        for (const char first : longer) {
            std::vector<int> current(shorter.size() + 1, 0);
            current[0] = previous[0] + static_cast<unsigned char>(first);
            for (std::size_t column = 1; column <= shorter.size(); ++column) {
                const char second = shorter[column - 1];
                current[column] = first == second ? previous[column - 1] : std::min(previous[column] + static_cast<unsigned char>(first), current[column - 1] + static_cast<unsigned char>(second));
            }
            previous.swap(current);
        }
        return previous.back();
    }
};
