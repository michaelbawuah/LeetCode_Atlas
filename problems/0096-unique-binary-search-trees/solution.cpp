#include <cstddef>
#include <cstdint>
#include <vector>
class Solution {
public:
    int numTrees(int n) {
        std::vector<std::int64_t> counts(static_cast<std::size_t>(n) + 1, 0);
        counts[0] = 1;
        for (int size = 1; size <= n; ++size) {
            for (int left = 0; left < size; ++left) {
                // Widened operands are multiplied before the result is accumulated.
                counts[static_cast<std::size_t>(size)] += counts[static_cast<std::size_t>(left)] * counts[static_cast<std::size_t>(size - 1 - left)];
            }
        }
        return static_cast<int>(counts[static_cast<std::size_t>(n)]);
    }
};
