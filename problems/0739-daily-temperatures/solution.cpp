#include <cstddef>
#include <vector>

using std::vector;

class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        vector<int> waits(temperatures.size(), 0);
        vector<std::size_t> unresolved;
        unresolved.reserve(temperatures.size());
        for (std::size_t today = 0; today < temperatures.size(); ++today) {
            while (!unresolved.empty() && temperatures[today] > temperatures[unresolved.back()]) {
                const std::size_t earlier = unresolved.back();
                unresolved.pop_back();
                waits[earlier] = static_cast<int>(today - earlier);
            }
            unresolved.push_back(today);
        }
        return waits;
    }
};
