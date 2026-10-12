#include <cstddef>
#include <vector>

class Solution {
public:
    std::vector<int> findClosestElements(std::vector<int>& arr, int k, int x) {
        std::size_t left = 0;
        std::size_t right = arr.size() - static_cast<std::size_t>(k);
        while (left < right) {
            const auto middle = left + (right - left) / 2;
            if (x - arr[middle] > arr[middle + static_cast<std::size_t>(k)] - x) {
                left = middle + 1;
            } else {
                right = middle;
            }
        }
        const auto first = arr.begin() + static_cast<std::ptrdiff_t>(left);
        return std::vector<int>(first, first + k);
    }
};
