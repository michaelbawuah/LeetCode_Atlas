#include <algorithm>
#include <cstddef>
#include <vector>

using std::vector;

class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int>> triples;
        if (nums.size() < 3) {
            return triples;
        }
        std::sort(nums.begin(), nums.end());
        for (std::size_t first = 0; first < nums.size() - 2; ++first) {
            if (first > 0 && nums[first] == nums[first - 1]) {
                continue;
            }
            if (nums[first] > 0) {
                break;
            }
            std::size_t left = first + 1;
            std::size_t right = nums.size() - 1;
            while (left < right) {
                const long long sum = static_cast<long long>(nums[first]) + nums[left] + nums[right];
                if (sum < 0) {
                    ++left;
                } else if (sum > 0) {
                    --right;
                } else {
                    triples.push_back({nums[first], nums[left], nums[right]});
                    ++left;
                    --right;
                    while (left < right && nums[left] == nums[left - 1]) {
                        ++left;
                    }
                    while (left < right && nums[right] == nums[right + 1]) {
                        --right;
                    }
                }
            }
        }
        return triples;
    }
};
