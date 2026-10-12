#include <unordered_set>
#include <vector>

using std::vector;

class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        std::unordered_set<int> seen;
        seen.reserve(nums.size());
        for (const int value : nums) {
            if (!seen.insert(value).second) {
                return true;
            }
        }
        return false;
    }
};
