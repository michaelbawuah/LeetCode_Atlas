#include <algorithm>
#include <cstddef>
#include <vector>

using std::vector;

class Solution {
public:
    vector<vector<int>> insert(vector<vector<int>>& intervals, vector<int>& newInterval) {
        vector<vector<int>> result;
        result.reserve(intervals.size() + 1);
        std::size_t index = 0;
        int start = newInterval[0];
        int end = newInterval[1];
        while (index < intervals.size() && intervals[index][1] < start) {
            result.push_back(intervals[index++]);
        }
        while (index < intervals.size() && intervals[index][0] <= end) {
            start = std::min(start, intervals[index][0]);
            end = std::max(end, intervals[index][1]);
            ++index;
        }
        result.push_back({start, end});
        while (index < intervals.size()) {
            result.push_back(intervals[index++]);
        }
        return result;
    }
};
