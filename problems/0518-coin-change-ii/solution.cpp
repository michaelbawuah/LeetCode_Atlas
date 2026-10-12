#include <algorithm>
#include <cstddef>
#include <cstdint>
#include <limits>
#include <vector>

using std::vector;

class Solution {
public:
    int change(int amount, vector<int>& coins) {
        // Only the final answer is bounded; intermediate subtotals may exceed even 64 bits.
        const std::int64_t cap = std::numeric_limits<int>::max();
        vector<std::int64_t> counts(static_cast<std::size_t>(amount) + 1, 0);
        counts[0] = 1;
        for (const int coin : coins) {
            for (int subtotal = coin; subtotal <= amount; ++subtotal) {
                const auto index = static_cast<std::size_t>(subtotal);
                const auto previous = static_cast<std::size_t>(subtotal - coin);
                // Both operands are 64-bit and capped; their sum is at most 2 * INT_MAX.
                counts[index] = std::min(cap, counts[index] + counts[previous]);
            }
        }
        // Saturating nonnegative additions produce min(true_count, cap).
        // The guaranteed-bounded final true_count therefore remains exact.
        return static_cast<int>(counts[static_cast<std::size_t>(amount)]);
    }
};
