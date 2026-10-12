#include <algorithm>
#include <utility>
#include <vector>

class MinStack {
    std::vector<std::pair<int, int>> entries_;
public:
    void push(int val) {
        const int minimum = entries_.empty() ? val : std::min(val, entries_.back().second);
        entries_.emplace_back(val, minimum);
    }
    void pop() { entries_.pop_back(); }
    int top() { return entries_.back().first; }
    int getMin() { return entries_.back().second; }
};
