#include <array>
#include <cstdint>
#include <numeric>
class Solution {
public:
    int countVowelPermutation(int n) {
        const std::int64_t modulus = 1'000'000'007LL;
        std::array<std::int64_t, 5> counts{1, 1, 1, 1, 1};
        for (int length = 2; length <= n; ++length) {
            const auto [a, e, i, o, u] = counts;
            counts = {(e + i + u) % modulus, (a + i) % modulus, (e + o) % modulus, i, (i + o) % modulus};
        }
        return static_cast<int>(std::accumulate(counts.begin(), counts.end(), std::int64_t{0}) % modulus);
    }
};
