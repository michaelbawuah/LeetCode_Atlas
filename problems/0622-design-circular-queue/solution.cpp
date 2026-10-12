#include <cstddef>
#include <vector>
class MyCircularQueue {
    std::vector<int> data_; std::size_t head_ = 0, size_ = 0;
public:
    explicit MyCircularQueue(int k) : data_(static_cast<std::size_t>(k), 0) {}
    bool enQueue(int value) {
        if (isFull()) return false;
        data_[(head_ + size_) % data_.size()] = value; ++size_; return true;
    }
    bool deQueue() {
        if (isEmpty()) return false;
        head_ = (head_ + 1) % data_.size(); --size_; return true;
    }
    int Front() { return isEmpty() ? -1 : data_[head_]; }
    int Rear() { return isEmpty() ? -1 : data_[(head_ + size_ - 1) % data_.size()]; }
    bool isEmpty() { return size_ == 0; }
    bool isFull() { return size_ == data_.size(); }
};
