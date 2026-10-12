#include <algorithm>
#include <cstddef>
#include <functional>
#include <vector>

class Solution {
public:
    std::vector<std::vector<int>> subsetsWithDup(std::vector<int>& nums) {
        auto ordered = nums;
        std::sort(ordered.begin(), ordered.end());
        std::vector<std::vector<int>> answers;
        std::vector<int> path;
        std::function<void(std::size_t)> choose = [&](std::size_t start) {
            answers.push_back(path);
            for (std::size_t index = start; index < ordered.size(); ++index) {
                if (index > start && ordered[index] == ordered[index - 1]) continue;
                path.push_back(ordered[index]);
                choose(index + 1);
                path.pop_back();
            }
        };
        choose(0);
        return answers;
    }
};
