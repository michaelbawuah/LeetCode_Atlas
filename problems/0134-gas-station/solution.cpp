#include <cstddef>
#include <vector>

using std::vector;

class Solution {
public:
    int canCompleteCircuit(vector<int>& gas, vector<int>& cost) {
        long long total = 0;
        long long running = 0;
        std::size_t start = 0;
        for (std::size_t index = 0; index < gas.size(); ++index) {
            const long long difference = static_cast<long long>(gas[index]) - cost[index];
            total += difference;
            running += difference;
            if (running < 0) {
                start = index + 1;
                running = 0;
            }
        }
        return total >= 0 ? static_cast<int>(start) : -1;
    }
};
