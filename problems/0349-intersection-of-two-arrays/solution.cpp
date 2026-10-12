#include <unordered_set>
#include <vector>

class Solution {
public:
    std::vector<int> intersection(std::vector<int>& nums1, std::vector<int>& nums2) {
        std::unordered_set<int> available(nums1.begin(), nums1.end());
        std::vector<int> result;
        for (const int value : nums2) {
            if (available.erase(value) != 0) {
                result.push_back(value);
            }
        }
        return result;
    }
};
