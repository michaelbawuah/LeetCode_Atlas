#include <stack>

class MyQueue {
    std::stack<int> incoming_;
    std::stack<int> outgoing_;

    void prepare() {
        if (!outgoing_.empty()) return;
        while (!incoming_.empty()) {
            outgoing_.push(incoming_.top());
            incoming_.pop();
        }
    }

public:
    MyQueue() = default;
    void push(int x) { incoming_.push(x); }
    int pop() {
        prepare();
        const int value = outgoing_.top();
        outgoing_.pop();
        return value;
    }
    int peek() {
        prepare();
        return outgoing_.top();
    }
    bool empty() { return incoming_.empty() && outgoing_.empty(); }
};
