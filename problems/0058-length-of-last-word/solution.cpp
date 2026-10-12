#include <cstddef>
#include <string>
class Solution {
public:
    int lengthOfLastWord(const std::string& s) {
        int index = static_cast<int>(s.size()) - 1;
        while (index >= 0 && s[static_cast<std::size_t>(index)] == ' ') --index;
        const int end = index;
        while (index >= 0 && s[static_cast<std::size_t>(index)] != ' ') --index;
        return end - index;
    }
};
