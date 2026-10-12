#include <cstddef>
#include <utility>
#include <vector>

using std::vector;

class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        vector<vector<int>> answers(1);
        for (const int value : nums) {
            const std::size_t previous_size = answers.size();
            for (std::size_t index = 0; index < previous_size; ++index) {
                auto addition = answers[index];
                addition.push_back(value);
                answers.push_back(std::move(addition));
            }
        }
        return answers;
    }
};
