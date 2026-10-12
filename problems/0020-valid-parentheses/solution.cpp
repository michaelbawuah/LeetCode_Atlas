#include <string>
#include <vector>

using std::string;

class Solution {
public:
    bool isValid(string s) {
        std::vector<char> openings;
        openings.reserve(s.size());
        for (const char character : s) {
            if (character == '(' || character == '[' || character == '{') {
                openings.push_back(character);
                continue;
            }
            char required;
            switch (character) {
                case ')':
                    required = '(';
                    break;
                case ']':
                    required = '[';
                    break;
                case '}':
                    required = '{';
                    break;
                default:
                    return false;
            }
            if (openings.empty() || openings.back() != required) {
                return false;
            }
            openings.pop_back();
        }
        return openings.empty();
    }
};
