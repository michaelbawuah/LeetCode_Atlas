#include <cstddef>
#include <iterator>
#include <list>
#include <unordered_map>
#include <utility>

class LRUCache {
    using Entries = std::list<std::pair<int, int>>;
    std::size_t capacity_;
    Entries usage_;
    std::unordered_map<int, Entries::iterator> slots_;
public:
    explicit LRUCache(int capacity) : capacity_(static_cast<std::size_t>(capacity)) {}
    int get(int key) {
        const auto found = slots_.find(key);
        if (found == slots_.end()) return -1;
        usage_.splice(usage_.end(), usage_, found->second);
        return found->second->second;
    }
    void put(int key, int value) {
        const auto found = slots_.find(key);
        if (found != slots_.end()) {
            found->second->second = value;
            usage_.splice(usage_.end(), usage_, found->second);
            return;
        }
        usage_.emplace_back(key, value);
        slots_[key] = std::prev(usage_.end());
        if (usage_.size() > capacity_) {
            slots_.erase(usage_.front().first);
            usage_.pop_front();
        }
    }
};
