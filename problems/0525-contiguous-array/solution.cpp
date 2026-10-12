#include <algorithm>
#include <cstddef>
#include <unordered_map>
#include <vector>

class Solution {
public:
    int findMaxLength(std::vector<int>& nums) {
        std::unordered_map<int, int> earliest{{0, -1}};
        earliest.reserve(nums.size() + 1);
        int balance = 0;
        int best = 0;
        for (std::size_t index = 0; index < nums.size(); ++index) {
            balance += nums[index] == 0 ? -1 : 1;
            const auto found = earliest.find(balance);
            if (found != earliest.end()) {
                best = std::max(best, static_cast<int>(index) - found->second);
            } else {
                earliest[balance] = static_cast<int>(index);
            }
        }
        return best;
    }
};
