// ListNode is supplied by the judge or local adapter.
class Solution {
public:
    void reorderList(ListNode* head) {
        if (head == nullptr || head->next == nullptr) {
            return;
        }
        ListNode* slow = head;
        ListNode* fast = head;
        while (fast->next != nullptr && fast->next->next != nullptr) {
            slow = slow->next;
            fast = fast->next->next;
        }
        ListNode* second = slow->next;
        slow->next = nullptr;
        ListNode* previous = nullptr;
        while (second != nullptr) {
            ListNode* following = second->next;
            second->next = previous;
            previous = second;
            second = following;
        }
        ListNode* first = head;
        second = previous;
        while (second != nullptr) {
            ListNode* first_next = first->next;
            ListNode* second_next = second->next;
            first->next = second;
            second->next = first_next;
            first = first_next;
            second = second_next;
        }
    }
};
