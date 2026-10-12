#include <algorithm>
#include <cstddef>
#include <string>
#include <unordered_set>
#include <vector>

using std::string;
using std::vector;

class Solution {
public:
    bool wordBreak(const string& s, vector<string>& wordDict) {
        const std::unordered_set<string> words(wordDict.begin(), wordDict.end());
        std::size_t longest = 0;
        for (const auto& word : wordDict) {
            longest = std::max(longest, word.size());
        }
        vector<unsigned char> present(longest + 1, 0);
        for (const auto& word : wordDict) {
            present[word.size()] = 1;
        }
        vector<std::size_t> lengths;
        for (std::size_t length = 1; length <= longest; ++length) {
            if (present[length] != 0) {
                lengths.push_back(length);
            }
        }
        vector<unsigned char> possible(s.size() + 1, 0);
        possible[0] = 1;
        for (std::size_t end = 1; end <= s.size(); ++end) {
            for (const auto length : lengths) {
                if (length > end) {
                    break;
                }
                if (possible[end - length] != 0 && words.contains(s.substr(end - length, length))) {
                    possible[end] = 1;
                    break;
                }
            }
        }
        return possible.back() != 0;
    }
};
