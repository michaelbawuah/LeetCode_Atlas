#include <algorithm>
#include <cstddef>
#include <vector>

using std::vector;

class Solution {
public:
    int maxArea(vector<int>& height) {
        std::size_t left = 0;
        std::size_t right = height.size() - 1;
        long long best = 0;
        while (left < right) {
            const auto width = static_cast<long long>(right - left);
            best = std::max(best, width * std::min(height[left], height[right]));
            if (height[left] <= height[right]) {
                ++left;
            } else {
                --right;
            }
        }
        return static_cast<int>(best);
    }
};
