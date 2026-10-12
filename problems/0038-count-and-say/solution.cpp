#include <cstddef>
#include <string>
#include <utility>

class Solution {
public:
    std::string countAndSay(int n) {
        std::string term = "1";
        for (int iteration = 1; iteration < n; ++iteration) {
            std::string following;
            std::size_t start = 0;
            while (start < term.size()) {
                std::size_t end = start + 1;
                while (end < term.size() && term[end] == term[start]) ++end;
                following += std::to_string(end - start);
                following.push_back(term[start]);
                start = end;
            }
            term = std::move(following);
        }
        return term;
    }
};
