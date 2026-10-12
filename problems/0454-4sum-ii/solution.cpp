#include <unordered_map>
#include <vector>

class Solution {
public:
    int fourSumCount(std::vector<int>& nums1, std::vector<int>& nums2, std::vector<int>& nums3, std::vector<int>& nums4) {
        std::unordered_map<long long, int> counts;
        counts.reserve(nums1.size() * nums2.size());
        for (const int first : nums1) {
            for (const int second : nums2) {
                ++counts[static_cast<long long>(first) + second];
            }
        }
        long long answer = 0;
        for (const int third : nums3) {
            for (const int fourth : nums4) {
                const auto found = counts.find(-static_cast<long long>(third) - fourth);
                if (found != counts.end()) {
                    answer += found->second;
                }
            }
        }
        return static_cast<int>(answer);
    }
};
