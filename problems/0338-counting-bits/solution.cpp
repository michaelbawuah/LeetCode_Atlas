#include <cstddef>
#include <vector>

using std::vector;

class Solution {
public:
    vector<int> countBits(int n) {
        vector<int> counts(static_cast<std::size_t>(n) + 1, 0);
        for (int value = 1; value <= n; ++value) {
            counts[static_cast<std::size_t>(value)] =
                counts[static_cast<std::size_t>(value >> 1)] + (value & 1);
        }
        return counts;
    }
};
