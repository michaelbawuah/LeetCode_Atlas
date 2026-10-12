// ListNode is supplied by the judge or local adapter.
class Solution {
public:
    ListNode* reverseBetween(ListNode* head, int left, int right) {
        ListNode dummy;
        dummy.next = head;
        ListNode* before = &dummy;
        for (int position = 1; position < left; ++position) {
            before = before->next;
        }
        ListNode* first = before->next;
        for (int offset = 0; offset < right - left; ++offset) {
            ListNode* moved = first->next;
            first->next = moved->next;
            moved->next = before->next;
            before->next = moved;
        }
        return dummy.next;
    }
};
