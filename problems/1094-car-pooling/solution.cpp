#include <map>
#include <vector>

class Solution {
public:
    bool carPooling(std::vector<std::vector<int>>& trips, int capacity) {
        std::map<int, int> changes;
        for (const auto& trip : trips) {
            changes[trip[1]] += trip[0];
            changes[trip[2]] -= trip[0];
        }
        int load = 0;
        for (const auto& [location, change] : changes) {
            static_cast<void>(location);
            load += change;
            if (load > capacity) {
                return false;
            }
        }
        return true;
    }
};
