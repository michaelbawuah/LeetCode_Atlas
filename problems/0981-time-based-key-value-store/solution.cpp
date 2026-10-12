#include <algorithm>
#include <iterator>
#include <string>
#include <unordered_map>
#include <utility>
#include <vector>

class TimeMap {
    std::unordered_map<std::string, std::vector<std::pair<int, std::string>>> history_;
public:
    void set(std::string key, std::string value, int timestamp) {
        history_[key].emplace_back(timestamp, std::move(value));
    }
    std::string get(std::string key, int timestamp) {
        const auto found = history_.find(key);
        if (found == history_.end()) return "";
        const auto& records = found->second;
        const auto end = std::upper_bound(records.begin(), records.end(), timestamp,
            [](int time, const auto& record) { return time < record.first; });
        return end == records.begin() ? "" : std::prev(end)->second;
    }
};
