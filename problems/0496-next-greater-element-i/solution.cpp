#include <unordered_map>
#include <vector>
class Solution {
public:
    std::vector<int> nextGreaterElement(std::vector<int>& nums1, std::vector<int>& nums2) {
        std::unordered_map<int, int> following; std::vector<int> pending;
        for (int value : nums2) {
            while (!pending.empty() && pending.back() < value) {
                following[pending.back()] = value; pending.pop_back();
            }
            pending.push_back(value);
        }
        std::vector<int> result; result.reserve(nums1.size());
        for (int value : nums1) {
            const auto found = following.find(value);
            result.push_back(found == following.end() ? -1 : found->second);
        }
        return result;
    }
};
