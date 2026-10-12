#include <algorithm>
#include <cstddef>
#include <vector>

using std::vector;

class Solution {
public:
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        vector<int> choices = candidates;
        std::sort(choices.begin(), choices.end());
        vector<vector<int>> answers;
        vector<int> path;
        search(choices, 0, target, path, answers);
        return answers;
    }

private:
    static void search(const vector<int>& choices, std::size_t start, int remaining,
                       vector<int>& path, vector<vector<int>>& answers) {
        if (remaining == 0) {
            answers.push_back(path);
            return;
        }
        for (std::size_t index = start; index < choices.size(); ++index) {
            const int value = choices[index];
            if (value > remaining) {
                break;
            }
            path.push_back(value);
            search(choices, index, remaining - value, path, answers);
            path.pop_back();
        }
    }
};
