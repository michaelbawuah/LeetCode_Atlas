#include <algorithm>
#include <cstddef>
#include <string>
#include <unordered_map>
#include <vector>

using std::string;
using std::vector;

class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        std::unordered_map<string, std::size_t> group_index;
        vector<vector<string>> groups;
        group_index.reserve(strs.size());
        for (const string& word : strs) {
            string key = word;
            std::sort(key.begin(), key.end());
            const auto [position, inserted] = group_index.emplace(key, groups.size());
            if (inserted) {
                groups.emplace_back();
            }
            groups[position->second].push_back(word);
        }
        return groups;
    }
};
