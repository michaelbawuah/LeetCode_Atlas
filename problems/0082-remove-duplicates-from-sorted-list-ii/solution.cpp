// ListNode is supplied by the judge or local adapter.
class Solution {
public:
    ListNode* deleteDuplicates(ListNode* head) {
        ListNode dummy(0);
        dummy.next = head;
        ListNode* previous = &dummy;
        ListNode* current = head;
        while (current != nullptr) {
            ListNode* end = current;
            while (end->next != nullptr && end->next->val == current->val) { end = end->next; }
            if (end == current) { previous = current; }
            else { previous->next = end->next; }
            current = end->next;
        }
        return dummy.next;
    }
};
