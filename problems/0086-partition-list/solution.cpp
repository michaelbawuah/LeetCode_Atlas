// ListNode is supplied by the judge or local adapter.
class Solution {
public:
    ListNode* partition(ListNode* head, int x) {
        ListNode smaller(0), larger(0);
        ListNode* low = &smaller;
        ListNode* high = &larger;
        while (head != nullptr) {
            ListNode* following = head->next;
            head->next = nullptr;
            if (head->val < x) { low->next = head; low = head; }
            else { high->next = head; high = head; }
            head = following;
        }
        low->next = larger.next;
        return smaller.next;
    }
};
