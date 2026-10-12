#include <cstdint>
#include <vector>

using std::vector;

class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int left = 0;
        int right = static_cast<int>(numbers.size()) - 1;
        while (left < right) {
            const std::int64_t total = static_cast<std::int64_t>(numbers[left]) + numbers[right];
            if (total == target) {
                return {left + 1, right + 1};
            }
            if (total < target) {
                ++left;
            } else {
                --right;
            }
        }
        return {};
    }
};
