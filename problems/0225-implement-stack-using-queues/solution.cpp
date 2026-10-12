#include <cstddef>
#include <queue>

class MyStack {
    std::queue<int> values_;

public:
    MyStack() = default;
    void push(int x) {
        const std::size_t previous = values_.size();
        values_.push(x);
        for (std::size_t index = 0; index < previous; ++index) {
            values_.push(values_.front());
            values_.pop();
        }
    }
    int pop() {
        const int value = values_.front();
        values_.pop();
        return value;
    }
    int top() { return values_.front(); }
    bool empty() { return values_.empty(); }
};
