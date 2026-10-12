#include <cstddef>
#include <deque>
#include <vector>

using std::vector;

class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        const auto width = static_cast<std::size_t>(k);
        std::deque<std::size_t> candidates;
        vector<int> result;
        result.reserve(nums.size() - width + 1);
        for (std::size_t index = 0; index < nums.size(); ++index) {
            if (index >= width && !candidates.empty() && candidates.front() <= index - width) {
                candidates.pop_front();
            }
            while (!candidates.empty() && nums[candidates.back()] <= nums[index]) {
                candidates.pop_back();
            }
            candidates.push_back(index);
            if (index + 1 >= width) {
                result.push_back(nums[candidates.front()]);
            }
        }
        return result;
    }
};
