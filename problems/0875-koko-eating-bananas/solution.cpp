#include <algorithm>
#include <vector>

using std::vector;

class Solution {
public:
    int minEatingSpeed(vector<int>& piles, int h) {
        if (piles.empty()) {
            return 0;
        }
        int low = 1;
        int high = *std::max_element(piles.begin(), piles.end());
        while (low < high) {
            const int speed = low + (high - low) / 2;
            long long hours = 0;
            for (const int pile : piles) {
                hours += (static_cast<long long>(pile) + speed - 1) / speed;
                if (hours > h) {
                    break;
                }
            }
            if (hours <= h) {
                high = speed;
            } else {
                low = speed + 1;
            }
        }
        return low;
    }
};
