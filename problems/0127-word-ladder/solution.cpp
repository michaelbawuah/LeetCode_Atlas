#include <queue>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <utility>
#include <vector>

class Solution {
public:
    int ladderLength(std::string beginWord, std::string endWord,
                     std::vector<std::string>& wordList) {
        std::unordered_set<std::string> words(wordList.begin(), wordList.end());
        if (!words.contains(endWord)) {
            return 0;
        }
        words.insert(beginWord);
        std::unordered_map<std::string, std::vector<std::string>> buckets;
        for (const auto& word : words) {
            for (std::size_t index = 0; index < word.size(); ++index) {
                auto key = word;
                key[index] = '*';
                buckets[key].push_back(word);
            }
        }
        std::queue<std::pair<std::string, int>> pending;
        pending.emplace(beginWord, 1);
        std::unordered_set<std::string> seen{beginWord};
        while (!pending.empty()) {
            const auto [word, length] = pending.front();
            pending.pop();
            if (word == endWord) {
                return length;
            }
            for (std::size_t index = 0; index < word.size(); ++index) {
                auto key = word;
                key[index] = '*';
                auto& neighbors = buckets[key];
                for (const auto& neighbor : neighbors) {
                    if (seen.insert(neighbor).second) {
                        pending.emplace(neighbor, length + 1);
                    }
                }
                // The earliest BFS visit has already offered every bucket edge.
                neighbors.clear();
            }
        }
        return 0;
    }
};
