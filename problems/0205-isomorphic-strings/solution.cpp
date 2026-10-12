#include <array>
#include <cstddef>
#include <string>
class Solution {
public:
    bool isIsomorphic(const std::string& s, const std::string& t) {
        std::array<int, 256> forward, backward; forward.fill(-1); backward.fill(-1);
        for (std::size_t i = 0; i < s.size(); ++i) {
            const auto a = static_cast<unsigned char>(s[i]), b = static_cast<unsigned char>(t[i]);
            if ((forward[a] != -1 && forward[a] != b) || (backward[b] != -1 && backward[b] != a)) return false;
            forward[a] = b; backward[b] = a;
        }
        return true;
    }
};
