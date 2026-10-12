#include <string>
class Solution {
public:
    int titleToNumber(const std::string& title) {
        int result = 0;
        for (char letter : title) result = result * 26 + (letter - 'A' + 1);
        return result;
    }
};
