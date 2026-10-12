// ListNode is supplied by LeetCode or by the local test adapter.
class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        ListNode* previous = nullptr;
        while (head != nullptr) {
            ListNode* following = head->next;
            head->next = previous;
            previous = head;
            head = following;
        }
        return previous;
    }
};
