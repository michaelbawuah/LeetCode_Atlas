#include <unordered_map>
#include <utility>
#include <vector>

class Solution {
public:
    int findTargetSumWays(std::vector<int>& nums, int target) {
        std::unordered_map<int, int> ways{{0, 1}};
        for (int value : nums) {
            std::unordered_map<int, int> following;
            for (const auto& [subtotal, count] : ways) {
                following[subtotal + value] += count;
                following[subtotal - value] += count;
            }
            ways.swap(following);
        }
        const auto found = ways.find(target);
        return found == ways.end() ? 0 : found->second;
    }
};
