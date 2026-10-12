// ListNode is supplied by the judge or local adapter.
class Solution {
public:
    ListNode* rotateRight(ListNode* head, int k) {
        if (head == nullptr || head->next == nullptr) { return head; }
        ListNode* tail = head;
        int length = 1;
        while (tail->next != nullptr) { tail = tail->next; ++length; }
        const int shift = k % length;
        if (shift == 0) { return head; }
        ListNode* new_tail = head;
        for (int step = 0; step < length - shift - 1; ++step) { new_tail = new_tail->next; }
        ListNode* new_head = new_tail->next;
        tail->next = head;
        new_tail->next = nullptr;
        return new_head;
    }
};
