#include <sstream>
#include <string>
#include <vector>
class Solution {
public:
    std::string reverseWords(const std::string& s) {
        std::istringstream stream(s); std::vector<std::string> words; std::string word;
        while (stream >> word) words.push_back(word);
        std::string result;
        result.reserve(s.size());
        for (auto it = words.rbegin(); it != words.rend(); ++it) {
            if (!result.empty()) result += ' ';
            result += *it;
        }
        return result;
    }
};
