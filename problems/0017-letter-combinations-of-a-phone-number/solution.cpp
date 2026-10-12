#include <array>
#include <cstddef>
#include <functional>
#include <string>
#include <vector>

class Solution {
public:
    std::vector<std::string> letterCombinations(std::string digits) {
        if (digits.empty()) return {};
        const std::array<std::string, 8> letters{"abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"};
        std::vector<std::string> answers;
        std::string path;
        path.reserve(digits.size());
        std::function<void(std::size_t)> choose = [&](std::size_t index) {
            if (index == digits.size()) {
                answers.push_back(path);
                return;
            }
            for (char letter : letters[static_cast<std::size_t>(digits[index] - '2')]) {
                path.push_back(letter);
                choose(index + 1);
                path.pop_back();
            }
        };
        choose(0);
        return answers;
    }
};
