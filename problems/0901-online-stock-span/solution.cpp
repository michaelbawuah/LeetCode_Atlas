#include <utility>
#include <vector>
class StockSpanner {
    std::vector<std::pair<int,int>> pending_;
public:
    int next(int price) {
        int span = 1;
        while (!pending_.empty() && pending_.back().first <= price) { span += pending_.back().second; pending_.pop_back(); }
        pending_.emplace_back(price, span); return span;
    }
};
