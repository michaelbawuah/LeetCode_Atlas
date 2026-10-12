#include <algorithm>
#include <cstddef>
#include <vector>
class Solution {
public:
    int numSquares(int n) {
        std::vector<int> squares;
        for (int root = 1; root * root <= n; ++root) {
            squares.push_back(root * root);
        }
        std::vector<int> best(static_cast<std::size_t>(n) + 1, n + 1);
        best[0] = 0;
        for (int total = 1; total <= n; ++total) {
            for (const int square : squares) {
                if (square > total) {
                    break;
                }
                const auto index = static_cast<std::size_t>(total);
                best[index] = std::min(best[index], best[static_cast<std::size_t>(total - square)] + 1);
            }
        }
        return best[static_cast<std::size_t>(n)];
    }
};
