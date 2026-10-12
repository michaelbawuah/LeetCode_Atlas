#include <deque>
class RecentCounter {
    std::deque<int> times_;
public:
    int ping(int t) {
        times_.push_back(t);
        while (times_.front() < t - 3000) times_.pop_front();
        return static_cast<int>(times_.size());
    }
};
