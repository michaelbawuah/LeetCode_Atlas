// ListNode is supplied by the judge or local adapter.
class Solution {
public:
    ListNode* swapPairs(ListNode* head) {
        ListNode dummy(0);
        dummy.next = head;
        ListNode* previous = &dummy;
        while (previous->next != nullptr && previous->next->next != nullptr) {
            ListNode* first = previous->next;
            ListNode* second = first->next;
            first->next = second->next;
            second->next = first;
            previous->next = second;
            previous = first;
        }
        return dummy.next;
    }
};
