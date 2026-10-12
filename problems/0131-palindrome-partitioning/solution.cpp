#include <cstddef>
#include <functional>
#include <string>
#include <vector>

class Solution {
public:
    std::vector<std::vector<std::string>> partition(std::string s) {
        const std::size_t size = s.size();
        std::vector<std::vector<bool>> palindrome(size, std::vector<bool>(size, false));
        for (std::size_t offset = size; offset > 0; --offset) {
            const std::size_t start = offset - 1;
            for (std::size_t end = start; end < size; ++end) {
                palindrome[start][end] = s[start] == s[end] &&
                    (end - start < 2 || palindrome[start + 1][end - 1]);
            }
        }
        std::vector<std::vector<std::string>> answers;
        std::vector<std::string> path;
        std::function<void(std::size_t)> split = [&](std::size_t start) {
            if (start == size) {
                answers.push_back(path);
                return;
            }
            for (std::size_t end = start; end < size; ++end) {
                if (!palindrome[start][end]) continue;
                path.push_back(s.substr(start, end - start + 1));
                split(end + 1);
                path.pop_back();
            }
        };
        split(0);
        return answers;
    }
};
