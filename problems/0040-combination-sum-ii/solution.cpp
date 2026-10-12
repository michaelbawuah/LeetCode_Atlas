#include <algorithm>
#include <cstddef>
#include <functional>
#include <vector>

class Solution {
public:
    std::vector<std::vector<int>> combinationSum2(std::vector<int>& candidates, int target) {
        auto ordered = candidates;
        std::sort(ordered.begin(), ordered.end());
        std::vector<std::vector<int>> answers;
        std::vector<int> path;
        std::function<void(std::size_t, int)> choose = [&](std::size_t start, int remaining) {
            if (remaining == 0) {
                answers.push_back(path);
                return;
            }
            for (std::size_t index = start; index < ordered.size(); ++index) {
                const int value = ordered[index];
                if (value > remaining) break;
                if (index > start && value == ordered[index - 1]) continue;
                path.push_back(value);
                choose(index + 1, remaining - value);
                path.pop_back();
            }
        };
        choose(0, target);
        return answers;
    }
};
