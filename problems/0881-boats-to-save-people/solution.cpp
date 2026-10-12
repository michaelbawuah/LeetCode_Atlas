#include <algorithm>
#include <vector>

using std::vector;

class Solution {
public:
    int numRescueBoats(vector<int>& people, int limit) {
        vector<int> ordered = people;
        std::sort(ordered.begin(), ordered.end());
        int left = 0;
        int right = static_cast<int>(ordered.size()) - 1;
        int boats = 0;
        while (left <= right) {
            if (left < right && ordered[left] + ordered[right] <= limit) {
                ++left;
            }
            --right;
            ++boats;
        }
        return boats;
    }
};
