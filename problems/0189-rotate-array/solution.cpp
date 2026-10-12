#include <algorithm>
#include <vector>

using std::vector;

class Solution {
public:
    void rotate(vector<int>& nums, int k) {
        k %= static_cast<int>(nums.size());
        if (k == 0) {
            return;
        }
        std::reverse(nums.begin(), nums.end());
        std::reverse(nums.begin(), nums.begin() + k);
        std::reverse(nums.begin() + k, nums.end());
    }
};
