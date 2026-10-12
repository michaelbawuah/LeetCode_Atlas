#include <iterator>
#include <map>

class MyCalendar {
    std::map<int, int> bookings_;

public:
    MyCalendar() = default;
    bool book(int startTime, int endTime) {
        const auto next = bookings_.lower_bound(startTime);
        if (next != bookings_.end() && next->first < endTime) return false;
        if (next != bookings_.begin() && std::prev(next)->second > startTime) return false;
        bookings_.emplace_hint(next, startTime, endTime);
        return true;
    }
};
