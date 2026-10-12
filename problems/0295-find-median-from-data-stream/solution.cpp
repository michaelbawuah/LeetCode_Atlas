#include <functional>
#include <queue>
#include <vector>

class MedianFinder {
    std::priority_queue<int> lower_;
    std::priority_queue<int, std::vector<int>, std::greater<int>> upper_;

public:
    MedianFinder() = default;
    void addNum(int num) {
        lower_.push(num);
        upper_.push(lower_.top());
        lower_.pop();
        if (upper_.size() > lower_.size()) {
            lower_.push(upper_.top());
            upper_.pop();
        }
    }
    double findMedian() {
        if (lower_.size() > upper_.size()) return static_cast<double>(lower_.top());
        // Convert before addition so the integer sum cannot overflow.
        return (static_cast<double>(lower_.top()) + static_cast<double>(upper_.top())) / 2.0;
    }
};
