#include <vector>

using std::vector;

class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int candidate = 0;
        int votes = 0;
        for (const int value : nums) {
            if (votes == 0) {
                candidate = value;
            }
            votes += value == candidate ? 1 : -1;
        }
        return candidate;
    }
};
