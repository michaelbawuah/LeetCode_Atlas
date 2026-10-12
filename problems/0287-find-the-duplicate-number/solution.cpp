#include <cstddef>
#include <vector>

class Solution {
public:
    int findDuplicate(std::vector<int>& nums) {
        int slow = nums.front();
        int fast = slow;
        do {
            slow = nums[static_cast<std::size_t>(slow)];
            fast = nums[static_cast<std::size_t>(nums[static_cast<std::size_t>(fast)])];
        } while (slow != fast);
        int entry = nums.front();
        while (entry != slow) {
            entry = nums[static_cast<std::size_t>(entry)];
            slow = nums[static_cast<std::size_t>(slow)];
        }
        return entry;
    }
};
