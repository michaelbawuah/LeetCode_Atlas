#include <algorithm>
#include <vector>

using std::vector;

class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        vector<int> tails;
        tails.reserve(nums.size());
        for (const int value : nums) {
            const auto position = std::lower_bound(tails.begin(), tails.end(), value);
            if (position == tails.end()) {
                tails.push_back(value);
            } else {
                *position = value;
            }
        }
        return static_cast<int>(tails.size());
    }
};
