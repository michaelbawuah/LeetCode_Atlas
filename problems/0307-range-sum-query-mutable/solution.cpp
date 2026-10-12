#include <cstddef>
#include <vector>

class NumArray {
    std::vector<long long> values_;
    std::vector<long long> tree_;
    static std::size_t low_bit(std::size_t value) { return value & (~value + 1); }
    long long prefix(std::size_t end) const {
        long long sum = 0;
        while (end != 0) { sum += tree_[end]; end -= low_bit(end); }
        return sum;
    }
public:
    explicit NumArray(std::vector<int>& nums) : values_(nums.begin(), nums.end()), tree_(nums.size() + 1, 0) {
        for (std::size_t i = 0; i < nums.size(); ++i) tree_[i + 1] = nums[i];
        for (std::size_t i = 1; i < tree_.size(); ++i) {
            const auto parent = i + low_bit(i);
            if (parent < tree_.size()) tree_[parent] += tree_[i];
        }
    }
    void update(int index, int val) {
        const auto position = static_cast<std::size_t>(index);
        const long long change = static_cast<long long>(val) - values_[position];
        values_[position] = val;
        for (auto i = position + 1; i < tree_.size(); i += low_bit(i)) tree_[i] += change;
    }
    int sumRange(int left, int right) {
        return static_cast<int>(prefix(static_cast<std::size_t>(right) + 1) - prefix(static_cast<std::size_t>(left)));
    }
};
