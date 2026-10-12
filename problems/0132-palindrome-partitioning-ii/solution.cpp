#include <algorithm>
#include <cstddef>
#include <string>
#include <vector>

class Solution {
public:
    int minCut(std::string s) {
        const int size = static_cast<int>(s.size());
        std::vector<int> cuts(s.size() + 1);
        for (int length = 0; length <= size; ++length) {
            cuts[static_cast<std::size_t>(length)] = length - 1;
        }
        for (int center = 0; center < size; ++center) {
            for (int gap = 0; gap <= 1; ++gap) {
                int left = center;
                int right = center + gap;
                while (left >= 0 && right < size &&
                       s[static_cast<std::size_t>(left)] == s[static_cast<std::size_t>(right)]) {
                    const auto end = static_cast<std::size_t>(right + 1);
                    cuts[end] = std::min(cuts[end], cuts[static_cast<std::size_t>(left)] + 1);
                    --left;
                    ++right;
                }
            }
        }
        return cuts.back();
    }
};
