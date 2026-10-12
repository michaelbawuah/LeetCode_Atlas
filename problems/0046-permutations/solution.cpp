#include <cstddef>
#include <utility>
#include <vector>

using std::vector;

class Solution {
public:
    vector<vector<int>> permute(vector<int>& nums) {
        vector<int> values = nums;
        vector<vector<int>> answers;
        arrange(values, 0, answers);
        return answers;
    }

private:
    static void arrange(vector<int>& values, std::size_t start, vector<vector<int>>& answers) {
        if (start == values.size()) {
            answers.push_back(values);
            return;
        }
        for (std::size_t index = start; index < values.size(); ++index) {
            std::swap(values[start], values[index]);
            arrange(values, start + 1, answers);
            std::swap(values[start], values[index]);
        }
    }
};
