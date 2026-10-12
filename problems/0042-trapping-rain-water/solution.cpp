#include <algorithm>
#include <cstddef>
#include <vector>

using std::vector;

class Solution {
public:
    int trap(vector<int>& height) {
        if (height.empty()) {
            return 0;
        }
        std::size_t left = 0;
        std::size_t right = height.size() - 1;
        int left_peak = 0;
        int right_peak = 0;
        long long water = 0;
        while (left < right) {
            if (height[left] <= height[right]) {
                left_peak = std::max(left_peak, height[left]);
                water += left_peak - height[left];
                ++left;
            } else {
                right_peak = std::max(right_peak, height[right]);
                water += right_peak - height[right];
                --right;
            }
        }
        return static_cast<int>(water);
    }
};
