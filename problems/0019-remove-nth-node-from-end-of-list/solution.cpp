// ListNode is supplied by LeetCode or the local adapter.
class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        if (n <= 0) {
            return head;
        }
        ListNode dummy(0);
        dummy.next = head;
        ListNode* fast = &dummy;
        ListNode* slow = &dummy;
        for (int step = 0; step < n; ++step) {
            if (fast->next == nullptr) {
                return head;
            }
            fast = fast->next;
        }
        while (fast->next != nullptr) {
            fast = fast->next;
            slow = slow->next;
        }
        if (slow->next != nullptr) {
            // Detach only: the judge or ListArena owns the borrowed nodes.
            slow->next = slow->next->next;
        }
        return dummy.next;
    }
};
