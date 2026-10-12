#include <algorithm>
#include <cstdlib>
#include <vector>

using std::vector;

class Solution {
public:
    int threeSumClosest(vector<int>& nums, int target) {
        vector<int> ordered = nums;
        std::sort(ordered.begin(), ordered.end());
        const int size = static_cast<int>(ordered.size());
        long long best = static_cast<long long>(ordered[0]) + ordered[1] + ordered[2];
        for (int anchor = 0; anchor < size - 2; ++anchor) {
            int left = anchor + 1;
            int right = size - 1;
            while (left < right) {
                const long long total = static_cast<long long>(ordered[anchor]) + ordered[left] + ordered[right];
                if (std::llabs(total - target) < std::llabs(best - target)) {
                    best = total;
                }
                if (total == target) {
                    return target;
                }
                if (total < target) {
                    ++left;
                } else {
                    --right;
                }
            }
        }
        return static_cast<int>(best);
    }
};
