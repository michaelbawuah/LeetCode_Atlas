#include <algorithm>
#include <vector>

using std::vector;

class Solution {
public:
    int rob(vector<int>& nums) {
        long long previous = 0;
        long long two_back = 0;
        for (const int value : nums) {
            const long long best = std::max(previous, two_back + value);
            two_back = previous;
            previous = best;
        }
        // The problem's constraints bound the maximum loot below INT_MAX.
        return static_cast<int>(previous);
    }
};
