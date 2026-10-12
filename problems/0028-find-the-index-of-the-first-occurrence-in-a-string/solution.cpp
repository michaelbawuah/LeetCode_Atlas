#include <cstddef>
#include <string>
#include <vector>
class Solution {
public:
    int strStr(const std::string& haystack, const std::string& needle) {
        if (needle.empty()) return 0;
        std::vector<std::size_t> failure(needle.size(), 0);
        for (std::size_t i = 1; i < needle.size(); ++i) {
            auto matched = failure[i - 1];
            while (matched != 0 && needle[i] != needle[matched]) matched = failure[matched - 1];
            if (needle[i] == needle[matched]) ++matched;
            failure[i] = matched;
        }
        std::size_t matched = 0;
        for (std::size_t i = 0; i < haystack.size(); ++i) {
            while (matched != 0 && haystack[i] != needle[matched]) matched = failure[matched - 1];
            if (haystack[i] == needle[matched]) ++matched;
            if (matched == needle.size()) return static_cast<int>(i + 1 - needle.size());
        }
        return -1;
    }
};
