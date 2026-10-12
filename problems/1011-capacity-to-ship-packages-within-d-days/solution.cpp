#include <algorithm>
#include <numeric>
#include <vector>

class Solution {
public:
    int shipWithinDays(std::vector<int>& weights, int days) {
        int left = *std::max_element(weights.begin(), weights.end());
        int right = std::accumulate(weights.begin(), weights.end(), 0);
        while (left < right) {
            const int capacity = left + (right - left) / 2;
            int used = 1;
            int load = 0;
            for (const int weight : weights) {
                if (load + weight > capacity) {
                    ++used;
                    load = 0;
                }
                load += weight;
            }
            if (used <= days) {
                right = capacity;
            } else {
                left = capacity + 1;
            }
        }
        return left;
    }
};
