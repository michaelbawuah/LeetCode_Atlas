#include <cstddef>
#include <string>
class Solution {
    static int value(char letter) {
        switch (letter) {
            case 'I': return 1; case 'V': return 5; case 'X': return 10;
            case 'L': return 50; case 'C': return 100; case 'D': return 500;
            case 'M': return 1000; default: return 0;
        }
    }
public:
    int romanToInt(const std::string& s) {
        int result = 0;
        for (std::size_t i = 0; i < s.size(); ++i) {
            const int current = value(s[i]);
            result += i + 1 < s.size() && current < value(s[i + 1]) ? -current : current;
        }
        return result;
    }
};
