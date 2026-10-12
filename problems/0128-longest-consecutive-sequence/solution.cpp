#include <algorithm>
#include <limits>
#include <unordered_set>
#include <vector>

using std::vector;

class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        const std::unordered_set<int> values(nums.begin(), nums.end());
        int best = 0;
        for (const int value : values) {
            if (value != std::numeric_limits<int>::min() && values.contains(value - 1)) {
                continue;
            }
            int length = 0;
            int current = value;
            while (values.contains(current)) {
                ++length;
                if (current == std::numeric_limits<int>::max()) {
                    break;
                }
                ++current;
            }
            best = std::max(best, length);
        }
        return best;
    }
};
