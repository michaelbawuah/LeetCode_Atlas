#include <algorithm>
#include <limits>
#include <vector>

using std::vector;

class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        const vector<int>& shorter = nums1.size() <= nums2.size() ? nums1 : nums2;
        const vector<int>& longer = nums1.size() <= nums2.size() ? nums2 : nums1;
        const int m = static_cast<int>(shorter.size());
        const int n = static_cast<int>(longer.size());
        const int half = (m + n + 1) / 2;
        int low = 0;
        int high = m;
        const double infinity = std::numeric_limits<double>::infinity();
        while (low <= high) {
            const int cut1 = low + (high - low) / 2;
            const int cut2 = half - cut1;
            const double left1 = cut1 == 0 ? -infinity : shorter[cut1 - 1];
            const double right1 = cut1 == m ? infinity : shorter[cut1];
            const double left2 = cut2 == 0 ? -infinity : longer[cut2 - 1];
            const double right2 = cut2 == n ? infinity : longer[cut2];
            if (left1 <= right2 && left2 <= right1) {
                if ((m + n) % 2 != 0) {
                    return std::max(left1, left2);
                }
                return (std::max(left1, left2) + std::min(right1, right2)) / 2.0;
            }
            if (left1 > right2) {
                high = cut1 - 1;
            } else {
                low = cut1 + 1;
            }
        }
        // The contract guarantees sorted inputs with nonempty combined length.
        return 0.0;
    }
};
