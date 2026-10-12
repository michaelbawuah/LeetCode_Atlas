#include <algorithm>
#include <cstddef>
#include <functional>
#include <limits>
#include <queue>
#include <utility>
#include <vector>

using std::vector;

class Solution {
public:
    int networkDelayTime(vector<vector<int>>& times, int n, int k) {
        const auto count = static_cast<std::size_t>(n) + 1;
        vector<vector<std::pair<int, int>>> adjacent(count);
        for (const auto& edge : times) {
            adjacent[static_cast<std::size_t>(edge[0])].emplace_back(edge[1], edge[2]);
        }
        const int unreachable = std::numeric_limits<int>::max();
        vector<int> distance(count, unreachable);
        distance[static_cast<std::size_t>(k)] = 0;
        using Entry = std::pair<int, int>;
        std::priority_queue<Entry, vector<Entry>, std::greater<Entry>> pending;
        pending.emplace(0, k);
        while (!pending.empty()) {
            const auto [elapsed, node] = pending.top();
            pending.pop();
            if (elapsed != distance[static_cast<std::size_t>(node)]) {
                continue;
            }
            for (const auto& [neighbor, delay] : adjacent[static_cast<std::size_t>(node)]) {
                const int arrival = elapsed + delay;
                auto& best = distance[static_cast<std::size_t>(neighbor)];
                if (arrival < best) {
                    best = arrival;
                    pending.emplace(arrival, neighbor);
                }
            }
        }
        int answer = 0;
        for (int node = 1; node <= n; ++node) {
            const int delay = distance[static_cast<std::size_t>(node)];
            if (delay == unreachable) {
                return -1;
            }
            answer = std::max(answer, delay);
        }
        return answer;
    }
};
