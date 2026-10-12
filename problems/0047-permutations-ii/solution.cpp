#include <cstddef>
#include <functional>
#include <map>
#include <vector>

class Solution {
public:
    std::vector<std::vector<int>> permuteUnique(std::vector<int>& nums) {
        std::map<int, int> counts;
        for (int value : nums) ++counts[value];
        std::vector<std::vector<int>> answers;
        std::vector<int> path;
        std::function<void()> arrange = [&]() {
            if (path.size() == nums.size()) {
                answers.push_back(path);
                return;
            }
            for (auto& [value, remaining] : counts) {
                if (remaining == 0) continue;
                --remaining;
                path.push_back(value);
                arrange();
                path.pop_back();
                ++remaining;
            }
        };
        arrange();
        return answers;
    }
};
