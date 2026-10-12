#include <cstddef>
#include <vector>

class MyCircularDeque {
    std::vector<int> data_;
    std::size_t head_ = 0;
    std::size_t size_ = 0;

public:
    explicit MyCircularDeque(int k) : data_(static_cast<std::size_t>(k), 0) {}
    bool insertFront(int value) {
        if (isFull()) return false;
        head_ = (head_ + data_.size() - 1) % data_.size();
        data_[head_] = value;
        ++size_;
        return true;
    }
    bool insertLast(int value) {
        if (isFull()) return false;
        data_[(head_ + size_) % data_.size()] = value;
        ++size_;
        return true;
    }
    bool deleteFront() {
        if (isEmpty()) return false;
        head_ = (head_ + 1) % data_.size();
        --size_;
        return true;
    }
    bool deleteLast() {
        if (isEmpty()) return false;
        --size_;
        return true;
    }
    int getFront() { return isEmpty() ? -1 : data_[head_]; }
    int getRear() { return isEmpty() ? -1 : data_[(head_ + size_ - 1) % data_.size()]; }
    bool isEmpty() { return size_ == 0; }
    bool isFull() { return size_ == data_.size(); }
};
