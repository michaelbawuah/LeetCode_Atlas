#include <cstddef>
#include <functional>
#include <queue>
#include <vector>

class KthLargest {
    std::size_t k_;
    std::priority_queue<int, std::vector<int>, std::greater<int>> largest_;
public:
    KthLargest(int k, std::vector<int>& nums) : k_(static_cast<std::size_t>(k)) {
        for (int value : nums) static_cast<void>(add(value));
    }
    int add(int val) {
        if (largest_.size() < k_) largest_.push(val);
        else if (val > largest_.top()) { largest_.pop(); largest_.push(val); }
        return largest_.top();
    }
};
