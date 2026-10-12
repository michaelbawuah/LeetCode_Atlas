#include <bit>
#include <cstdint>
#include <vector>

class Solution {
public:
    int singleNumber(std::vector<int>& nums) {
        std::uint32_t once = 0;
        std::uint32_t twice = 0;
        for (const int value : nums) {
            const auto bits = static_cast<std::uint32_t>(value);
            once = (once ^ bits) & ~twice;
            twice = (twice ^ bits) & ~once;
        }
        return static_cast<int>(std::bit_cast<std::int32_t>(once));
    }
};
