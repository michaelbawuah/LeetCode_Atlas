#include <cstddef>
#include <queue>
#include <string>
#include <unordered_set>
#include <utility>
#include <vector>
using std::string;
using std::vector;
class Solution {
  public:
    int openLock(vector<string> &deadends, const string &target) {
        const std::unordered_set<string> blocked(deadends.begin(), deadends.end());
        if (blocked.contains("0000"))
            return -1;
        std::unordered_set<string> seen{"0000"};
        std::queue<std::pair<string, int>> pending;
        pending.emplace("0000", 0);
        while (!pending.empty()) {
            auto [state, distance] = pending.front();
            pending.pop();
            if (state == target)
                return distance;
            for (std::size_t index = 0; index < state.size(); ++index)
                for (int step : {-1, 1}) {
                    string next = state;
                    next[index] = static_cast<char>('0' + (state[index] - '0' + step + 10) % 10);
                    if (!blocked.contains(next) && seen.insert(next).second)
                        pending.emplace(next, distance + 1);
                }
        }
        return -1;
    }
};
