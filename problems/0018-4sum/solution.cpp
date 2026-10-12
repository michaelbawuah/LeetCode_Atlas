#include <algorithm>
#include <cstdint>
#include <vector>

using std::vector;

class Solution {
public:
    vector<vector<int>> fourSum(vector<int>& nums, int target) {
        vector<int> ordered = nums;
        std::sort(ordered.begin(), ordered.end());
        vector<vector<int>> answer;
        const int size = static_cast<int>(ordered.size());
        for (int first = 0; first < size - 3; ++first) {
            if (first > 0 && ordered[first] == ordered[first - 1]) {
                continue;
            }
            for (int second = first + 1; second < size - 2; ++second) {
                if (second > first + 1 && ordered[second] == ordered[second - 1]) {
                    continue;
                }
                int left = second + 1;
                int right = size - 1;
                while (left < right) {
                    const std::int64_t total = static_cast<std::int64_t>(ordered[first]) + ordered[second] + ordered[left] + ordered[right];
                    if (total < target) {
                        ++left;
                    } else if (total > target) {
                        --right;
                    } else {
                        answer.push_back({ordered[first], ordered[second], ordered[left], ordered[right]});
                        ++left;
                        --right;
                        while (left < right && ordered[left] == ordered[left - 1]) {
                            ++left;
                        }
                        while (left < right && ordered[right] == ordered[right + 1]) {
                            --right;
                        }
                    }
                }
            }
        }
        return answer;
    }
};
