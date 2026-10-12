#include <cstddef>
#include <vector>

class Solution {
public:
    void merge(std::vector<int>& nums1, int m, std::vector<int>& nums2, int n) {
        int first = m - 1;
        int second = n - 1;
        int write = m + n - 1;
        while (second >= 0) {
            const auto destination = static_cast<std::size_t>(write);
            if (first >= 0 && nums1[static_cast<std::size_t>(first)] > nums2[static_cast<std::size_t>(second)]) {
                nums1[destination] = nums1[static_cast<std::size_t>(first--)];
            } else {
                nums1[destination] = nums2[static_cast<std::size_t>(second--)];
            }
            --write;
        }
    }
};
